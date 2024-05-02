

# # Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# sort a list without using sort key word ?

list1 =[4,3,6,2,7,5,8]

n= len(list1)
for  i in range(n):
    for j in range(i+1,n):
        if list1 [i]>list1[j]:
            list1[i],list1[j]= list1[j],list1[i]
print( list1)






# +++++++++++++++++++++++++



a = input







