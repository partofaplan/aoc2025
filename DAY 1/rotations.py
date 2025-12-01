from pathlib import Path

DIAL_SIZE = 100
START = 50 

def load_instructions(path):
    return [line.strip().upper() for line in Path(path).read_text().splitlines() if line.strip()]

def process_instructions(steps):
    total = START
    outputs = [total]
    for step in steps:
        direction, value = step[0], int(step[1:])
        total = total + value if direction == "R" else total - value
        total %= DIAL_SIZE 
        outputs.append(total)
    return outputs

def zero_count(outputs):
    return outputs.count(0)

if __name__ == "__main__":
    instructions = load_instructions("input.txt")
    print(zero_count(process_instructions(instructions)))