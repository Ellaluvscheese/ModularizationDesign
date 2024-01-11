
def main():
    print(f'head: {add(7, 4)}')

    print(f"{addTail(7, 4)}")


def add(value1, value2):
    if value2 == 0:
        # print(value1, value2)
        return value1
    else:
        sum_total = 1 + add(value1, value2 - 1)
        print(f'Head: {sum_total}')
        return sum_total
        # return 1 + add(value1, value2 - 1)

def addTail(value1, value2):
    if value2 == 0:
        # print(value1, value2)
        return value1
    else:
        sum_total = addTail(value1 + 1, value2 - 2)
        print(f'Tail: {sum_total}')
        return sum_total
        # return add(value1 + 1, value2 - 1)

main()