# Name: Brandon Barrett
# Email: barretbj@colorado.edu
# SUID: 810-05-1814
#
# By submitting this file as my own work, I declare that this
# code has been written on my own with no unauthorized help. I agree to the
# CU Honor Code. I am also aware that plagiarizing code may result in
# a failing grade for this class.
from __future__ import print_function
from PIL import Image
import sys
import random
import numpy as np
import time
import matplotlib.pyplot as plt

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2 # C-style division with truncation
        # Gotta love python
        left = lst[:mid]
        right = lst[mid:]
        # Divide and Conquer
        mergeSort(left)
        mergeSort(right)
        return combineLists(lst, left, right) # return sorted lists
    return lst # if the list is len == 1 then its trivially sorted

def combineLists(lst, left, right):
    i, j, k = 0, 0, 0
    # This is where we merge our lists, itterating through the smallest
    # values and adding them to the returned lst
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
    return lst

#------ Quick Sort --------------
def quickSort(lst):
    # just abstract the divide and conquer so that we only need to
    # pass a single argument to the quickSort function
    divideConquer(lst, 0, len(lst) - 1)
    return lst

# SITATION: I got the idea for this design pattern at
# https://en.wikipedia.org/wiki/Quicksort, although my implementation is still different
def divideConquer(lst, first, last):
    # if first == last then it's trivially sorted
    if first < last:
        # Loosely sort around pivot and return new pivot
        split = partition(lst, first, last)
        # Recurse left side
        divideConquer(lst, first, split - 1)
        # recurse right side
        divideConquer(lst, split + 1, last)

def partition(lst, first, last):
    left = first + 1
    right = last
    # since list is random, we can use first item as a pivot strategy
    pivot = lst[first]

    done = False
    while not done:
        # Move until we exceed left val
        while left <= right and lst[left] <= pivot:
            left = left + 1

        # Move right inward
        while lst[right] >= pivot and right >= left:
            right = right - 1
        # We've gone as far as we need
        if right < left:
            done = True
        else:
            # Switch left and right
            tmp = lst[left]
            lst[left] = lst[right]
            lst[right] = tmp

    tmp = lst[first]
    lst[first] = lst[right]
    lst[right] = tmp
    # New pivot point
    return right

# ------ Timing Utility Functions ---------

# Code below is given only for demonstration purposes

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst

def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)

def analyzeRuntimeComplexity(lowBound, highBound):
    functionStore = {
        'mergeSort': mergeSort,
        'quickSort': quickSort,
        'insertionSort': insertionSort
    }

    for fnc in ['mergeSort','quickSort','insertionSort']:
        nValues = []
        avgVals = []
        worstAvgVals = []
        worstVals = []
        sampleSize = 20
        for n in range(lowBound, highBound, 5):
            # Compute average running time over randomly generated lists of size n
            avgCaseComplexity = 0
            worstAvgComplexity = 0
            for i in range(sampleSize * n):
                testList = generateRandomList(n)
                runningTime = measureRunningTimeComplexity(functionStore[fnc], testList)
                avgCaseComplexity += runningTime
                # keep it if we have a new high
                worstAvgComplexity = max(worstAvgComplexity, runningTime)

            # Keep track of our iteration for x-axis
            nValues.append(n)
            # Find our averages
            avgVals.append(avgCaseComplexity / (sampleSize * n))
            worstAvgVals.append(worstAvgComplexity)

        # Take care of our plotting
        plt.plot(nValues, avgVals, 'g', nValues, worstAvgVals, 'r')
        plt.legend(['average', 'worst average'], loc='upper left')
        plt.ylabel('Running Time')
        plt.xlabel('list size')

        functionName = fnc + '.png'
        # Save figure
        plt.savefig(functionName)
        # If we don't clear the figure then we'll see previous fnc data
        # on this plot
        plt.clf()
        Image.open(functionName).save(fnc + '.jpg','JPEG')
