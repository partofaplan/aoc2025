from pathlib import Path

def main():
    input_path = Path(__file__).with_name("input.txt")
    ranges = []
    numbers = []

    with open(input_path, "r") as file:
        for line in file:
            line = line.strip()
            if '-' in line:
                start, end = map(int, line.split('-'))
                ranges.append((start, end))
            elif line.isdigit():
                numbers.append(int(line))

    count = 0
    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                count += 1
                break
    print(count)
if __name__ == "__main__":
    main()

     


