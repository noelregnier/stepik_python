#task description https://stepik.org/lesson/24463/step/7?unit=6771
import re

tree = {}
checked = set()

def add(line: str):
    line = re.split(r"\s*[:,\s]\s*", line)
    k = line.pop(0)
    v = set(line)
    tree[k] = v

def deep_check(item):
    global values
    new_values = set()
    if values.intersection(checked):
        print(item)
        return
    for v in values:
        if v in tree and tree[v] != set():
            new_values.update(tree[v])
    if not new_values:
        checked.add(item)
        return
    values = new_values
    deep_check(item)

a = int(input())
for i in range(a):
    add(input())

b = int(input())
for i in range(b):
    item = input()
    values = tree[item]
    deep_check(item)






