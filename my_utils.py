def get_column(file_name, query_column, query_value, result_column=1):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            A = line.strip().split(',')
            if A[query_column] == query_value:
                result.append(float(A[result_column]))
    return result


