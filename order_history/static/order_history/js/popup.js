function add_select_option(model, name, pk) {
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