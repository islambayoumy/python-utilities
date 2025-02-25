# Python Utilities

Some python scripts for solving common problems.

## Getting Started

Every file (script) is for one separate problem.

### Prerequisites

All scripts here were written in Python 3.x.

## Utilities: list_reducer

### Problem Statement

Assume you have a list of website users' visits throughout the year. 
You need to draw a graph representing the number of users' visits per day, 
meaning that you will have around 360 records. 
Displaying these many records on a UI can be overwhelming.

This script reduces the list by averaging each two consecutive numbers and dates.

### How It Works

- **Starting from `test_fun()`**:
    - Generates a random list of 100 integers.
    - Creates a list of 100 dates counting backward from today.
    - Sets the target length of the reduced list to 25 (or any other specified length).
    - Passes these parameters to the `reduce_list()` method and retrieves the reduced data.
    - Asserts that the reduced list length does not exceed the specified length.
    - Uses `draw_line()` to visualize both the original and reduced lists.

- **In `reduce_list()`**:
    - Iteratively reduces the list size by averaging adjacent values and dates until the desired length is reached.
    - Uses `avg_dates()` to calculate the midpoint date between two dates.
    - Returns the reduced values and dates.

- **In `draw_line()`**:
    - Uses `matplotlib` subplots to plot both the original and reduced lists in a single visualization.

### Pros & Cons of This Approach

#### Pros:
- Preserves the overall trend of the data.
- Provides a clearer visualization for human interpretation.
- Reduces the amount of data sent to the frontend, improving performance.
- Smooths out fluctuations and outliers.

#### Cons:
- The reduced numbers are averaged values rather than actual recorded values.

This utility helps make large datasets more manageable while maintaining useful insights.
