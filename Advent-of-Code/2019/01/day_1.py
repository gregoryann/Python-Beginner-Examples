#!/usr/bin/python3
# Advent of Code 2019
# Day 1

fuel_count = lambda x: x // 3 - 2
mass = [int(element) for element in open("input").read().splitlines()]


def calculate_fuel_recursion(atomic_mass: int):
    return atomic_mass + calculate_fuel_recursion(fuel_count(atomic_mass)) if atomic_mass > 0 else 0


if __name__ == "__main__":
    print(f"""
    Module fuel requirement: {sum((fuel_count(element) for element in mass))}
    Full fuel requirement: {sum((calculate_fuel_recursion(fuel_count(element)) for element in mass))}
    """)