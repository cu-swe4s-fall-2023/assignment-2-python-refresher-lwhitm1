test -e ssshtest || curl -sSLO https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run get_data_test python ../src/get_data.py test/test_Agrofood_co2_emission.csv "Afghanistan" test/Afghanistan_data.txt
assert_exit_code 0

run plot_hist_test python ../src/hist.py test/Afghanistan_data.txt test/Afghanistan.png "Afghanistan" 'Fires' 'Frequency'
assert_exit_code 0






