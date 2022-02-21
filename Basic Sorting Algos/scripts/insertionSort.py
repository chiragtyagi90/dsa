def insertionSort(list):
    for i in range(1 ,len(list)):
        temp=list[i]
        j=i-1
        while temp<list[j] and j>-1:
            list[j+1]=list[j]
            list[j]=temp
            j=j-1
    return list

unsortedList=[23,12,3,987,-8,45]
print(insertionSort(unsortedList))