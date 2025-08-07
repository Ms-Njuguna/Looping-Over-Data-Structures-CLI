# challenge 1

count = int(input("Let's create a counter, from where do you want me to count down? "))

while count > 0:
    print(count) 
    count -= 1
print("Blast off!")


# challenge 2

num = int(input("Give me a number: "))
total = 0

for i in range(1, num):
    total += i
print(f"The total sum is: {total}")

