import math


def mean(arr):
    """Find the mean value of an array"""
    try:
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
        return sum / len(arr)
    except Exception as e:
        print(f"An error has occured:/n{e}")


def pearson_correlation(X, Y):
    """From:
    https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
    Pearson's correlation coefficient is the
    covariance of the two variables divided by
    the product of their standard deviations.
    The form of the definition involves a "product moment",
    that is, the mean (the first moment about the origin)
    of the product of the mean-adjusted random variables;
    """
    try:
        mean_X = mean(X)
        mean_Y = mean(Y)
        X_diffs = [x - mean_X for x in X]
        Y_diffs = [y - mean_Y for y in Y]
        sum_X_diffs_sq = sum([x**2 for x in X_diffs])
        sum_Y_diffs_sq = sum([y**2 for y in Y_diffs])
        sum_XY_diffs = sum([x * y for (x, y) in zip(X_diffs, Y_diffs)])
        r = sum_XY_diffs / (math.sqrt(sum_X_diffs_sq) * math.sqrt(sum_Y_diffs_sq))
        return r
    except Exception as e:
        print(f"An error has occured:/n{e}")


X = [1, 2, 3, 4, 4, 4, 5, 6, 7]
Y = [1, 2, 3, 3, 3, 3, 5, 5, 6]

print(pearson_correlation(X, Y))
