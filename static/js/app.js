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

/* Convert a snake_case enum value to a Title Case display label.
 * Empty/null -> "—". Used for aircraft_type, military_civilian, role_type,
 * wing_type, display_status, etc. Do NOT use the result as a CSS class name —
 * keep the raw value for that. */
function prettyEnum(s) {
    if (s == null || s === '') return '—';
    return String(s).replace(/_/g, ' ').replace(/\b\w/g, function(c) {
        return c.toUpperCase();
    });
}

function renderAircraftResults(results, total, container, page, pages) {
    var $c = $(container);

    if (!results || results.length === 0) {
        $c.html('<p class="no-results">No aircraft found.</p>');
        return;
    }

    var html = '<div class="results-meta"><span>' + total + ' aircraft found</span></div>';

    html += '<table class="result-table"><thead><tr>' +
        '<th>Designation</th><th>Model Name</th><th>Aircraft Name</th><th>Tail #</th><th>Manufacturer</th><th>Type</th><th>Mil/Civ</th><th>Role</th><th>Year</th>' +
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

    html += '<table class="result-table"><thead><tr>' +
        '<th>Museum</th><th>City</th><th>Country</th><th>Region</th>' +
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
