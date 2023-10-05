#!/bin/bash

set -u
set -o pipefail

#This script runs print_fies.py with the updated command line arguments. The first example should run. The other two should have errors. 

#This one should work
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3

#This shoould also work
python print_fires.py  --file_name 'Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3 --operation 'mean'
set +e
#This one should throw an error via try except blocks in my_utils.py
python print_fires.py --file_name Agrofood_co2_emission.csv --country 'United States of America' --country_column 100 


#This one should also give an error via arg parser in print_fires.py
python print_fires.py --file_name Agrofood_co2_emission.csv --country 'United States of America' --country_column five --fires_column 55
set -e
