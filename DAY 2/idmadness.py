from pathlib import Path

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

data = Path("input.txt").read_text()
numbers = expand_tokens(data)

def find_invalid_numbers(nums):
    invalids = []
    for num in nums:
        str_num = str(num)
        if str_num[0] == '0' or any(str_num.count(digit) > 1 for digit in set(str_num)):
            invalids.append(num)
    return invalids

invalid_numbers = find_invalid_numbers(numbers)
print(f"Invalid numbers count: {len(invalid_numbers)}")