def main():
    total = 0

    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a value:'))
        
    total = 0
    
    for numbers in numbers:
        total = total + numbers
        


    # total = sum(numbers)
    print(total)

    return total, numbers


if __name__ == '__main__':
    main()
