from utils import test

range_start = 130254
range_end = 678275


def is_monotonically_increasing(L):
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            return False
    return True


def has_pair(L):
    for i in range(1, len(L)):
        if L[i] == L[i - 1]:
            return True
    return False


def is_password(number):
    digits = [int(d) for d in str(number)]
    return is_monotonically_increasing(digits)\
        and has_pair(digits)


def part_1(start, end):
    return len(list(filter(is_password, range(start, end))))


def test_part_1():
    test(is_password,
         [122345, 111123, 135679, 111111, 223450, 123789],
         [True, True, False, True, False, False])


test_part_1()
print(part_1(range_start, range_end))


def has_pair_not_more(L):
    for i in range(1, len(L)):
        result = 0 # accumulates the decision
        if L[i] == L[i - 1]:
            # we have a pair
            if i - 2 >= 0 and L[i - 2] != L[i]:
                # check the previous element before pair
                result += 1
            if i + 1 < len(L) and L[i + 1] != L[i]:
                # check the next element after pair
                result += 1
            if i - 2 < 0:
                # it's at the beginning
                result += 1
            if i + 1 >= len(L):
                # it's at the end
                result += 1
            if result == 2:
                return True
    return False


def is_password_2(number):
    digits = [int(d) for d in str(number)]
    return is_monotonically_increasing(digits) \
        and has_pair_not_more(digits)


def test_part_2():
    test(is_password_2,
         [112233, 123444, 111122],
         [True, False, True])


def part_2(start, end):
    return len(list(filter(is_password_2, range(start, end))))


test_part_2()
print(part_2(range_start, range_end))