"""get_fires.py will utilize the get_column function from my_utils.py. Luckily we have used arg parser and will help with any argument inputting mishaps. """

import sys
import argparse
from my_utils import get_column



def get_args():
    parser = argparse.ArgumentParser(description='''utilize get_column function from my_utils.py 
                                                    to return list of number of fires for a specified country.''', 
                                     prog='print_fires.py')
    parser.add_argument('--file_name',
                        type=str,
                        help='''Name of file.Typically a csv containing fire data for each country.''',
                        required=True)
    parser.add_argument('--country',
                        type=str,
                        help='''Name of the country you would like to evaluate''',
                        required=True)
    parser.add_argument('--country_column',
                        type=int,
                        help='''Indicates the position of the column in which the countries are listed.''',
                        required=True)
    parser.add_argument('--fires_column',
                        type=int,
                        help='''Indicates the position of the column for the fire type you are interested
                            in. Default value is set to 1- you must explicitly state which column you would
                            like to use otherwise.''',
                        required=False)

    args = parser.parse_args()
    return args

def main():
    arg = get_args()

    fires = get_column(arg.file_name, arg.country_column, arg.country, arg.fires_column)
    print(fires)

if __name__ == '__main__':
    main()