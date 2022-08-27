const elements_select = document.getElementsByTagName("select");
const elements_update_btn = document.getElementsByClassName("update_btn");

const change_url = (select, update_btn) => {
    const pk = select[select.selectedIndex].value;
    const url = update_btn.getAttribute("href");
    const new_url = url.replace(/.$/, pk);
    update_btn.setAttribute("href", new_url);
};

for (let i = 0; i < elements_select.length; i++) {
    const select = elements_select[i];
    const update_btn = elements_update_btn[i];
    select.addEventListener("change", () => {
        change_url(select, update_btn);
    });
}