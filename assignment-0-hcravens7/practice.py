# Paste your pytest output summary line below after running `pytest`
# pytest output: ================================ 4 passed in 0.01s ===============================
# Your code has been rated at 10.00/10 (previous run: 9.50/10, +0.50)

from __future__ import annotations


def greet(name):
    """inputs name and returns greeting"""
    return "Hello, " + name + "!"

def mean(nums):
    """Return the arithmetic mean of nums."""
    acc = 0
    for num in nums:
        acc = acc + num
    return acc/len(nums)

def normalize(nums):
    """Return a new list scaled so it sums to 1.0."""
    total = sum(nums)
    result = []
    for num in nums:
        normalized = num/total
        result.append(normalized)
    return result

def main() -> None:
    """Entry point for running this file directly."""
    print(greet("Gradescope"))
    print(mean([2, 4, 6]))

if __name__ == "__main__":
    main()
