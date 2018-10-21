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
        return reduce_list(reduced_values, reduced_dates, 10)