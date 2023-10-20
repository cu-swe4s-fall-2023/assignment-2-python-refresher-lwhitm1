import sys
from my_utils import get_column

file_name = sys.argv[1]
country_name = sys.argv[2]
out_file = sys.argv[3]


with open(out_file, 'w') as f:
    fires = get_column(file_name, 0, country_name, 3)
    for data in fires:
        f.write(str(data) + '\n')


