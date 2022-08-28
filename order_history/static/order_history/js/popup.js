let window_object_reference = null;

const open_requested_window = (url) => {
    if (window_object_reference === null || window_object_reference.closed) {
        window_object_reference = window.open(url, "subwin", "width=500, height=500", "popup");
    } else {
        window_object_reference.focus();
    }
};

const elements_popup_btn = document.getElementsByClassName("popup_btn");
for (let i = 0; i < elements_popup_btn.length; i++) {
    const popup_btn = elements_popup_btn[i];
    popup_btn.addEventListener("click", (event) => {
        open_requested_window(popup_btn.href);
        event.preventDefault();
    }, false);
}
