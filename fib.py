n='hello'
# # print(n)

def practice(name):
   return 'hello ' + name

# print(practice('lianne')+"!")

def square(number):
    return number*number

# print(square(5)+square(12))

total=0
for i in range (1,11):
    total = total +i
 
# print(total)
    
def added(number):
    if number == 1:
        # print('the sum of 1 is 1')
        return 1
    else: 
        # print('trying to find the sum of ' + str(number) + 'we are going to add it to '+ str(number-1))
        return number + added(number-1) 

# # print(added(10))

def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# print(fib(10))

for i in range(1,10):
    # print('the fib of ' +  str(i) + ' is ' + str(fib(i)))

# def power(n):
#     i=0
#     while True:
#         if n == 2**i:
#             return True
#         if 2**i > n:
#             return False
#         i=i+1

# # print(power(1000000))

# recursion for Two
# def recursiveTwo(n):
#     if n <= 0:
#         return False
#     elif n == 2:
#         return True
#     elif n == 1: 
#         return True
#         # % returns remainder after dividing, number is odd if the remainder is 1
#     elif n%2 == 1:
#         return False
#     else: 
#         return recursiveTwo(n/2)

# # recursion for Three
# def recursiveThree(n):
#     if n <= 0:
#         return False
#     elif n == 1:
#         return True
#     # if n is not divisible by 3, then n is not a power of 3
#     elif n%3 != 0:
#         return False
#     else:
#         return recursiveThree(n/3)
    

    def isPowerOfFour(n):
        if n <= 0:
            return False
        elif n == 4:
            return True
        elif n == 1: 
            return True
        elif n%4 != 0:
            return False
        else: 
            return isPowerOfFour(n/4)

print(isPowerOfFour(6))


def runningSum(nums):

        newArray=[]
        newArray.append(nums[0])
        for i in range (len(nums)-1):
            newNum = newArray[i]+ nums[i+1]
            newArray.append(newNum)
        return newArray

print(runningSum([1,2,3,4]))
