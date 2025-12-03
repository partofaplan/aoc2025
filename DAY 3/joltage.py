total = 0
with open("input.txt") as file:
    for line in file:
        digits = [int(ch) for ch in line.strip()]
        best = -1
        max_right = -1
        # scan from right to left to know the best trailing digit
        for d in reversed(digits):
            if max_right != -1:
                best = max(best, 10 * d + max_right)
            max_right = max(max_right, d)
        print("Result number:", best)
        total += best
print("Total:", total)



