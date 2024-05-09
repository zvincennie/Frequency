#Zachary Vincennie U80303351


def find_frequency(numbers):
    frequency = {}  # Dictionary to store frequency of each number
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    result = []  # List to store tuples (number, frequency)
    for num, freq in frequency.items():
        result.append((num, freq))

    return result

def main():
    # Read input from the file named "frequency_nums.txt"
    with open("frequency_nums1.txt", "r") as file:
        input_data = file.read().split()

    numbers = [int(num) for num in input_data]  # Convert input to a list of integers
    frequency_list = find_frequency(numbers)

    print("The frequency of the numbers:", end=" ") #Print out and return the output
    for num, freq in frequency_list:
        print(f"({num},{freq})", end=" ")

if __name__ == "__main__":
    main()

