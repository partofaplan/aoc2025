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

data = Path("test_input.txt").read_text()
numbers = expand_tokens(data)
print(",".join(map(str, numbers)))