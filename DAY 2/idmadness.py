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

# Part 1 solution
# def find_repeating_numbers(numbers):
#     def is_repeat(n: int) -> bool:
#         s = str(n)
#         if len(s) % 2:
#             return False
#         half = len(s) // 2
#         return s[:half] == s[half:]
#     return [n for n in numbers if is_repeat(n)]

def find_repeating_numbers(numbers):
    def is_repeat(n: int) -> bool:
        s = str(n)
        return bool(re.fullmatch(r'(.+)\1+', s))
    return [n for n in numbers if is_repeat(n)]
    
input_file = Path(__file__).parent / "input.txt"

with input_file.open() as f:
    content = f.read()
    numbers = expand_tokens(content)
    repeating_numbers = find_repeating_numbers(numbers)
    print("Repeating Numbers:", repeating_numbers)
    print("Sum:", sum(repeating_numbers))


