from fastapi import APIRouter

from inputFiles import file_path as fp

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 6"],
    responses={404: {"description": "Not found"}},
)
file = open(fp.file_path + 'day_06.txt', "r")
data = file.read().splitlines()


@router.get("/day6/part1")
async def return_part_one_output():
    return [
        {"result": solve_part_one()}
    ]


@router.get("/day6/part2")
async def return_part_two_output():
    return [
        {"result": solve_part_two()}
    ]


def solve_part_one() -> int:
    result = 1
    times = list(map(int, data[0].split()[1:]))
    distances = list(map(int, data[1].split()[1:]))
    for index, time in enumerate(times):
        possibilities = 0
        for second in range(1, time):
            if second * (time - second) > distances[index]:
                possibilities += 1
        result *= possibilities
    return result


def solve_part_two() -> int:
    result = 0
    times = int("".join(data[0].split()[1:]))
    distances = int("".join(data[1].split()[1:]))
    for second in range(1, times):
        if second * (times - second) > distances:
            result += 1
    return result
