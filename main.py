# '''
# For in loops
# '''

# students = ['bob', 'Adriana', 'Felix']

# for v in students:
#   print("hi", v)

# print(range(10))
# print(list(range(10)))
# print(list(range(3,6)))
# print(list(range(3,12,2)))

# for x in range(1, 6, 2):
#   print(x*2)

# for i in range(1,6):
#   for j in range (i):
#     print("+" ,end=" ")
#   print()

# '''
# While loops
# '''
# i= 1
# while i<10:
#     print(i)
#     i+=1

#==========================================

#break stratment]
# i= 1
# while i<10:
#     print(i)
#     if i==5:
#       break
#     i+=1

#continue stratment

# i= 0
# while i<5:
#     i+=1
#     if i==4:
#       continue
#     print(i)

for i in range(1,10):
  if i==3:
    break
  print(i)