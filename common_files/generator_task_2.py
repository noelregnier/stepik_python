#task description https://stepik.org/lesson/24464/step/5?unit=6769
# import itertools

def primes():
    yield 2
    x = 3
    while 1:
        the_number = x
        for i in range(x)[2:]:
            if x % i == 0:
                the_number=0
                break

        if the_number:
            yield the_number
        x+=1


# print(list(itertools.takewhile(lambda x : x <= 150, primes())))



