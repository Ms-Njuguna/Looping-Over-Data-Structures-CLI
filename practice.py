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


# challenge 3

attempts = 0

while attempts < 3:
    password = input("Enter your password: ")
    if password == "python123":
        print("Access granted!")
        break
    elif password != "python123":
        print("Wrong")
        attempts += 1
else:  
    print("Too many attempts. Access denied.")
   