import math

from days import AOCDay, day


@day(1)
class Day1(AOCDay):
    def common(self, input_data):
        pass

    def part1(self, input_data):
        sum = 0
        for line in input_data:
            sum += math.floor(int(line) / 3) - 2
        yield sum


    def part2(self, input_data):
        sum = 0
        for line in input_data:
            add = math.floor(int(line) / 3) - 2
            extra = add
            sum += add
            extra_total = 0
            while extra is None or extra > 0:
                extra = max(math.floor(extra / 3) - 2, 0)
                extra_total += extra
            sum += extra_total
        yield sum