a=int(input('Pls enter a number: '))

def factorial(a):
    if  a<2:
        return 1
    else:
        return a*factorial(a-1)

Factorial = factorial(a)
print('The factorial of',a,'is',Factorial)
print('Thank You')