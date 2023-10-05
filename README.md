[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

# Description
- This project is part of my Software Engineering for Scientists class at CU Boulder. Most recent update is due to assignment 4.
    
    - My_utils.py has new functionality! We can now calculate mean, median, and standard deviation.

        - Note: print_fires.py can handle using these operations. Pass the operation (mean, median, dev) that you would like to perform on the list returned from get_column using --operation. 

    - Run run.sh to run print_fires.py which returns a list/array of the number of forest fires in the USA as integers.
        
        - Note: run.sh can handle command line arguments! Currently run.sh has three examples of usage (One that works and two that throw errors.)
        
        - Note: print_fires.py utilizes the get_column function from my_utils.py. The result_column arg is named and set to a default of 1. You must explicitly define the column you want otherwise.


# How to use
- Everything you need to run:
    - A csv file
        - This project is set up to use a file called Agrofood_co2_emission.csv from https://drive.google.com/drive/folders/15dnNnOEjDZDvwzM-_tGGtWjTbNL669i7?usp=drive_link

    - The files included in this repository. Run `git clone <this repo>`
        - run.sh (automates the running of print_fires.py)
        - print_fires.py (Currently set to return a list of the number of forest fires in the USA as integers. Has an optional argument to perform an operation (calculating mean, median, or standard deviation of the list and returning the specified value)
        - my_utils.py (contains the function needed to 'search' the csv and return the results from your query as well as functions that calculate mean, median, and standard deviation of a list of integers)
-How to run:
    - Run `./run.sh`
        - already has line to run scripts with command line arguments specified. You can change arguments in script to fit needs.
    - Run `python print_fires.py --file_name (file name) --country (country name) --country_column (column number that lists country) --fires_column (column number for what type of fires you're interested in)`
        - arg parser with throw errors if you mess it up
    
    - Examples:
        - This will run correctly: `python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3`
            -   Returns: `[1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405]`

        - This will also run correctly (with the specified operation): `python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3 --operation dev`
            - Returns: `1007.703`  

        - This will also run correctly (with the specified operation): `python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3 --operation median`
            - Returns: `1558`

        - This will also run correctly (with the specified operation): `python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'United States of America' --country_column 0 --fires_column 3 --operation mean`
            - Returns: `1928.225806451613`

        - This will throw an error because of an incorrect command line argument argument: `python print_fires.py --file_name Agrofood_co2_emission.csv --country 'United States of America' --country_column five --fires_column 55`
            - Returns: ```usage: print_fires.py [-h] --file_name FILE_NAME --country COUNTRY --country_column COUNTRY_COLUMN [--fires_column FIRES_COLUMN]
                        print_fires.py: error: argument --country_column: invalid int value: 'five''
                    ```
        - This will throw an error if something is not compatible with the script (forces script to throw an error via try/except block): `python print_fires.py --file_name Agrofood_co2_emission.csv --country 'United States of America' --country_column 100`
            - Returns: `Something is wrong either country_column or fire_column. Not able to convert value to integer.`


# How to test
    - From the test directory run:
        - For unit tests:
            - Run: 
            ```
            python -m unittest unit/test_my_utils.py
            ```
        - For functional tests:
            - Run: 
            ```
            bash func/test_print_fires.sh
            ``` 
