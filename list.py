list=[1,2,3,4,4,5,6,7,8,8,4,2,1,2]

for i in list:

    dict={
    i:list.count(i)
    }

    dict.update(dict)
    
    print(dict)