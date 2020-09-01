# Biggie Size
lst = [-1,2,-3,0]
def biggie_size(lst):
    for i in range(0, len(lst),1):
        if lst[i] >0:
             lst[i]="big"
    return lst

print(biggie_size(lst))

# Count Positives
lst = [-1,2,-3,0]
def count_positive(lst):
    x=0
    for i in lst:
        if i>0:
            x+=1
    lst[-1]=x
    return lst
    
print(count_positive(lst))

# Sum Total
lst = [-1,2,-3,0]
def sum_total(lst):
    total = 0
    for i in lst:
        total +=i
    return total

print(sum_total(lst))

# Average 
lst = [-1,2,-3,0]
def avg (lst):
    total = 0
    for i in lst:
        total +=i
    avg = total / len(lst)
    return avg

print(avg(lst))

# Length 
lst = [-1,2,-3,0]
def list_length (lst):
    return len(lst)

print(list_length(lst))

# Minimum 
lst = [-1,2,-3,0]
def min_val(lst):
    lwst = lst[0]
    for i in lst:
        if len(lst) == 0:
            return False
        elif i< lwst:
            lwst = i
    return lwst

print(min_val(lst))

# Maximum 
lst = [-1,2,-3,0]
def max_val(lst):
    hghst = lst[0]
    for i in lst:
        if len(lst)==0:
            return False
        elif i> hghst:
            hghst = i
    return hghst

print(max_val(lst))

# Ultimate Analysis
lst = [-1,2,-3,0]
def ultimate_analysis(lst):
    hghst = lst[0]
    lwst = lst[0]
    total = 0
    for i in lst:
        total +=i
        if i<lwst:
            lwst = i
        elif i>hghst:
            hghst=i
    avg=total/len(lst)
    my_dict={'sumTotal':total, 'average':avg, 'minimum':lwst, 'maximum':hghst, 'length':len(lst)}
    return my_dict

print(ultimate_analysis(lst))

# Reverse List
lst = [-1,2,-3,0]
def reverse_list(lst):
    for i in range(0, len(lst), 1):
        temp=lst[i]
        lst[i]=lst[len(lst)-1-i]
        lst[len(lst)-1-i]=temp
    return lst

print (reverse_list(lst))