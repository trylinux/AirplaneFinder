/* ─── CSRF token setup ────────────────────── */

// Send the CSRF token with every jQuery AJAX request so that
// session-based POST/PUT/PATCH/DELETE calls pass Flask-WTF validation.
$(function() {
    var csrfToken = $('meta[name="csrf-token"]').attr('content');
    if (csrfToken) {
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS)$/i.test(settings.type)) {
                    xhr.setRequestHeader('X-CSRFToken', csrfToken);
                }
            }
        });
    }
});

/* ─── Shared utilities ────────────────────── */

function escHtml(str) {
    if (!str) return '';
    return $('<span>').text(str).html();
}

/* Hand-curated labels for enum values where the default snake_case →
 * Title Case rule reads awkwardly:
 *   missile_rocket   → "Missile / Rocket"  (combined category)
 *   air_to_air, etc. → "Air-to-Air"        (military convention is hyphens, not spaces)
 * Anything not in this map falls through to the default prettifier below.
 */
var PRETTY_ENUM_OVERRIDES = {
    missile_rocket:  'Missile / Rocket',
    air_to_air:      'Air-to-Air',
    surface_to_air:  'Surface-to-Air',
    air_to_surface:  'Air-to-Surface',
    anti_ship:       'Anti-Ship',
};

/* Convert a snake_case enum value to a Title Case display label.
 * Empty/null -> "—". Used for aircraft_type, military_civilian, role_type,
 * wing_type, display_status, etc. Do NOT use the result as a CSS class name —
 * keep the raw value for that. */
function prettyEnum(s) {
    if (s == null || s === '') return '—';
    if (Object.prototype.hasOwnProperty.call(PRETTY_ENUM_OVERRIDES, s)) {
        return PRETTY_ENUM_OVERRIDES[s];
    }
    return String(s).replace(/_/g, ' ').replace(/\b\w/g, function(c) {
        return c.toUpperCase();
    });
}

/* attachSortableHeaders($container, options)
 *
 * Make every <th data-sort="field"> inside $container clickable to sort.
 * First click sorts ascending; second click on the same column flips to
 * descending; clicking a different column resets to ascending on that one.
 *
 * options:
 *   getState: () => ({sort_by, sort_dir})       — read current sort
 *   setState: ({sort_by, sort_dir}) => void     — write + reload the table
 *
 * Adds an ▲/▼ glyph on the active column's header. Idempotent — safe to
 * call after every re-render of the table.
 */
function attachSortableHeaders($container, options) {
    var $hdrs = $container.find('th[data-sort]');
    var state = options.getState() || {};

    $hdrs.each(function() {
        var $th = $(this);
        var key = $th.data('sort');
        $th.addClass('sortable-th').css('cursor', 'pointer');
        // Strip any indicator from a previous render before deciding what to add.
        $th.find('.sort-indicator').remove();
        if (state.sort_by === key) {
            var arrow = state.sort_dir === 'desc' ? '▼' : '▲';
            $th.append(' <span class="sort-indicator">' + arrow + '</span>');
        }
    });

    // Use one delegated listener on the container so re-rendering the
    // <table> doesn't strip the click handler.
    $container.off('click.sortable').on('click.sortable', 'th[data-sort]', function() {
        var key = $(this).data('sort');
        var cur = options.getState() || {};
        var nextDir = (cur.sort_by === key && cur.sort_dir === 'asc') ? 'desc' : 'asc';
        options.setState({sort_by: key, sort_dir: nextDir});
    });
}

function renderAircraftResults(results, total, container, page, pages) {
    var $c = $(container);

    if (!results || results.length === 0) {
        $c.html('<p class="no-results">No aircraft found.</p>');
        return;
    }

    var html = '<div class="results-meta"><span>' + total + ' aircraft found</span></div>';

    // data-sort attributes match _AIRCRAFT_SORT_COLUMNS in app.py. The page
    // wiring (templates/aircraft.html) calls attachSortableHeaders() to
    // make these headers clickable.
    html += '<table class="result-table"><thead><tr>' +
        '<th data-sort="full_designation">Designation</th>' +
        '<th data-sort="model_name">Model Name</th>' +
        '<th data-sort="aircraft_name">Aircraft Name</th>' +
        '<th data-sort="tail_number">Tail #</th>' +
        '<th data-sort="manufacturer">Manufacturer</th>' +
        '<th data-sort="aircraft_type">Type</th>' +
        '<th data-sort="military_civilian">Mil/Civ</th>' +
        '<th data-sort="role_type">Role</th>' +
        '<th data-sort="year_built">Year</th>' +
    '</tr></thead><tbody>';

    results.forEach(function(a) {
        var milCivRaw = a.military_civilian || 'military';   // raw, used for CSS class
        html += '<tr class="aircraft-row" data-id="' + a.id + '">' +
            '<td><strong>' + escHtml(a.full_designation || a.model) + '</strong></td>' +
            '<td>' + escHtml(a.model_name || '—') + '</td>' +
            '<td>' + escHtml(a.aircraft_name || '—') + '</td>' +
            '<td>' + escHtml(a.tail_number || '—') + '</td>' +
            '<td>' + escHtml(a.manufacturer) + '</td>' +
            '<td>' + escHtml(prettyEnum(a.aircraft_type || 'fixed_wing')) + '</td>' +
            '<td><span class="badge status-' + milCivRaw + '">' + escHtml(prettyEnum(milCivRaw)) + '</span></td>' +
            '<td>' + escHtml(prettyEnum(a.role_type)) + '</td>' +
            '<td>' + (a.year_built || '—') + '</td>' +
        '</tr>';
    });

    html += '</tbody></table>';

    // Pagination
    if (pages && pages > 1) {
        html += '<div class="pagination">';
        for (var i = 1; i <= pages; i++) {
            html += '<button class="page-btn' + (i === page ? ' active' : '') + '" data-page="' + i + '">' + i + '</button>';
        }
        html += '</div>';
    }

    $c.html(html);
}

function renderMuseumResults(results, total, container, page, pages) {
    var $c = $(container);

    if (!results || results.length === 0) {
        $c.html('<p class="no-results">No museums found.</p>');
        return;
    }

    var html = '<div class="results-meta"><span>' + total + ' museums found</span></div>';

    // data-sort attributes match _MUSEUM_SORT_COLUMNS in app.py.
    html += '<table class="result-table"><thead><tr>' +
        '<th data-sort="name">Museum</th>' +
        '<th data-sort="city">City</th>' +
        '<th data-sort="country">Country</th>' +
        '<th data-sort="region">Region</th>' +
    '</tr></thead><tbody>';

    results.forEach(function(m) {
        var loc = escHtml(m.city);
        if (m.state_province) loc += ', ' + escHtml(m.state_province);
        html += '<tr class="museum-row" data-id="' + m.id + '">' +
            '<td><strong>' + escHtml(m.name) + '</strong></td>' +
            '<td>' + loc + '</td>' +
            '<td>' + escHtml(m.country) + '</td>' +
            '<td>' + escHtml(m.region) + '</td>' +
        '</tr>';
    });

    html += '</tbody></table>';

    if (pages && pages > 1) {
        html += '<div class="pagination">';
        for (var i = 1; i <= pages; i++) {
            html += '<button class="page-btn' + (i === page ? ' active' : '') + '" data-page="' + i + '">' + i + '</button>';
        }
        html += '</div>';
    }

    $c.html(html);
}
