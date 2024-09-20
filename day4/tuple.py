#define the tuple
my_tuple =(5,6,7,8,9)
#define the function for sum of tuple
def sumOfTuple(my_tuple):
    sum=0
    for i in my_tuple:
        sum=sum+ i
    return sum

#call the function
sum = sumOfTuple(my_tuple)
print("Sum of tuple is: ",sum)

my_tuple[2]=10
print(my_tuple[2])
