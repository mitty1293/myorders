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

function create_select_option(model, name, pk) {
    const select = document.getElementById('id_' + model);
    // <option value="pk">選択肢名</option> をつくる
    const option = document.createElement('option');
    option.setAttribute('value', pk);
    option.innerHTML = name;

    // カテゴリの先頭に追加し、選択済みにする
    select.add(option, 0);
    select.options[0].selected = true;
}

function update_select_option(model, name, pk) {
    const select = document.getElementById('id_' + model);
    const selected_index = select.selectedIndex;
    const option = select[selected_index];
    option.innerHTML = name;
}

function delete_select_option(model, name, pk) {
    const select = document.getElementById('id_' + model);
    const selected_index = select.selectedIndex;
    const option = select[selected_index];
}