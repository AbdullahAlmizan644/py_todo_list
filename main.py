from js import console

my_input=Element("myInput")
btn=Element("Btn")
list_group=Element("myUL")


def newElement(*args):
    text=my_input.element.value
    item=create("li", classes="list-group-item")
    item.element.innerText=text
    list_group.element.appendChild(item.element)


btn.element.onclick=newElement

