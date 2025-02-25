import random
from datetime import datetime as dt, timedelta
import matplotlib.pyplot as plt
from typing import List, Tuple


class DataReducer:
    def __init__(self, values: List[int], dates: List[str], length: int):
        self.values = values
        self.dates = dates
        self.length = length

    @staticmethod
    def avg_dates(date1: str, date2: str) -> str:
        """Calculate the average date between two dates."""
        d1 = dt.strptime(date1, '%Y-%m-%d')
        d2 = dt.strptime(date2, '%Y-%m-%d')
        avg_date = (d1.timestamp() + d2.timestamp()) / 2
        return dt.fromtimestamp(int(avg_date)).strftime('%Y-%m-%d')

    def reduce_list(self) -> Tuple[List[int], List[str]]:
        """Recursively reduce the list by averaging adjacent values and dates until the desired length is reached."""
        values, dates = self.values, self.dates
        while len(values) > self.length:
            values, dates = [
                (values[i] + values[i + 1]) // 2 for i in range(0, len(values) - 1, 2)
            ], [
                self.avg_dates(dates[i], dates[i + 1]) for i in range(0, len(dates) - 1, 2)
            ]
        return values, dates

    def draw_line(self, new_values: List[int], new_labels: List[str]) -> None:
        """Plot the original and reduced data lists."""
        plt.figure(figsize=(10, 8))

        plt.subplot(2, 1, 1)
        plt.plot(self.dates, self.values, 'r', label='Original')
        plt.title('Original List')
        plt.xticks(rotation=45)
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(new_labels, new_values, 'b', label='Reduced')
        plt.title('Reduced List')
        plt.xticks(rotation=45)
        plt.legend()

        plt.tight_layout()
        plt.show()


def test_fun():
    """Generate random values and test the reduction function with visualization."""
    values = [random.randint(1, 100) for _ in range(100)]
    dates = [(dt.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(100)]
    length = 25 # Desired length of the reduced list

    reducer = DataReducer(values, dates, length)
    new_values, new_dates = reducer.reduce_list()

    assert len(new_values) <= length, "Reduced list exceeds the desired length"

    print(f"Original list ({len(values)} items): {values}\n{dates}")
    print(f"Reduced list ({len(new_values)} items): {new_values}\n{new_dates}")

    reducer.draw_line(new_values, new_dates)


test_fun()
