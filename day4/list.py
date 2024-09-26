# my_list = []

# print (type([]))

my_list = [1,2,3,4,5,6,7,8,9]
#define sum of 

def sumOfList(my_list):
    sum=0
    for i in my_list:
        sum=sum+ i
    return sum
def largestNumber(my_list):
    for i in my_list:
        min_num= i
        if  i>min_num:
            min_num=i
            



sum = sumOfList(my_list)
print(sum)  