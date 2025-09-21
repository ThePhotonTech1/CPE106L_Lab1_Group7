from collections import Counter

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2

def mode(numbers):
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [val for val, cnt in counts.items() if cnt == max_count]
    return min(modes)

if __name__ == "__main__":
    raw = input("Enter numbers separated by spaces: ")
    numbers = [float(x) for x in raw.split()]

    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

