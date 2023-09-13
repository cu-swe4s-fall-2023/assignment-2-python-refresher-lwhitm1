from my_utils import get_column
country='United States of America'
country_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
"""fires_column is set to default value of 1. If you wish to 
return another column explicitly state what column you wish 
to use when utilizing the function"""
fires = get_column(file_name, country_column, country, fires_column)
print(fires)
