Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> __builtins__
<module '__builtin__' (built-in)>
>>> __b

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __b
NameError: name '__b' is not defined
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> __builtins__.abs.__doc__
'abs(number) -> number\n\nReturn the absolute value of the argument.'
>>> abs(10)
10
>>> abs(-10)
10
>>> a = 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a = 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> a.__doc__
"int(x=0) -> int or long\nint(x, base=10) -> int or long\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is floating point, the conversion truncates towards zero.\nIf x is outside the integer range, the function returns a long instead.\n\nIf x is not a number or if base is given, then x must be a string or\nUnicode object representing an integer literal in the given base.  The\nliteral can be preceded by '+' or '-' and be surrounded by whitespace.\nThe base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to\ninterpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
>>> type(a)
<type 'int'>
>>> b = 1.5
>>> vars()
{'a': 20, 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> b.__doc__
'float(x) -> floating point number\n\nConvert a string or number to a floating point number, if possible.'
>>> type(b)
<type 'float'>
>>> c = 0
>>> c = D

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c = D
NameError: name 'D' is not defined
>>> c = "D"
>>> c.__doc__
"str(object='') -> string\n\nReturn a nice string representation of the object.\nIf the argument is a string, the return value is the same object."
>>> type(c)
<type 'str'>
>>> burts = "D"
>>> ord(burts)
68
>>> hex(ord(burts))
'0x44'
>>> bin(ord(burts))
'0b1000100'
>>> 
