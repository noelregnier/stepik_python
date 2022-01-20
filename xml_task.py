from xml.etree import ElementTree

inp = '''
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
'''
root = ElementTree.fromstring(inp)
# root = ElementTree.fromstring(input())
red = 0
green = 0
blue = 0

parents = [root]
children = []
n = 1


def take_color(child):
    global red
    global green
    global blue
    if child.attrib['color'] == 'red':
        red += n
    if child.attrib['color'] == 'blue':
        blue += n
    if child.attrib['color'] == 'green':
        green += n


def get_children(parent):
    for child in parent:
        children.append(child)
        take_color(child)


take_color(root)
while parents:
    n += 1
    for i in parents:
        get_children(i)
    parents = children.copy()
    children.clear()

print(red, green, blue)
