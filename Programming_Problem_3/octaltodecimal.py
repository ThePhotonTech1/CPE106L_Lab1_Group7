def octal_to_decimal():
    octal_str = input("Enter an octal number: ")
    
    decimal = 0
    power = 0
    
    # Process digits from right to left
    for i in range(len(octal_str) - 1, -1, -1):
        digit = int(octal_str[i])
        if digit > 7:
            print("Invalid octal digit")
            return
        decimal += digit * (8 ** power)
        power += 1
    
    print(f"Decimal equivalent: {decimal}")

if __name__ == "__main__":
    octal_to_decimal()
