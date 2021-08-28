let list_items = document.getElementsByTagName('footer');
console.log(list_items[0]);
for (let i = 0; i < list_items.length; i++) {
    console.log(list_items[i])
    list_items[i].setAttribute("style", "display: none");
}

