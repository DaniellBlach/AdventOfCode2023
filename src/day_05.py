from fastapi import APIRouter

from inputFiles import file_path as fp

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 5"],
    responses={404: {"description": "Not found"}},
)


def format_data() -> list:
    maps = []
    i = 2
    while i < len(lines):
        maps.append([])
        i += 1
        while i < len(lines) and not lines[i] == "":
            maps[-1].append(list(map(int, lines[i].split())))
            i += 1
        i += 1
    return maps


file = open(fp.file_path + 'day_05.txt', "r")
lines = file.read().split("\n")
seeds = list(map(int, lines[0].split(" ")[1:]))
maps = format_data()


@router.get("/day5/part1")
async def return_part_one_output():
    return [
        {"result": solve_part_one()}
    ]


def solve_part_one() -> int:
    result = []
    for seed in seeds:
        num = seed
        for m in maps:
            for destination_start, source_start, range_length in m:
                if source_start <= num < source_start + range_length:
                    num = destination_start + (num - source_start)
                    break
        result.append(num)
    return min(result)
