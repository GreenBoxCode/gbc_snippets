import math  # Python built in Library for square root function
import warnings

x = [3.2, 3.12, 3.3, 4.33, 4.67, 4.44]
try:
    def sample_std(arr):
        """Return the standard deviation of a sample"""
        sum = 0
        count = len(arr)
        mu = my_mean(arr)
        for i in arr:
            # The Summation
            sum = sum + (i - mu) ** 2
        return math.sqrt(sum / (count - 1))

except Exception as e:
    print(f"Exception has occured\n{e}")


def my_mean(arr):
    sum = 0
    count = len(arr)
    for i in arr:
        sum += i
    result = sum / count
    print(f"The mean is: {result}")
    return result


sstd = sample_std(x)

print(f"The set of {x} has a sample standard deviation of {sstd}")
