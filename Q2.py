def func(a):
    array = [1]*len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if j != i :
                array[i]= array[i]*a[j]
    return array 
