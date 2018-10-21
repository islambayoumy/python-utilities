# Python Utilities

Some python scripts for solving common problems.

## Getting Started

Every file (script) is for one separate problem.

### Prerequisites

All scripts here were written in python 3.x

## Utilities: list_reducer

##### Problem statement:

Assume you have a list of a website users' visits among a year.
And you need to draw a graph that represents the number of users' visits per day, this means that you will draw a graph with ~= 360 record, which is unrepresentable from UI point of view.
So this script is reducing the list by calculating the average of each two consecutive numbers & dates.

##### How it works:

- Starting from **test_fun()**:
    - Generate random list of 20 integers and sort them
    - Set list of 20 dates
    - Set length of the reduced list to n where n < 20
    - Pass the above parameters to **reduce_list()** method and get the return
    - Assert the reduced list length to be <= length
    - Use **draw_line()** method to draw the old & reduced lists

- At **reduce_list()**:
    - Set condition (length of values' list <= passed length) to break the recursion
    - Get te average of each two consecutive numbers
    - Use **avg_dates()** to get the avg between two dates
    - Return values & dates lists

- At **draw_line()**:
    Uses *matplotlib* subplots to plot the old list & the reduced one in the same screen

##### Pros & cons for using this solution:

###### Pros:
- Give almost the same graph
- More clear for human eyes
- Reducing data fetched at the frontend resulting in better performance
- Removing outliers
###### Cons:
- Numbers are average, not actual
