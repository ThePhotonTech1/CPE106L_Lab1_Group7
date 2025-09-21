def decimal_to_octal():
    decimal = int(input("Enter a decimal number: "))
    
    if decimal == 0:
        print("Octal equivalent: 0")
        return
    
    original_decimal = decimal
    octal_digits = []
    
    # Convert using repeated division by 8
    while decimal > 0:
        remainder = decimal % 8
        octal_digits.append(str(remainder))
        decimal = decimal // 8
    
    # Reverse to get correct order
    octal_digits.reverse()
    octal_result = ''.join(octal_digits)
    
    print(f"Octal equivalent: {octal_result}")

if __name__ == "__main__":
    decimal_to_octal()
