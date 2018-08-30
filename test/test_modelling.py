'''
test_modelling.py - tests whether polyfit makes an accurate linear fit between
two points by taking the midpoint of the line and ensuring the slope-intercept
returns the corresponding midpoint y position. It should if the line is in
fact linear.
'''
from nose.tools import assert_almost_equal
import numpy as np
import pytest

def test_line_fit():
    x = [59, 662]
    y = [10, 20]
    slope, intercept = np.polyfit(x, y, 1)
    midpoint_x = (59+662)/2
    midpoint_y = (10+20)/2
    assert_almost_equal(midpoint_x*slope + intercept, midpoint_y)
