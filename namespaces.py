# task description https://stepik.org/lesson/24460/step/10?unit=6766

namespaces = {}
structure = {'global': set()}


def create(namespace, parent):
    namespaces[namespace] = parent
    structure[namespace] = set()


def add(namespace, var):
    structure.get(namespace).add(var)


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
            get(i[1], i[2])


try_me()
# print("namespaces:    ", namespaces)
# print("structure:    ", structure)