def Merge(dict1, dict2):
    return(dict2.update(dict1))
    
dict1 = {'appu': 10, 'bob': 8}
dict2 = {'danny': 6, 'carol': 4}
 
print(Merge(dict1, dict2))
 
print(dict2)