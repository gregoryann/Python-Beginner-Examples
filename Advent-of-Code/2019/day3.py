from collections import defaultdict

from days import AOCDay, day

DEBUG = False

@day(3)
class Day3(AOCDay):
    grid = None

    def manhattan(self, pos):
        return abs(pos[0]) + abs(pos[1])  # Goal is 0, 0

    def steps(self, pos):
        lines = self.grid[pos[0]][pos[1]]
        steps = 0
        lines_added = []
        for line in lines:
            if line[0] not in lines_added:
                steps += line[1]
                lines_added.append(line[0])
        return steps

    def printgrid(self):
        minx, maxx, miny, maxy = 0, 0, 0, 0
        for x, ys in self.grid.items():
            for y, wires in ys.items():
                if x < minx:
                    minx = x
                if x > maxx:
                    maxx = x
                if y < miny:
                    miny = y
                if y > maxy:
                    maxy = y

        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                print(sum([x[0] for x in self.grid[x][y]]) or ".", end="")
            print("")

    def common(self, input_data):
        self.grid = defaultdict(lambda: defaultdict(list))
        # input_data = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
        # input_data = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
        # input_data = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
        wire_id = 0
        for path in input_data:
            wire_id += 1
            position = [0, 0]
            steps = 0
            for entry in path.split(","):
                for i in range(int(entry[1:])):
                    steps += 1
                    if entry[0] == "U":
                        position[1] -= 1
                    elif entry[0] == "D":
                        position[1] += 1
                    elif entry[0] == "L":
                        position[0] -= 1
                    elif entry[0] == "R":
                        position[0] += 1
                    self.grid[position[0]][position[1]].append([wire_id, steps])
        if DEBUG:
            self.printgrid()

    def part1(self, input_data):
        overlaps = []
        for x, ys in self.grid.items():
            for y, wires in ys.items():
                if len(set([x[0] for x in wires])) > 1:
                    overlaps.append([x, y])
        smallest_mhd = None
        for pos in overlaps:
            mhd = self.manhattan(pos)
            if smallest_mhd is None or smallest_mhd > mhd:
                smallest_mhd = mhd
        yield smallest_mhd


    def part2(self, input_data):
        overlaps = []
        for x, ys in self.grid.items():
            for y, wires in ys.items():
                if len(set([x[0] for x in wires])) > 1:
                    overlaps.append([x, y])
        smallest_steps = None
        for pos in overlaps:
            steps = self.steps(pos)
            if smallest_steps is None or smallest_steps > steps:
                smallest_steps = steps
        yield smallest_steps