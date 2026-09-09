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

function escHtml(s) {
    if (s == null) return '';
    return String(s).replace(/[&<>"']/g, function(c) {
        return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c];
    });
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

/* pageWindow(page, pages, radius)
 *
 * Which page numbers a pager should show: the first and last page, the
 * current page and `radius` neighbours each side, with null marking a gap.
 * e.g. pageWindow(150, 300, 2) → [1, null, 148, 149, 150, 151, 152, null, 300]
 * Shared by the desktop pager below and templates/mobile/base.html — keep
 * the two copies identical.
 */
function pageWindow(page, pages, radius) {
    radius = radius == null ? 2 : radius;
    var out = [], last = 0;
    for (var i = 1; i <= pages; i++) {
        if (i === 1 || i === pages || Math.abs(i - page) <= radius) {
            // A one-page hole is shown as the page itself — "3 … 5" is silly.
            if (i - last === 2) out.push(i - 1);
            else if (i - last > 2) out.push(null);
            out.push(i);
            last = i;
        }
    }
    return out;
}

/* renderPagination(page, pages)
 *
 * Windowed pager HTML: ‹ 1 … 148 149 [150] 151 152 … 300 ›. Rendering every
 * page as a button (the old behaviour) put hundreds of buttons in a
 * non-wrapping flex row; the row was centred, so the visible slice started
 * somewhere in the 100s and pages 1..N were unreachable. Every button
 * carries data-page, which the page-level click handler reads.
 */
function renderPagination(page, pages) {
    if (!pages || pages < 2) return '';
    page = Math.min(Math.max(page || 1, 1), pages);
    var html = '<nav class="pagination" aria-label="Pagination">';
    html += '<button class="page-btn page-nav" data-page="' + (page - 1) + '"' +
        (page <= 1 ? ' disabled' : '') + ' aria-label="Previous page">&lsaquo;</button>';
    pageWindow(page, pages, 2).forEach(function(n) {
        if (n === null) { html += '<span class="page-gap" aria-hidden="true">…</span>'; return; }
        html += '<button class="page-btn' + (n === page ? ' active' : '') + '" data-page="' + n + '"' +
            (n === page ? ' aria-current="page"' : '') + '>' + n + '</button>';
    });
    html += '<button class="page-btn page-nav" data-page="' + (page + 1) + '"' +
        (page >= pages ? ' disabled' : '') + ' aria-label="Next page">&rsaquo;</button>';
    html += '<span class="page-status">Page ' + page + ' of ' + pages + '</span>';
    html += '</nav>';
    return html;
}

/* Footer for un-paged embeds (dashboard quick search): the API only sent
 * one page, so point at the full directory when there is more. */
function renderViewAll(results, total, url) {
    if (!url || !results || total <= results.length) return '';
    return '<div class="results-more"><a href="' + escHtml(url) + '">View all ' + total +
        ' results <i class="fa-solid fa-arrow-right"></i></a></div>';
}

