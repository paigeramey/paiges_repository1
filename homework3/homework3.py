# 3
# 3.1
def say_goodbye(name):
    print("Goodbye,", name)

say_goodbye("Paige")
# 3.2
def circle_area(radius):
    print(3.14*radius**2)

circle_area(4)

# 4
# 4.1
def subtract(a, b):
    return a - b

print(subtract(5,2))

def multiply(a, b):
    return a * b

print(multiply(5,2))

def divide(a, b):
    return a/b

print(divide(5,2))

# 5
# 5.1
def what_to_wear(*temps):
    low = min(temps)
    high = max(temps)
    return low, high

print(what_to_wear(55, 21, 64, 72, 49))

# 5.2
def is_weekend(day):
    if day == 6 or day == 7:
        return "It's the weekend"
    else:
         return "Not the weekend"

print(is_weekend(4))

# 5.3
def efficientcy(miles, gallons):
    return miles/gallons

print(efficientcy(15, 1))

# 5.4
def encrypt(code):
    last = code % 10 
    n = len(str(code))
    code = code - last #Removes the last digit 
    code //=10
    code = code + (last*(10**(n-1)))
    return code

code = 123
print(encrypt(code))

# 6
# 6.1
def exponent(x, y):
    a = x
    for i in range(1, y):
        x*=a
    return x

print(exponent(2, 3))

# 6.2
# 6.2.1

list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
def for_min(list):
    min = float("inf") 
    for num in list:
        if num < min:
            min = num
    return min

print(for_min(list))

def for_max(list):
    max = float("-inf")
    for num in list:
        if num > max:
            max = num
    return max

print(for_max(list))

def while_min(list):
    min = list[0]
    index = 0
    while index < len(list):
        if list[index] < min:
            min = list(index)
        index += 1
    return min

print(while_min(list))

def while_max(list):
    max = list[0]
    index = 0
    while index < len(list):
        if list[index] > max:
            max = list[index]
        index += 1
    return max

print(while_max(list))

def digit_sum(num):
    sum = 0
    while num > 0:
        last_digit = num % 10
        remaining_num = num //10
        num = remaining_num
        sum += last_digit
    return sum

print(digit_sum(2048))