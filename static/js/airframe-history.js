(() => {
    const {el, api, link, message} = Explorer;
    const root = document.querySelector('#history-app'), editing = root.dataset.editing === 'true';
    const url = `/api/v1/aircraft/${root.dataset.aircraftId}/history`;
    const list = document.querySelector('#history-events'), status = document.querySelector('#history-status');
    const form = document.querySelector('#history-form'), saveStatus = document.querySelector('#history-save-status');
    let editId = null;
    function dateLabel(event) {
        if (event.event_year == null) return 'Date unknown';
        let label = String(event.event_year);
        if (event.event_month != null) label = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][event.event_month - 1] + ' ' + label;
        if (event.event_day != null) label = event.event_day + ' ' + label;
        return (event.is_approximate ? 'Around ' : '') + label;
    }
    function reset() { editId = null; form.reset(); document.querySelector('#history-form-title').textContent = 'Add a milestone'; }
    async function load() {
        try {
            const events = await api(url + (editing ? '/manage' : ''));
            list.replaceChildren();
            message(status, events.length ? `${events.length} recorded milestone${events.length === 1 ? '' : 's'}.` : 'No history has been recorded for this airframe yet.');
            for (const event of events) {
                const item = el('li', null, 'x-card x-event');
                item.append(el('div', dateLabel(event), 'x-event-date'), el('h2', event.title));
                if (!event.is_published) item.append(el('span', 'Draft · hidden from visitors', 'x-tag'));
                item.append(el('span', event.event_type, 'x-tag'));
                if (event.description) item.append(el('p', event.description));
                for (const [field, label] of [['operator','Operator'], ['location','Location'], ['registration','Registration']]) {
                    if (event[field]) item.append(el('p', `${label}: ${event[field]}`, 'x-muted'));
                }
                const source = el('p', 'Source: ', 'x-muted');
                if (event.source_url) {
                    const a = link(event.source_name || event.source_url, event.source_url); a.target = '_blank'; a.rel = 'noopener noreferrer'; source.append(a);
                } else source.append(document.createTextNode(event.source_name));
                item.append(source);
                if (editing) {
                    const actions = el('div', null, 'x-actions'), edit = el('button', 'Edit', 'x-button secondary');
                    edit.type = 'button';
                    edit.onclick = () => {
                        reset(); editId = event.id;
                        for (const field of form.elements) {
                            if (!field.name) continue;
                            if (field.type === 'checkbox') field.checked = Boolean(event[field.name]);
                            else field.value = event[field.name] ?? '';
                        }
                        document.querySelector('#history-form-title').textContent = 'Edit milestone';
                        message(saveStatus, ''); form.scrollIntoView({behavior:'smooth', block:'start'}); form.elements.title.focus({preventScroll:true});
                    };
                    actions.append(edit);
                    if (root.dataset.canDelete === 'true') {
                        const remove = el('button','Delete','x-button danger'); remove.type = 'button';
                        remove.onclick = async () => {
                            if (!confirm('Delete this history milestone?')) return;
                            remove.disabled = true;
                            try { await api(`/api/v1/history/${event.id}`, {method:'DELETE', body:'{}'}); if (editId === event.id) reset(); await load(); }
                            catch (error) { message(status,error.message,true); remove.disabled = false; }
                        }; actions.append(remove);
                    }
                    item.append(actions);
                }
                list.append(item);
            }
        } catch (error) { message(status,error.message,true); }
    }
    if (form) {
        document.querySelector('#history-cancel').onclick = () => {reset(); message(saveStatus,'');};
        form.onsubmit = async event => {
            event.preventDefault(); const data = Object.fromEntries(new FormData(form));
            for (const field of ['event_year','event_month','event_day']) data[field] = data[field] ? Number(data[field]) : null;
            data.is_published = form.elements.is_published.checked; data.is_approximate = form.elements.is_approximate.checked;
            const button = form.querySelector('[type="submit"]'); button.disabled = true;
            try { await api(editId ? `/api/v1/history/${editId}` : url, {method:editId ? 'PATCH' : 'POST', body:JSON.stringify(data)}); reset(); message(saveStatus,'Milestone saved.'); await load(); }
            catch (error) { message(saveStatus,error.message,true); }
            finally { button.disabled = false; }
        };
    }
    load();
})();
