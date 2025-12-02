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
        if str_num[0] == '0':
            invalids.append(num)
            continue
        length = len(str_num)
        for sub_len in range(1, length // 2 + 1):
            if length % sub_len == 0:
                substring = str_num[:sub_len]
                if substring * (length // sub_len) == str_num:
                    invalids.append(num)
                    break
    return invalids

invalid_numbers = find_invalid_numbers(numbers)
print(f"Found {len(invalid_numbers)} invalid numbers.")