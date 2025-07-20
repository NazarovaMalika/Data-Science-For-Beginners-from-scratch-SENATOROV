"""My Data Science Homework Module.

This module contains my homework submission with proper documentation.
"""

from typing import List


def main() -> None:
    """Execute the main homework function.
    
    This function demonstrates basic data analysis operations.
    """
    print("Hello, this is my homework!")
    
    # Sample data analysis
    data: List[int] = [1, 2, 3, 4, 5]
    print(f"Data: {data}")
    print(f"Sum: {sum(data)}")
    print(f"Average: {sum(data) / len(data)}")


if __name__ == "__main__":
    main()
