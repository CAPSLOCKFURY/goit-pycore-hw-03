import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    validate_input(min, max, quantity)

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

def validate_input(min: int, max: int, quantity: int) -> None:
    if min < 1:
        raise ValueError("Minimal ticket number must be greater than 1")
    elif max > 1000:
        raise ValueError("Maximum ticket number must be less than 1000")
    elif quantity > (max - min + 1):
        raise ValueError("Number of tickets to get is exceeding tickets number range")