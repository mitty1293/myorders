function add_category(name, pk) {
    var select = document.getElementById('id_category');
    // <option value="pk">選択肢名</option> をつくる
    var option = document.createElement('option');
    option.setAttribute('value', pk);
    option.innerHTML = name;

    // カテゴリの先頭に追加し、選択済みにする
    select.add(option, 0);
    select.options[0].selected = true;
}

function add_unit(name, pk) {
    var select = document.getElementById('id_unit');
    // <option value="pk">選択肢名</option> をつくる
    var option = document.createElement('option');
    option.setAttribute('value', pk);
    option.innerHTML = name;

    // カテゴリの先頭に追加し、選択済みにする
    select.add(option, 0);
    select.options[0].selected = true;
}