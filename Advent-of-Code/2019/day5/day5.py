from utils import test, load_intcode, IntcodeComputer

program = load_intcode("day5/input.txt")
test_program = [1, 6, 0, 0 , 4, 0, 99]

test_program1 = ([3,9,8,9,10,9,4,9,99,-1,8], 8)
test_program2 = ([3,9,7,9,10,9,4,9,99,-1,8], 8)
test_program3 = ([3,3,1108,-1,8,3,4,3,99], 8)
test_program4 = ([3,3,1107,-1,8,3,4,3,99], 8)
test_jmp_program = ([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 8)
test_jmp_program2 = ([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 8)

test_programs = [test_program1, test_program2, test_program3, test_program4, test_jmp_program, test_jmp_program2]


def run_test_program(program, inp):
    computer = IntcodeComputer(program)
    return computer.run(inp)


test(lambda x: run_test_program(*x), test_programs, [1, 0, 1, 0, 1, 1])

computer = IntcodeComputer(program)
print(computer.run(5))