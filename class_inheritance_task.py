# task description https://stepik.org/lesson/24462/step/7?unit=6768

tree = {}
def add(line: str):
    pieces = line.split(":")
    try:
        parents = pieces[1].strip().split(" ")
        tree[pieces[0].strip()] = set(i for i in parents)
    except:
        tree[pieces[0].strip()] = None

deep_found = False

def deep_get(one, two):
    global deep_found
    if one == two:
        deep_found = True
        return
    if not tree[two]:
        return
    if one in tree[two]:
        deep_found = True
        return
    for element in tree[two]:
        deep_get(one, element)


n = int(input())
for i in range(n):
    line = input()
    add(line)

# print()
# print(tree)

q = int(input())
for i in range(q):
    deep_found = False
    one, two = input().split(" ")
    if one and two in tree:
        deep_get(one, two)
    print("Yes") if deep_found else print("No")
