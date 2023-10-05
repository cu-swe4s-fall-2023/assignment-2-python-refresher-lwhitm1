"""my_util.py houses the function get_column which takes in a file (file_name) a column and value to search that column for (query_column and query_value) and returns the value of a specified column (result_column). Function will append all result values to a list as integers. You can then perform a number of operations on the list of integers, including calculating the mean, median, and standard deviation"""


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
    try: #try to calculate the mean
        mean = sum(result) / len(result)
        return mean
    except ZeroDivisionError: #not able to calculate the mean of an empty list
        return None
    except TypeError: #something in the list is not an integer
        return None

def get_median(result):
    result_sorted = sorted(result)
    n = len(result_sorted)
    try: #try to calculate the median of this list. We already sorted it in ascending order
        if n % 2 == 1: #if there's an odd number of items in list, we only need to find the one in the middle
            median = result_sorted[n//2]
            return median
        else: #if even number of items, have to average the two middle numbers
            val1 = result_sorted[n//2 -1]
            val2 = result_sorted[n//2]
            median = (val1 + val2)/2
            return median
    except IndexError: #something is wrong with the list (might be empty)
        return None
    except TypeError: #something is wrong with the list. Something isn't an integer
        return None

def get_std_dev(result):
    dif_of_squares = []
    try: #std deviation requires knowing the mean. Use your get_mean function to do this
        mean = get_mean(result)
        try: #If able to get the mean, proceed with the calculation of the standard deviation
            for i in result:
                difference = i - mean
                diff_squared = difference ** 2
                dif_of_squares.append(diff_squared)
            variance = sum(dif_of_squares) / len(result)
            std_dev = variance ** (1/2)
            std_dev = "{:.3f}".format(std_dev)
            return std_dev
        except ZeroDivisionError: #something wrong with the list, might be empty
            return None
    except: #not able to get the mean
        return None
