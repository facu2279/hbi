#!/usr/bin/python3
"""
Given a list of non-negative integers representing the
heights of walls with unit width 1, as if viewing the
cross-section of a relief map, calculate how many square
units of water will be retained after it rains
"""


def maxWater(arr, n):
    """
    calculate how many square units of water will be
    retained after it rains
    """
    water = 0

    for i in range(1, n - 1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i + 1, n):
            right = max(right, arr[j])

        water = water + (min(left, right) - arr[i])

    return water


def rain(walls):
    """
    asda
    """
    rain = maxWater(walls, len(walls))
    return rain
