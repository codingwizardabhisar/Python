n1=input("enter first number :  ")
# by default input takes all argument as string
n2=input("enter second number : ")
# lets change data type to int type casting 
sum1 =  int(n1) + int(n2) 
sum2=n1+n2
print(sum1)
print(sum2) #in sum2 it add like strings eg 6+6=66
print(type(sum2))

name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break
print(name)




num1 = int(input())
num2 = int(input())
 
# printing the sum in integer
print(num1 + num2)




# input
string = str(input())
 
# output
print(string)



# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)