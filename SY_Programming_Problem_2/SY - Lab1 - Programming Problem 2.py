def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines]

        while True:
            print(f"\nThe file has {len(lines)} lines.")
            try:
                choice = int(input("Enter a line number (0 to quit): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 0:
                print("Exiting program. Goodbye!")
                break
            elif 1 <= choice <= len(lines):
                print(f"Line {choice}: {lines[choice - 1]}")
            else:
                print(f"Invalid choice. Enter a number between 1 and {len(lines)}.")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
