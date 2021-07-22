list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
pos_l1 = []
pos_l2 =[]
for i in list1:
    if i > 0:
        pos_l1.append(i)
print("Positive numbers in" , list1 ,"are " , pos_l1)        
for j in list2:
    if j > 0:
        pos_l2.append(j)
print("Positive numbers in" ,list2,  "are " ,pos_l2) 
