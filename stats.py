from collections import Counter

def mean(numbers):
    """Calculate the mean (average) of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return 0
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [key for key, value in count.items() if value == max_count]
    return modes[0] if len(modes) == 1 else modes

def main():
    """Test the mean, median, and mode functions with a sample list."""
    test_numbers = [4, 1, 2, 2, 3, 5, 7, 7, 7]
    print("Test List:", test_numbers)
    print("Mean:", mean(test_numbers))
    print("Median:", median(test_numbers))
    print("Mode:", mode(test_numbers))

if __name__ == "__main__":
    main()
