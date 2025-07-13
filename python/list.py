l1 =  [1,8,7,2,21,15]

# l1.sort() #ascending order
# print(l1)

# l1.reverse() #reversed the list
# print(l1) 

# l1.append(45) #add the value at the end of the list
# print(l1)

# l1.insert(3,8) #add the 8 in index 3 of the list 
# print(l1)

# last_value=l1.pop()
# print(last_value)
# print(l1)

# third_item=l1.pop(2)
# print(third_item)
# print(l1)

# l1.remove(2)
# print(l1)






#wap to store 7 fruits in a list entered by the user

# fruit=[]
# for i in range(7):
#     name=input(f"enter the fruit : {i+1} ")
#     fruit.append(name)

# print("list of the fruit = " ,fruit)


#wap to accept the marks of 6 students  and display them in a sorted mannner


# student=[]
# for i in range(7):
#     marks=int(input(f"enter the marks : {i+1} "))
#     student.append(marks)
#     student.sort()

# print(student)

#write a program to sum  a list with 4 number

student=[]
for i in range(7):
  marks=int(input(f"enter the marks : {i+1} "))
  student.append(marks)

total= sum(student)
print("the sum is :",total)

