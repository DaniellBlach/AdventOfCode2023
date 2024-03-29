from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 2"],
    responses={404: {"description": "Not found"}},
)
file = open(fp.file_path + 'day_02.txt', "r")
game_records = file.read().split("\n")


@router.get("/day2/part1")
async def return_part_one_output():
    return [
        {"result": solve_part_one()}
    ]


@router.get("/day2/part2")
async def return_part_two_output():
    return [
        {"result": solve_part_two()}
    ]


def solve_part_one() -> int:
    rules = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for count, game in enumerate(game_records):
        results = game.split(":")
        sets = results[1].replace('; ', ', ').split(",")
        valid_value = True
        for cubes in sets:
            cubes = cubes[1:].split(" ")
            if rules[cubes[1]] < int(cubes[0]):
                valid_value = False
        if valid_value:
            result += count + 1
    return result


def solve_part_two() -> int:
    result = 0
    for count, game in enumerate(game_records):
        results = game.split(":")
        sets = results[1].replace('; ', ', ').split(",")
        red = []
        green = []
        blue = []
        for cubes in sets:
            cubes = cubes[1:].split(" ")
            if cubes[1] == "red":
                red.append(int(cubes[0]))
            elif cubes[1] == "green":
                green.append(int(cubes[0]))
            elif cubes[1] == "blue":
                blue.append(int(cubes[0]))
        result += (max(red) * max(green) * max(blue))
    return result
