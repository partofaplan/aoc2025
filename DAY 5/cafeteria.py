with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        line = line.strip()
        if '-' in line:
            parts = line.split('-')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                result = int(parts[1]) - int(parts[0])
                print(result)
                total += result
    print("Total:", total)



                

