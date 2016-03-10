import sys
import gradeSorting as gs
import mySortingFunctions as msf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        sortsToGraph=['mergeSort','quickSort','insertionSort']
    else:
        sortsToGraph=sys.argv[1:len(sys.argv)]

    print('Graphing the following functions:',sortsToGraph)

    testPassed = 0
    for fns in sortsToGraph:
        lst = gs.generateRandomList(42)
        lstRet = gs.callUserSortFunction(lst,fns)
        (passed,reason) = gs.checkAscendingSorted(lstRet,lst)
        if (passed):
            plt.plot(lstRet)
            plt.ylabel('some numbers')
            plt.savefig('foo.png')
        else:
            gs.failedTest(lst,lstRet,fns,reason)

    # plt.plot([1,2,3,4])
    # plt.ylabel('some numbers')
    # plt.savefig('foo.png')
