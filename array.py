arr1=[1,2,3,5]
arr2=[2,10,5,21]
res=[]
arr3=[]
combined = [arr1,arr2]



for sublist in combined:
    for item in sublist:
        if item in arr3:
            res.append(item)
        else:
            arr3.append(item)
print(res)                

