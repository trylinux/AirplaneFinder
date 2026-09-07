/* Shared UI and request helpers for histories, discovery, and trip planning. */
window.Explorer = (() => {
    function el(tag, text, className) {
        const node = document.createElement(tag);
        if (text != null) node.textContent = text;
        if (className) node.className = className;
        return node;
    }
    function link(text, href, className) {
        const node = el('a', text, className); node.href = href; return node;
    }
    async function api(url, options = {}) {
        const headers = {Accept:'application/json', ...options.headers};
        if (options.body != null) {
            headers['Content-Type'] = 'application/json';
            headers['X-CSRFToken'] = document.querySelector('meta[name="csrf-token"]')?.content || '';
        }
        const response = await fetch(url, {...options, headers});
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.error || (response.status === 429 ? 'Too many requests. Please wait a minute.' : 'Could not complete the request. Please try again.'));
        return data;
    }
    function message(node, text, error = false) {
        node.textContent = text; node.classList.toggle('is-error', error);
    }
    function directions(museum) {
        const destination = museum.latitude != null && museum.longitude != null
            ? `${museum.latitude},${museum.longitude}` : [museum.name, museum.address, museum.city, museum.country].filter(Boolean).join(', ');
        return 'https://www.google.com/maps/dir/?' + new URLSearchParams({api:'1', destination});
    }
    function external(text, href) {
        const node = link(text, href, 'x-button secondary'); node.target = '_blank'; node.rel = 'noopener noreferrer'; return node;
    }
    return {el, link, api, message, directions, external};
})();
