def validate_array(arr):
    if len(arr) < 4:
        raise ValueError("Array size should be 4 or greater.")
    
    for element in arr:
        if not isinstance(element, (int, float)):
            raise ValueError("Array should contain numeric elements only.")


def calculate_median(arr):
    n = len(arr)
    index = n // 2
    
    if n % 2 == 0:
        return (arr[index - 1] + arr[index]) / 2.0
    else:
        return arr[index]


def calculate_quartiles(arr):
    validate_array(arr)
    arr.sort()
    
    n = len(arr)
    q1 = calculate_median(arr[:n // 2])
    q2 = calculate_median(arr)
    q3 = calculate_median(arr[(n + 1) // 2:])
    
    return q1, q2, q3

def interquartile_range(q1,q3):
    ''' Calculate the interquartile range of an array.'''
    return q3 - q1  

array = [2.5, 5.1, 7.3, 3.9, 9.2, 12.7, 8.4, 6.6, 1.8, 4.3]
q1, q2, q3 = calculate_quartiles(array)

print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"Interquartile range: {interquartile_range(q1,q3)}")
print(f'Minimum: {min(array)}')
print(f'Maximum: {max(array)}')
print(f'Range: {max(array) - min(array):.3F}')

