def bubblesort(xlist):
    """
    バブルソート
    @in xlist (list)
    @return xlist(bubble sort list)
    """

    listlen = len(xlist)
    for i in range(listlen-1):
        for j in range(listlen-1, i, -1):
            if xlist[j] < xlist[j-1]:
                tmp = xlist[j]
                xlist[j] = xlist[j-1]
                xlist[j-1] = tmp
    return xlist

if __name__ == '__main__':
    print(bubblesort([14,46,634,32,2,1,5,34,345,63,36,46,0,4,6,7,3,343]))
