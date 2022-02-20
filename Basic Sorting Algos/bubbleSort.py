def bubbleSort(list):
    for i in range(0,len(list)-1):
        for j in range(len(list)-1):
            # if a first index value is greater than the second index value, swap their positions with each other.
            if (list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

unsortedList=[5, 3, 8, 6, 7, 2]
print(bubbleSort(unsortedList))