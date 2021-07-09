

namespaces = {}
structure = {'global': set()}

def create(namespace, parent):
    namespaces[namespace] = parent
    if parent in structure:
        structure.get(parent).add(namespace)
    else:
        structure[parent] = set()

def add(namespace, var):
    if namespace in structure:
        structure.get(namespace).add(var)
    else:
        structure[namespace] = {var}

def get(namespace, var):
    if var in structure[namespace]:
        print(namespace)
        return

    while namespace != 'global':
        namespace = namespaces[namespace]
        if var in structure[namespace]:
            print(namespace)
            return
    print("None")




def try_me():
    n = int(input())
    for i in range(n):
        i = input().split()

        if i[0] == "add":
            add(i[1], i[2])
        elif i[0] == "create":
            create(i[1], i[2])
        else:
        # elif i[0] == "get":
            get(i[1], i[2])


# try_me()
# print(namespaces)
# print(structure)