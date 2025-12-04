with open('input.txt', 'r') as file:
    lines = file.readlines()

total_sum = 0
for line in lines:
    line = line.strip()
    digits = [ch for ch in line if ch.isdigit()]
    
    n = len(digits)
    k = 12
    stack = []
    to_remove = n - k
    
    for digit in digits:
        while to_remove and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    result = ''.join(stack[:k])
    total_sum += int(result) 
print("Total Sum:", total_sum)