function renderAircraftResults(results, total, container, page, pages, viewAllUrl) {
    var $c = $(container);

    if (!results || results.length === 0) {
        $c.html('<p class="no-results">No aircraft found.</p>');
        return;
    }

    var html = '<div class="results-meta"><span>' + total + ' aircraft found</span></div>';

    // data-sort attributes match _AIRCRAFT_SORT_COLUMNS in app.py. The page
    // wiring (templates/aircraft.html) calls attachSortableHeaders() to
    // make these headers clickable.
    html += '<div class="table-scroll"><table class="result-table"><thead><tr>' +
        '<th data-sort="manufacturer">Manufacturer</th>' +
        '<th data-sort="full_designation">Designation</th>' +
        '<th data-sort="model_name">Model Name</th>' +
        '<th data-sort="aircraft_name">Aircraft Name</th>' +
        '<th data-sort="tail_number">Tail #</th>' +
        '<th data-sort="aircraft_type">Type</th>' +
        '<th data-sort="military_civilian">Mil/Civ</th>' +
        '<th data-sort="role_type">Role</th>' +
        '<th data-sort="year_built">Year</th>' +
    '</tr></thead><tbody>';

    results.forEach(function(a) {
        var milCivRaw = a.military_civilian || 'military';   // raw, used for CSS class
        // Manufacturer leads, then the designation — an aircraft reads
        // "Lockheed SR-71", not "SR-71, Lockheed". Both cells are real
        // anchors so middle-click / open-in-new-tab work and the names are
        // crawlable; the row click handler defers to them.
        var href = '/aircraft/' + a.id;
        html += '<tr class="aircraft-row" data-id="' + a.id + '">' +
            '<td><a class="row-link" href="' + href + '">' +
                escHtml(a.manufacturer || '—') + '</a></td>' +
            '<td><a class="row-link" href="' + href + '"><strong>' +
                escHtml(a.full_designation || a.model) + '</strong></a></td>' +
            '<td>' + escHtml(a.model_name || '—') + '</td>' +
            '<td>' + escHtml(a.aircraft_name || '—') + '</td>' +
            '<td>' + escHtml(a.tail_number || '—') + '</td>' +
            '<td>' + escHtml(prettyEnum(a.aircraft_type || 'fixed_wing')) + '</td>' +
            '<td><span class="badge status-' + milCivRaw + '">' + escHtml(prettyEnum(milCivRaw)) + '</span></td>' +
            '<td>' + escHtml(prettyEnum(a.role_type)) + '</td>' +
            '<td>' + (a.year_built || '—') + '</td>' +
        '</tr>';
    });

    html += '</tbody></table></div>';
    html += renderPagination(page, pages);
    html += renderViewAll(results, total, viewAllUrl);

    $c.html(html);
}

function renderMuseumResults(results, total, container, page, pages, viewAllUrl) {
    var $c = $(container);

    if (!results || results.length === 0) {
        $c.html('<p class="no-results">No museums found.</p>');
        return;
    }

    var html = '<div class="results-meta"><span>' + total + ' museums found</span></div>';

    // data-sort attributes match _MUSEUM_SORT_COLUMNS in app.py.
    html += '<div class="table-scroll"><table class="result-table"><thead><tr>' +
        '<th data-sort="name">Museum</th>' +
        '<th data-sort="city">City</th>' +
        '<th data-sort="country">Country</th>' +
        '<th data-sort="region">Region</th>' +
    '</tr></thead><tbody>';

    results.forEach(function(m) {
        var loc = escHtml(m.city);
        if (m.state_province) loc += ', ' + escHtml(m.state_province);
        html += '<tr class="museum-row" data-id="' + m.id + '">' +
            '<td><a class="row-link" href="/museums/' + m.id + '"><strong>' +
                escHtml(m.name) + '</strong></a></td>' +
            '<td>' + loc + '</td>' +
            '<td>' + escHtml(m.country) + '</td>' +
            '<td>' + escHtml(m.region) + '</td>' +
        '</tr>';
    });

    html += '</tbody></table></div>';
    html += renderPagination(page, pages);
    html += renderViewAll(results, total, viewAllUrl);

    $c.html(html);
}


// Admin lists and pickers need the full catalog; the API caps each page at 100.
// Return the familiar {results, total} shape only after every page succeeds.
function fetchAllResults(url, params, success) {
    var deferred = $.Deferred(), results = [];
    function next(page) {
        $.getJSON(url, $.extend({}, params, {page: page, per_page: 100}))
            .done(function(data) {
                results = results.concat(data.results || []);
                if (page < data.pages) next(page + 1);
                else deferred.resolve({results: results, total: data.total});
            }).fail(function(xhr) { deferred.reject(xhr); });
    }
    if (success) deferred.done(success);
    next(1);
    return deferred.promise();
}
