x = [1,2,4,6,8,2,34,6,9,345,8,245,78657,1,32,134,75]

def insertion_sort(x):
    for loop_iteration in range(1,len(x)):
        while_cntr=0
        while x[loop_iteration-while_cntr]<x[loop_iteration-1-while_cntr]:
            x[loop_iteration-1-while_cntr], x[loop_iteration-while_cntr]=x[loop_iteration-while_cntr], x[loop_iteration-1-while_cntr]
            while_cntr+=1
    return x
                
print(insertion_sort(x))