age = 15  # Example age variable
#Condition to check if the age is greater than 12
if age > 12:
    print("You are a teenager or older.")
else:
    print("You are a child.")
#Condition to check if the age is less than or equal to 12
if age <= 12:
    print("You are a child.")
else:
    print("You are a teenager or older.")
#Condition to check if the age is exactly 15
if age == 15:
    print("You are exactly 15 years old.")
else:
    print("You are not 15 years old.")
#Condition to check if the age is not equal to 18
if age != 18:
    print("You are not 18 years old.")
else:
    print("You are 18 years old.")
#Condition to check if the age is between 13 and 19 (inclusive)
if 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")
#Condition to check if the age is less than 20 or greater than 30
if age < 20 or age > 30:
    print("You are either under 20 or over 30 years old.")
else:
    print("You are between 20 and 30 years old.")   
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:    
    print("You are an adult.")
else:
    print("You are a senior citizen.")
#Condition to check if the age is not in a specific range
if age < 13 or age > 19:
    print("You are not a teenager.")
else:
    print("You are a teenager.")
#Condition to check if the age is in a specific set of values
if age in {13, 14, 15, 16, 17, 18, 19}:
    print("You are a teenager.")
else:
    print("You are not a teenager.")
#Condition to check if the age is not in a specific set of values
if age not in {20, 21, 22, 23, 24, 25, 26, 27, 28, 29}:
    print("You are not in your twenties.")
else:
    print("You are in your twenties.")
#Condition to check if the age is divisible by 2
if age % 2 == 0:
    print("Your age is an even number.")
else:
    print("Your age is an odd number.")
#Condition to check if the age is a prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if is_prime(age):
    print("Your age is a prime number.")
else:   
    print("Your age is not a prime number.")
