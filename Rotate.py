"""
rotate.py
----------
A simple Python CLI tool to rotate a list of numbers left or right.

Usage:
    python rotate.py
    # Interactive mode

Examples:
    Input list: 1 2 3 4 5
    Rotate by: 2
    Direction (L/R): R
    Output: [4, 5, 1, 2, 3]

Author: <Your Name>
Hacktoberfest 2025 Contribution
License: MIT
"""

def rotate_list(nums, k, direction='L'):
    """Rotate a list `nums` by `k` steps.
    direction = 'L' for left, 'R' for right."""
    if not nums:
        return []
    k = k % len(nums)
    if direction.upper() == 'L':
        return nums[k:] + nums[:k]
    elif direction.upper() == 'R':
        return nums[-k:] + nums[:-k]
    else:
        raise ValueError("Direction must be 'L' or 'R'.")

def main():
    print("=== Hacktoberfest 2025 Rotate Tool ===")
    try:
        nums = input("Enter numbers separated by spaces: ").strip().split()
