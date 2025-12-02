from pathlib import Path
import re

def expand_tokens(text):
    nums = []
    for token in text.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            lo, hi = map(int, token.split("-", 1))
            nums.extend(range(lo, hi + 1))
        else:
            nums.append(int(token))
    return nums

pattern = re.compile(r"(\d{1,3})\1")
def find_repeating_numbers(numbers):
    return [num for num in numbers if pattern.fullmatch(str(num))]

input_file = Path(__file__).parent / "input.txt"

with input_file.open() as f:
    content = f.read()
    numbers = expand_tokens(content)
    repeating_numbers = find_repeating_numbers(numbers)
    print("Repeating Numbers:", repeating_numbers)
    print("Sum:", sum(repeating_numbers))


