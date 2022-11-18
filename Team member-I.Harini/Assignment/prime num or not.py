Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 11
>>> if num > 1
SyntaxError: expected ':'
>>> if num>1:
...     for i in range(2,int(num/2)+1):
...         if(num%i)==0:
...             print(num,"is not a prime number")
...             break
...         else:
...             print(num,"is a prime number")
... else:
...     print(num,"is not a prime number")
