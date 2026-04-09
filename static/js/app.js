/* ─── Shared utilities ────────────────────── */

function escHtml(str) {
    if (!str) return '';
    return $('<span>').text(str).html();
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
        var typeLabel = (a.aircraft_type || 'fixed_wing').replace(/_/g, ' ');
        var milCiv = a.military_civilian || 'military';
        var roleLabel = (a.role_type || '—').replace(/_/g, ' ');
        html += '<tr class="aircraft-row" data-id="' + a.id + '">' +
            '<td><strong>' + escHtml(a.full_designation || a.model) + '</strong></td>' +
            '<td>' + escHtml(a.model_name || '—') + '</td>' +
            '<td>' + escHtml(a.aircraft_name || '—') + '</td>' +
            '<td>' + escHtml(a.tail_number || '—') + '</td>' +
            '<td>' + escHtml(a.manufacturer) + '</td>' +
            '<td>' + escHtml(typeLabel) + '</td>' +
            '<td><span class="badge status-' + milCiv + '">' + milCiv + '</span></td>' +
            '<td>' + escHtml(roleLabel) + '</td>' +
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
