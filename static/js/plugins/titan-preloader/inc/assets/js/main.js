'use strict';

const fire_outro_complete = (href) => {
    const event = new CustomEvent('titan-outro-complete', { detail: href });
    window.dispatchEvent(event);
};

const execute_outro_transition = (href) => {
    if (typeof titan_outro === 'undefined') {
        // this is an excluded page and does not contain any preloader markup
        fire_outro_complete(href);
        return;
    }

    const body = document.body;
    if (body != null) {
        let state = body.classList.contains('gfx-titan-page-transitions-off');
        if (state) {
            // page transitions are off
            fire_outro_complete(href);
            return;
        }
    }

    titan_outro(href);
};

const transition_handler = (e) => {
    let target = e.target.closest('a');
    if (target == null) return;

    if (target.matches('#wpadminbar a')) return;
    let href = target.getAttribute('href');
    let targetAttr = target.getAttribute('target');
    if (
        href == null ||
        href == '' ||
        href == '#' ||
        href.startsWith('javascript')
    )
        return;
    if (targetAttr != null && targetAttr != '' && targetAttr != '_self') return;
    e.preventDefault();
    execute_outro_transition(href);
};

document.addEventListener('click', (e) => {
    transition_handler(e);
});

window.addEventListener('titan-intro-complete', () => {
    if (typeof titan_intro === 'undefined') return;
    if (TITAN_DEMO_MODE) setTimeout(titan_intro, 3000);
    else titan_intro();
});

window.addEventListener('titan-outro-complete', (e) => {
    window.location.href = e.detail;
});

/**
 * Problem:
 *  On pressing the back button, the page is stuck with the preloader covering the page.
 *  The JavaScript is not properly executed when navigating back to the previous page.
 * Solution:
 *  Add an event listener to the window 'unload' event.
 */
window.addEventListener('unload', () => {});