from utils import test, load_intcode

program = load_intcode("day2/input.txt")


def run(program):
    """
    Runs an intcode program
    """
    for i in range(0, len(program), 4):
        op_code = program[i]
        if op_code == 99:
            return program
        src1_pos = program[i+1]
        src2_pos = program[i+2]
        dst_pos = program[i+3]
        if op_code == 1:
            program[dst_pos] = program[src1_pos] + program[src2_pos]
        elif op_code == 2:
            program[dst_pos] = program[src1_pos] * program[src2_pos]
        else:
            raise Exception("shouldn't happen")


def test_part_1():
    test(run, [[1,0,0,0,99], [2,3,0,3,99], [2,4,4,5,99,0], [1,1,1,4,99,5,6,0,99]], [[2,0,0,0,99], [2,3,0,6,99], [2,4,4,5,99,9801], [30,1,1,4,2,5,6,0,99]])


def solve_part_1(program):
    program[1] = 12
    program[2] = 2
    result = run(program)
    print(result[0])


def solve_part_2(initial_program):
    for noun in range(100):
        for verb in range(100):
            new_program = initial_program[:]
            new_program[1] = noun
            new_program[2] = verb
            result = run(new_program)
            if result[0] == 19690720:
                print(100 * noun + verb)


test_part_1()
# solve_part_1(program)
solve_part_2(program)