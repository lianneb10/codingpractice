n='hello'
print(n)

def practice(name):
   return 'hello ' + name

print(practice('lianne')+"!")

def square(number):
    return number*number

print(square(5)+square(12))

total=0
for i in range (1,11):
    total = total +i
 
print(total)
    
def added(number):
    if number == 1:
        print('the sum of 1 is 1')
        return 1
    else: 
        print('trying to find the sum of ' + str(number) + 'we are going to add it to '+ str(number-1))
        return number + added(number-1) 

# print(added(10))

def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))

for i in range(1,10):
    print('the fib of ' +  str(i) + ' is ' + str(fib(i)))

def power(n):
    for i in range(0,n):
        print(2**i)
        if n == 2**i:
            return True
        if 2**i > n:
            return False
    return False

print(power(1000000))