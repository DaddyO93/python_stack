x = [1,2,4,6,8,2,34,6,9,345,8,245,78657,1,32,134,75]

def selection_sort(x):
    for start in range(len(x)-1):
        lowest = start
        for i in range(start, len(x)):
            if x[i]<x[lowest]:
                lowest=i
        x[lowest], x[start]=x[start], x[lowest]
    return x
print(selection_sort(x))