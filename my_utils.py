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
                    sys.exit(3)
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(2)
    
    return result


