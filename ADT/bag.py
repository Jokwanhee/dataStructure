def insert(bag, e):
    bag.append(e)


def remove(bag, e):
    if (e in bag):
        bag.remove(e)


def contains(bag, e):
    return e in bag


def count(bag):
    return len(bag)


def main():
    bags = []
    insert(bags, 1)
    insert(bags, 2)
    insert(bags, 3)
    insert(bags, 2)
    insert(bags, 3)
    print("가방 속 숫자 : ", bags)

    remove(bags, 3)
    print("가방 속 숫자 : ", bags)

    print("가방 속 숫자 총 개수 : ", count(bags))

    print("가방 속 숫자 1 여부 : ", contains(bags,1))

if __name__ == "__main__":
    main()
