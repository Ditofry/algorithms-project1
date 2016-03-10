# Programming Assignment #1

## Instructions
The assignment asks you to write and perform an empirical complexity analysis of three sorting routines:

 - Insertion sort (the code is already given in the kit)
 - Merge sort (please write the recursive merge sort)
 - Quick sort (please write a randomized quicksort method as covered in class).

## Task #1
Fill in the implementation of mergeSort and quickSort in the mySortingFunctions.py
Use the given grading script to check that your functions work.

## Task #2
Empirically estimate the average and worst case running time for each sorting function. Specifically write Python code that

1. Creates a randomly shuffled list of size n (see the function generateRandomList(n) already implemented in mySortingFunctions.py )

2. Runs the specified sorting function on this list and measures running time
( see the function measureRunningTimeComplexity(sortFunction,lst): already implemented in mySortingFunctions.py )

3. For each value of n ranging from 5, 10, 15, … , 500
  - Compute average and worst-case running time over randomly generated lists of size n
  - Worst case can be generated in one of two ways: simply pass a reverse sorted array or use multiple trials and the maximum running time amonst all trials.
  - Do at least 20 n samples of lists of size n to compute average and “worst case”

4. Plot for each sorting function a graph that shows n on the x-axis and average/worst-case times on the y-axis.

## Submission
The ZIP file should be named `<yourlastname>.<yourfirstname>.prog1.zip`

The ZIP should extract the following files (zip should NOT contain folders in it, it will make our grading harder).

 1. mySortingFunctions.py (the code you will write for your sorting and timing functions)

 2. insertionSort.jpg (an image file showing the plots for worst case and running times for insertion sort)

 3. mergeSort.jpg (an image file showing the plots for worst case and running times for merge sort)

 4. quickSort.jpg (an image file showing the plots for worst case and running times for quick sort)

Anything else will be ignored. Please make sure that no executables or compiled libraries are submitted.

We suggest using R, gnuplot or matplotlib in Python to generate these plots.
