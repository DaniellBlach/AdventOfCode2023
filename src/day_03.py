from fastapi import APIRouter

from inputFiles import file_path as fp

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 3"],
    responses={404: {"description": "Not found"}},
)


def prepare_data():
    file = open(fp.file_path + 'day_03.txt', "r")
    result = []
    for j in file.read().split("\n"):
        result.append("." + j + ".")
    row = "." * len(result[0])
    result.append(row)
    result.insert(0, row)
    return result


engine_schematic = prepare_data()
rows_count = len(engine_schematic)
chars_count = len(engine_schematic[0])


@router.get("/day3/part1")
async def return_part_one_output():
    return [
        {"result": solve_part_one()}
    ]


def solve_part_one() -> int:
    result = 0

    for i in range(len(engine_schematic)):
        digit = ""
        for j in range(len(engine_schematic[i])):
            if engine_schematic[i][j].isdigit():
                digit += engine_schematic[i][j]
            elif len(digit) > 0 and not engine_schematic[i][j].isdigit():
                adjacent_symbol = find_adjacent_symbol(i, j - len(digit), j - 1)
                if adjacent_symbol:
                    result += int(digit)
                digit = ""
    return result


def find_adjacent_symbol(row: int, begin: int, end: int):
    # RIGHT
    if end + 1 < chars_count and engine_schematic[row][end + 1] != "." and not engine_schematic[row][end + 1].isdigit():
        return True
    # LEFT
    if begin - 1 > 0 and engine_schematic[row][begin - 1] != "." and not engine_schematic[row][begin - 1].isdigit():
        return True
    # TOP
    if row - 1 > 0:
        for j in range(max(0, begin - 1), min(end + 1, chars_count) + 1):
            if engine_schematic[row - 1][j] != "." and not engine_schematic[row - 1][j].isdigit():
                return True
    # BOTTOM
    if row + 1 < rows_count:
        for j in range(max(0, begin - 1), min(end + 1, rows_count) + 1):
            if engine_schematic[row + 1][j] != "." and not engine_schematic[row + 1][j].isdigit():
                return True
    return False
