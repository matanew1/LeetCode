def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_recursive(n - 1)
        series.append(series[len(series) - 2] + series[len(series) - 1])
        return series

print(fibonacci_recursive(10))
