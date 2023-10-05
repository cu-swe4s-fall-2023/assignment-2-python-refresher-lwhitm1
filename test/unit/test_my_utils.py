import sys
import os
sys.path.insert(0, '../../src') # noqa

import my_utils
import unittest
import random
import numpy as np

class TestMyUtils(unittest.TestCase):
    def test_mean(self):
        test_list = []
        for i in range(10):
            n = random.randint(1,10000)
            test_list.append(n)
        test_mean = np.mean(test_list)
        mean = my_utils.get_mean(test_list)
        self.assertEqual(mean, test_mean)
    
    def test_mean_empty_list(self):
        test_list = []
        mean = my_utils.get_mean(test_list)
        self.assertEqual(mean, None)
    
    def test_median_odd_list_length(self):
        test_list = []
        for i in range(11):
            n = random.randint(1,10000)
            test_list.append(n)
        test_median = np.median(test_list)
        median = my_utils.get_median(test_list)
        self.assertEqual(median, test_median)
    
    def test_median_even_list_length(self):
        test_list = []
        for i in range(10):
            n = random.randint(1,10000)
            test_list.append(n)
        test_median = np.median(test_list)
        median = my_utils.get_median(test_list)
        self.assertEqual(median, test_median)

    def test_median_empty_list(self):
        test_list = []
        median = my_utils.get_median(test_list)
        self.assertEqual(median, None)
    
    def test_std_dev(self):
        test_list = []
        for i in range(10):
            n = random.randint(1,10000)
            test_list.append(n)
        test_std_dev = np.std(test_list)
        test_std_dev = "{:.3f}".format(test_std_dev)
        test_mean = np.mean(test_list)
        std_dev = my_utils.get_std_dev(test_list)
        self.assertEqual(std_dev, test_std_dev)

    def test_std_dev_empty_list(self):
        test_list = []
        std_dev = my_utils.get_std_dev(test_list)
        self.assertEqual(std_dev, None)

