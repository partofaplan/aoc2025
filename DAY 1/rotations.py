from pathlib import Path

DIAL_SIZE = 100
START = 50 

def load_instructions(path):
    return [line.strip().upper() for line in Path(path).read_text().splitlines() if line.strip()]

def process_instructions(steps):
    total = START
    outputs = [total]
    crossings = 0
    for step in steps:
        direction, value = step[0], int(step[1:])
        delta = value if direction == "R" else -value
        if delta > 0:
            crossings += (total + delta - 1) // DIAL_SIZE
        elif delta < 0:
            distance = -delta
            crossings += ((total - 1) // DIAL_SIZE) - ((total - distance) // DIAL_SIZE)
        total = (total + delta) % DIAL_SIZE
        outputs.append(total)
    return outputs, crossings

def zero_count(outputs):
    return outputs.count(0)

if __name__ == "__main__":
    instructions = load_instructions("input.txt")
    outputs, crossings = process_instructions(instructions)
    print("zero_count:", zero_count(outputs))
    print("crossings:", crossings)
    print("total_zero_hits:", zero_count(outputs) + crossings)
