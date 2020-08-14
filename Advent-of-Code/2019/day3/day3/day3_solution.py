import math
from utils import test, file_into_list

wire1, wire2 = file_into_list("day3/input.txt", lambda x: x.split(","))


def manhattan_distance_from_origin(coords):
    """
    Gives the manhattan distance to origin
    """
    return abs(coords[0]) + abs(coords[1])


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def intersection_with_sums(lst1, lst2):
    """
    Finds the intersections between two lists along with the sum of indexes
    Very slow version
    """
    common_points = []
    for i, coord in enumerate(lst1):
        try:
            j = lst2.index(coord)
            if j > 0:
                common_points.append((coord, i+j))
        except ValueError:
            pass
    return common_points


def intersection_with_sums_fast(lst1, lst2):
    """
    Finds the intersections between two lists along with the sum of indexes
    """
    common = intersection(lst1, lst2)
    common_with_sums = []
    for coord in common:
        try:
            sum1 = lst1.index(coord)
            sum2 = lst2.index(coord)
            common_with_sums.append((coord, sum1+sum2))
        except ValueError:
            pass

    return common_with_sums


def add_coords(path, direction, count):
    for i in range(count):
        last_coord = path[-1]
        if direction == 'R':            
            path.append((last_coord[0] + 1, last_coord[1]))
        elif direction == 'L':
            path.append((last_coord[0] - 1, last_coord[1]))
        elif direction == 'U':
            path.append((last_coord[0], last_coord[1] + 1))
        elif direction == 'D':
            path.append((last_coord[0], last_coord[1] - 1))
    return path


def parse_step(step):
    direction = step[0]
    count = int(step[1:])
    return direction, count


def get_path(wire):
    path = [(0, 0)]
    for step in wire:
        direction, count = parse_step(step)
        path = add_coords(path, direction, count)
    return path


def part_1(wires):
    wire1, wire2 = wires
    path1 = get_path(wire1)
    path2 = get_path(wire2)
    cross_points = intersection(path1, path2)
    # map from points to their manhattan distance to origin and then filter those that are 0 (correspond with origin)
    return min(filter(lambda a: a != 0, map(lambda x: manhattan_distance_from_origin(x), cross_points)))


def test_part_1():
    test(part_1, [(['R8','U5','L5','D3'], ['U7','R6','D4','L4']),(['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']), (['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'])], [6, 159, 135])


test_part_1()
print(part_1((wire1, wire2)))


def part_2(wires):
    wire1, wire2 = wires
    path1 = get_path(wire1)
    path2 = get_path(wire2)
    cross_points_with_sums = intersection_with_sums_fast(path1, path2)
    return min(filter(lambda x: x != 0, map(lambda x: x[1], cross_points_with_sums)))


def test_part_2():
    test(part_2, [(['R8','U5','L5','D3'], ['U7','R6','D4','L4']),(['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']), (['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'])], [30, 610, 410])


test_part_2()
print(part_2((wire1, wire2)))