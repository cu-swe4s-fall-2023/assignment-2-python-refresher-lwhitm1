test -e ssshtest || curl -sSLO https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_print_fires_regular_no_operation python ../../src/print_fires.py  --file_name 'test_Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3
assert_exit_code 0

run test_print_fires_regular_no_operation_wrong_file_name python ../../src/print_fires.py  --file_name 'Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3
assert_exit_code 1

run test_print_fires_regular_mean python ../../src/print_fires.py  --file_name 'test_Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3 --operation 'mean'
assert_exit_code 0

run test_print_fires_regular_median python ../../src/print_fires.py  --file_name 'test_Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3 --operation 'median'
assert_exit_code 0

run test_print_fires_regular_std_dev python ../../src/print_fires.py  --file_name 'test_Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3 --operation 'dev'
assert_exit_code 0
