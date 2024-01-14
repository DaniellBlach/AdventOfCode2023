from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 1"],
    responses={404: {"description": "Not found"}},
)
file = open(fp.file_path + 'day_01.txt', "r")
calibrations = file.read().split("\n")


@router.get("/day1/part1")
async def return_part_one_output():
    return [
        {"result": solve_part_one()}
    ]


@router.get("/day1/part2")
async def return_part_one_output():
    return [
        {"result": solve_part_two()}
    ]


def solve_part_one() -> int:
    result = 0
    for line in calibrations:
        string = ''.join(char for char in line if char.isdigit())
        result += int(string[0] + '' + string[-1])
    return result


def solve_part_two() -> int:
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    result = 0

    for line in calibrations:
        nums = []
        for char in range(len(line)):
            if (line[char].isdigit()):
                nums.append(line[char])
            else:
                for number in numbers:
                    if line[char:char + len(number)] == number:
                        nums.append(numbers[number])
        result += int(str(nums[0]) + '' + str(nums[-1]))
    return result

