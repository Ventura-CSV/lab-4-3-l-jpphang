def main():
    total = 0

    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a value:'))
        
    total = 0
    
    for number in numbers:
        total += number
        


    # total = sum(numbers)
    print(total)

    return total, numbers


if __name__ == '__main__':
    main()
