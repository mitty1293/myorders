const elements_select = document.getElementsByTagName("select");
const elements_update_btn = document.getElementsByClassName("update_btn");
const elements_delete_btn = document.getElementsByClassName("delete_btn");

const change_url = (select, link_element) => {
    const pk = select[select.selectedIndex].value;
    const url = link_element.getAttribute("href");
    const new_url = url.replace(/.$/, pk);
    link_element.setAttribute("href", new_url);
};

for (let i = 0; i < elements_select.length; i++) {
    const select = elements_select[i];
    const update_btn = elements_update_btn[i];
    const delete_btn = elements_delete_btn[i];
    select.addEventListener("change", () => {
        change_url(select, update_btn);
        change_url(select, delete_btn);
    });
}