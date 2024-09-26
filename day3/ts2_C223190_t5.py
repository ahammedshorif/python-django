num = input("Enter the number: ")

# Iterate from 1 to 10 
for i in range(1, 11):
#skip when i == 3
    if i == 3:
        continue
    print(f"{num} * {i} = {num * i}")
