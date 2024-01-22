from fastapi import APIRouter

from inputFiles import file_path as fp

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 4"],
    responses={404: {"description": "Not found"}},
)
file = open(fp.file_path + 'day_04.txt', "r")
scratchcards = file.read().split("\n")


@router.get("/day4/part1")
async def return_part_one_output():
    return [
        {"result": solve_part_one()}
    ]


@router.get("/day4/part2")
async def return_part_two_output():
    return [
        {"result": solve_part_two()}
    ]


def solve_part_one() -> int:
    result = 0
    for card in scratchcards:
        score = 0
        winning_numbers, numbers = card.split("|")
        numbers = list(filter(None, numbers.split(" ")))
        winning_numbers = list(filter(None, winning_numbers.split(":")[1].split(" ")))
        for number in numbers:
            if number in winning_numbers:
                score += 1
        if score > 0:
            result += 2 ** (score - 1)
    return result


def solve_part_two() -> int:
    result = [1] * len(scratchcards)
    for x, card in enumerate(scratchcards):
        score = 0
        winning_numbers, numbers = card.split("|")
        numbers = list(filter(None, numbers.split(" ")))
        winning_numbers = list(filter(None, winning_numbers.split(":")[1].split(" ")))
        for number in numbers:
            if number in winning_numbers:
                score += 1
        if score > 0:
            for i in range(score):
                result[x + 1 + i] += result[x]
    return sum(result)
