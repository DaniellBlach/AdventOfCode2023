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


def solve_part_one() -> int:
    result = 0
    for line in calibrations:
        string = ''.join(char for char in line if char.isdigit())
        result += int(string[0] + '' + string[-1])
    return result
