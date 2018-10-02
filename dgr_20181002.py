Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print('Hello world')
Hello world
>>> print("12x x")
12x x
>>> print(return)
SyntaxError: invalid syntax
>>> print("finally")
finally
>>> x=12.2
>>> y=14
>>> vars
<built-in function vars>
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x=100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> spam    
eggs   spam23    _speed

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> _speed

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    _speed
NameError: name '_speed' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> _speedm

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    _speedm
NameError: name '_speedm' is not defined
>>> "mnemonic"="memory aid"
SyntaxError: can't assign to literal
>>> x1q3z9ocd = 35.0
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> _speed

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    _speed
NameError: name '_speed' is not defined
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> x=3.9*x*(1-x)
>>> print(x)
-46.8
>>> x=0.6
>>> x=3.9*x*(1-x)
>>> print(x)
0.936
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> zz=yy/1000
>>> print(zz)
5
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> 
>>> x=1+2*3-4/5**6
>>> print(x)
7
>>> b=2**3
>>> print(b)
8
>>> ddd=1+4
>>> print(ddd)
5
>>> eee='Hello'+'there'
>>> print(eee)
Hellothere
>>> eee='Hello '+'there'
>>> print(eee)
Hello there
>>> l=5/4.
>>> print(l)
1.25
>>> l=5/4
>>> print(l)
1
>>> xx=1
>>> type(xx)
<type 'int'>
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) +100)199.0
SyntaxError: invalid syntax
>>> print(float(99) +100)
199.0
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10 /2)
5
>>> print(9/2)
4
>>> print(9/2.)
4.5
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv='hello bob'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam=input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam=input('Who are you?')
Who are you?print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1
    print('Welcome',nam)
        ^
SyntaxError: invalid syntax
>>> print('Welcome',nam)print('Welcome',nam)
SyntaxError: invalid syntax
>>> nam=input('Who are you?')
Who are you? Chuck

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> inp=input('Europe floor?')
Europe floor?

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    inp=input('Europe floor?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> inp=input('Europe floor?')
Europe floor?0
>>> usf=int(inp)+1
>>> print('US floor'usf)
SyntaxError: invalid syntax
>>> print('US floor', usf)
('US floor', 1)
>>> #test
>>> input ("Enter hours:")
Enter hours:35
35
>>> input ("Enter Rate:")
Enter Rate:2.75
2.75
>>> vars()
{'x1q3p9afd': 437.5, 'x1q3z9afd': 12.5, 'inp': 0, 'xx': 1, 'zz': 5, 'nsv': 'hello bob', 'usf': 1, 'sval': '123', '__package__': None, '__doc__': None, 'ddd': 5, '__builtins__': <module '__builtin__' (built-in)>, 'yy': 5280, 'y': 14, 'jj': 23, 'x1q3z9ocd': 35.0, '__name__': '__main__', 'b': 8, 'temp': 98.6, 'f': 42.0, 'kk': 3, 'l': 1, 'i': 42, 'eee': 'Hello there', 'x': 7, 'ival': 123}
>>> input ("Enter Rate:")
Enter Rate:2.75.

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    input ("Enter Rate:")
  File "<string>", line 1
    2.75.
        ^
SyntaxError: unexpected EOF while parsing
>>> hours=35
>>> rate=2.75
>>> pay=hours*rate
>>> print(pay)
96.25
>>> input ("Enter hours:")
Enter hours:35
35
>>> input ("Enter Rate:")
Enter Rate:2.75
2.75
>>> vars()
{'x1q3p9afd': 437.5, 'x1q3z9afd': 12.5, 'inp': 0, 'xx': 1, 'zz': 5, 'nsv': 'hello bob', 'usf': 1, 'rate': 2.75, 'pay': 96.25, 'sval': '123', '__package__': None, '__doc__': None, 'ddd': 5, '__builtins__': <module '__builtin__' (built-in)>, 'yy': 5280, 'y': 14, 'jj': 23, 'x1q3z9ocd': 35.0, '__name__': '__main__', 'hours': 35, 'b': 8, 'temp': 98.6, 'f': 42.0, 'kk': 3, 'l': 1, 'i': 42, 'eee': 'Hello there', 'x': 7, 'ival': 123}
>>> hours=35
>>> rate=2.75
>>> pay=hours*rate
>>> print(pay)
96.25
>>> 
