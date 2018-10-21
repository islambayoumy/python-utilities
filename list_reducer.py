import random
from datetime import datetime as dt
import matplotlib.pyplot as plt

def avg_dates(date1, date2) -> str:
    d1 = dt.strptime(str(date1), '%Y-%m-%d')
    d2 = dt.strptime(str(date2), '%Y-%m-%d')
    avg_date = (d1.timestamp() + d2.timestamp()) / 2

    return dt.fromtimestamp(int(avg_date)).strftime("%Y-%m-%d")

def reduce_list(values, dates, length) -> tuple:
    if len(values) <= length:
        return values, dates
    else:
        reduced_values, reduced_dates = [], []
        for x in range(0, len(values) - 1, 2):
            temp_value = (values[x] + values[x + 1]) / 2
            temp_date = avg_dates(dates[x], dates[x+1])
            reduced_values.append(int(temp_value))
            reduced_dates.append(temp_date)
        return reduce_list(reduced_values, reduced_dates, length)

def draw_line(values, labels, new_values, new_labels):
    plt.figure(figsize=(10, 8))

    plt.subplot(3,1,1)
    plt.plot(labels, values, 'r')
    plt.title('Old List')
    plt.xticks(rotation=45)

    plt.subplot(3,1,3)    
    plt.plot(new_labels, new_values)
    plt.title('Reduced List')

    plt.show()

def test_fun():
    values = random.sample(range(1, 100), 20)
    values.sort(reverse=False)

    dates = ['2015-01-01', '2015-06-01',
            '2015-07-01', '2015-10-01',
            '2015-12-01', '2016-02-01',
            '2016-04-01', '2016-05-01',
            '2016-08-01', '2016-10-01',
            '2016-11-01', '2017-02-01',
            '2017-03-01', '2017-06-01',
            '2017-09-01', '2017-11-01',
            '2018-01-01', '2018-02-01',
            '2018-04-01', '2018-06-01']

    length = 5

    new_values, new_dates = reduce_list(values, dates, length)

    assert(len(new_values)<=length)

    print("Original list: {} \n {}".format(values, dates))
    print("Original list length: {}".format(len(values)))

    print("Reduced list: {} \n {}".format(new_values, new_dates))
    print("Reduced list length: {}".format(len(new_values)))

    draw_line(values, dates, new_values, new_dates)

test_fun()
