// remove footer contents
let list_items = document.getElementsByTagName('footer');
for (let i = 0; i < list_items.length; i++) {
    list_items[i].setAttribute("style", "display: none");
}

// remove side bar contents
list_items = document.getElementsByTagName('aside');
for (let i = 0; i < list_items.length; i++) {
    list_items[i].setAttribute("style", "display: none");
}

// set manin contents into the center
list_items = document.getElementsByTagName('section')
for (let i = 0; i < list_items.length; i++) {
    list_items[i].setAttribute("style", "padding-left: 0");
}
