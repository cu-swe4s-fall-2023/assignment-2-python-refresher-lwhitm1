"""my_util.py houses the function get_column which takes in a file (file_name) a column and value to search that column for (query_column and query_value) and returns the value of a specified column (result_column). Function will append all result values to a list as integers."""


import sys
def get_column(file_name, query_column, query_value, result_column=1):
    result = []
    #try to open the file. If not able, will exit with specified errors
    try:
        with open(file_name, 'r') as f:
            for line in f:
                A = line.strip().split(',')
                #try to append values to list as integers. If not able will exit with specified error
                try:
                    if A[query_column] == query_value:
                        result.append(int(float(A[result_column])))
                except IndexError:
                    print('Something is wrong either country_column or fire_column. Not able to convert value to integer.')
                    sys.exit(1)
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)
    
    return result

def get_mean(result):
    if len(result) == 0:
        print('List is empty. Not able to calculate the mean.')
        sys.exit(1)
    try:
        mean = sum(result) / len(result)
        return mean
    except ZeroDivisionError:
        print('Not able to calculate the mean for empty list.')
        sys.exit(1)

def get_median(result):
    result_sorted = sorted(result)
    n = len(result_sorted)
    if len(result) == 0:
        print('List is empty. Not able to calculate the median.')
        sys.exit(1)
    try:
        if n % 2 == 1:
            median = result_sorted[n//2]
            return median
        else:
            val1 = result_sorted[n//2 -1]
            val2 = result_sorted[n//2]
            median = (val1 + val2)/2
            return median
    except:
        print('Not able to calculate the median.')
        sys.exit(1)

def get_std_dev(result):
    mean = get_mean(result)
    dif_of_squares = []
    if len(result) == 0:
        print('List is empty. Not able to calculate the median.')
        sys.exit(1)
    try:
        for i in result:
            difference = i - mean
            diff_squared = difference ** 2
            dif_of_squares.append(diff_squared)
        variance = sum(dif_of_squares) / len(result)
        std_dev = variance ** (1/2)
        return std_dev
    except:
        print('Unable to calculate the standard deviation.')
        sys.exit(1)

