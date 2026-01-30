from aoc.core import timeit
import re


# @timeit
# def part1(data: str) -> int:
#     values: dict[str, int] = {}
#     # Pattern: Matches 1-2 operands, an optional operator, and the target
#     # Examples: "123 -> x", "NOT x -> y", "x AND y -> z"
#     pattern = re.compile(r"^(?:([a-z0-9]+) )?([A-Z]+)? ?([a-z0-9]+) -> ([a-z]+)$")
#
#     for line in data.strip().split("\n"):
#         line = line.strip()
#         # Using the regex to extract parts
#         match = pattern.search(line)
#
#         if match is not None:
#             op_a, operator, op_b, target = match.groups()
#             if target not in values:
#                 values[target] = 0
#             if op_a is not None:
#                 if op_a not in values and not op_a.isdigit():
#                     values[op_a] = 0
#             if op_b not in values and not op_b.isdigit():
#                 values[op_b] = 0
#
#             if operator:
#                 if operator == "AND":
#                     if op_a.isdigit() and op_b.isdigit():
#                         values[target] = int(op_a) & int(op_b)
#                     elif op_a.isdigit() and not op_b.isdigit():
#                         values[target] = int(op_a) & values[op_b]
#                     elif not op_a.isdigit() and op_b.isdigit():
#                         values[target] = values[op_a] & int(op_b)
#                     else:
#                         values[target] = values[op_a] & values[op_b]
#
#                 elif operator == "RSHIFT":
#                     if op_a.isdigit() and op_b.isdigit():
#                         values[target] = int(op_a) >> int(op_b)
#                     elif op_a.isdigit() and not op_b.isdigit():
#                         values[target] = int(op_a) >> values[op_b]
#                     elif not op_a.isdigit() and op_b.isdigit():
#                         values[target] = values[op_a] >> int(op_b)
#                     else:
#                         values[target] = values[op_a] >> values[op_b]
#
#                 elif operator == "LSHIFT":
#                     if op_a.isdigit() and op_b.isdigit():
#                         values[target] = int(op_a) << int(op_b)
#                     elif op_a.isdigit() and not op_b.isdigit():
#                         values[target] = int(op_a) << values[op_b]
#                     elif not op_a.isdigit() and op_b.isdigit():
#                         values[target] = values[op_a] << int(op_b)
#                     else:
#                         values[target] = values[op_a] << values[op_b]
#
#                 elif operator == "OR":
#                     if op_a.isdigit() and op_b.isdigit():
#                         values[target] = int(op_a) | int(op_b)
#                     elif op_a.isdigit() and not op_b.isdigit():
#                         values[target] = int(op_a) | values[op_b]
#                     elif not op_a.isdigit() and op_b.isdigit():
#                         values[target] = values[op_a] | int(op_b)
#                     else:
#                         values[target] = values[op_a] | values[op_b]
#
#                 elif operator == "NOT":
#                     if not op_b.isdigit():
#                         values[target] = ~values[op_b] & 0xFFFF
#             else:
#                 if op_b.isdigit():
#                     values[target] = int(op_b)
#                 else:
#                     values[target] = values[op_b]
#
#     print(values["a"])
#     return 1


@timeit
def part1(data: str) -> int:
    instructions = {}
    cache = {}

    pattern = re.compile(r"^(?:([a-z0-9]+) )?([A-Z]+)? ?([a-z0-9]+) -> ([a-z]+)$")

    for line in data.strip().split("\n"):
        match = pattern.search(line.strip())
        if match:
            op_a, operator, op_b, target = match.groups()
            instructions[target] = (op_a, operator, op_b)

    def get_val(x):
        if x.isdigit():
            return int(x)
        return calculate(x)

    def calculate(wire):
        if wire in cache:
            return cache[wire]

        # Get the recipe for this wire
        op_a, operator, op_b = instructions[wire]

        if not operator:  # Simple assignment: 123 -> x or y -> x
            res = get_val(op_b)
        elif operator == "NOT":
            res = ~get_val(op_b) & 0xFFFF
        elif operator == "AND":
            res = get_val(op_a) & get_val(op_b)
        elif operator == "OR":
            res = get_val(op_a) | get_val(op_b)
        elif operator == "LSHIFT":
            res = get_val(op_a) << get_val(op_b)
        elif operator == "RSHIFT":
            res = get_val(op_a) >> get_val(op_b)

        cache[wire] = res & 0xFFFF  # Store result and mask to 16-bit
        return cache[wire]

    # instructions["b"] = (None, None, 16076)
    # Start the chain reaction by asking for wire 'a'
    result = calculate("a")
    return result


@timeit
def part2(data: str) -> int:
    instructions = {}
    # instructions["b"] = (None, None, 16076)
    cache = {}
    pattern = re.compile(r"^(?:([a-z0-9]+) )?([A-Z]+)? ?([a-z0-9]+) -> ([a-z]+)$")

    for line in data.strip().split("\n"):
        match = pattern.search(line.strip())
        if match:
            op_a, operator, op_b, target = match.groups()

            # Solve this by clearing the cache instead
            #
            # def solve(instructions, override_b=None):
            #     cache = {}
            #
            #     # If we are doing Part 2, force b's value into the cache immediately
            #     if override_b is not None:
            #         cache["b"] = override_b
            #
            #     def calculate(wire):
            #         if wire in cache: return cache[wire]
            #
            #         # ... rest of your calculate logic ...
            #
            #         cache[wire] = res & 0xFFFF
            #         return cache[wire]
            #
            #     return calculate("a")
            #
            # --- Execution ---
            # Part 1
            # ans_a = solve(instructions)
            #
            # Part 2
            # We use the same instructions but "prime" the cache with the result from Part 1
            # ans_part2 = solve(instructions, override_b=ans_a)
            if target != "b":
                instructions[target] = (op_a, operator, op_b)
            else:
                instructions["b"] = (None, None, "16076")

    def get_val(x):
        if x.isdigit():
            return int(x)
        return calculate(x)

    def calculate(wire):
        if wire in cache:
            return cache[wire]

        # Get the recipe for this wire
        op_a, operator, op_b = instructions[wire]

        if not operator:  # Simple assignment: 123 -> x or y -> x
            res = get_val(op_b)
        elif operator == "NOT":
            res = ~get_val(op_b) & 0xFFFF
        elif operator == "AND":
            res = get_val(op_a) & get_val(op_b)
        elif operator == "OR":
            res = get_val(op_a) | get_val(op_b)
        elif operator == "LSHIFT":
            res = get_val(op_a) << get_val(op_b)
        elif operator == "RSHIFT":
            res = get_val(op_a) >> get_val(op_b)

        cache[wire] = res & 0xFFFF  # Store result and mask to 16-bit
        return cache[wire]

    # Start the chain reaction by asking for wire 'a'
    result = calculate("a")
    return result
