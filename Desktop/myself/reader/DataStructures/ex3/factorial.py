'''
n! = 1 if n==0:
   = n * (n-1) if n >= 1
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    print(factorial(5))