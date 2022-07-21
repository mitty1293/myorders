const select_elements = document.getElementsByTagName("select");
const class_update_elements = document.getElementsByClassName("class_update");

const change_url = (select_elem, class_update_elem) => {
    const pk = select_elem[select_elem.selectedIndex].value;
    const url = class_update_elem.getAttribute("href");
    const new_url = url.replace(/.$/, pk);
    class_update_elem.setAttribute("href", new_url);
};

for (let i = 0; i < select_elements.length; i++) {
    const select_elem = select_elements[i];
    const class_update_elem = class_update_elements[i];
    select_elem.addEventListener("change", () => {
        change_url(select_elem, class_update_elem);
    });
}