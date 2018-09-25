Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars
<built-in function vars>
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input ("Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: ")
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainiigais input ("Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: ")
SyntaxError: invalid syntax
>>> mans_mainiigais input("Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: ")
SyntaxError: invalid syntax
>>> mans_mainiigais = input("Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: ")
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: vars()
>>> mans_mainiigais = input("Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: ")
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: 10
>>> vars()
{'mans_mainiigais': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainiigais = input("Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: ")
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainiigais)
<type 'int'>
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 5
5
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: 8
>>> vars()
{'mans_mainiigais': 8, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
>>> 
>>> 
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj,lūdzu,ievadi vienu skaitli: 12
mans_mainiigais = 12
vai Tu esi ievadījis skaitli = 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj,lūdzu,ievadi daļskaitli : 8.96
mans_mainiigais = 8.96000010.3
respektīvi,Tu esi ievadījis skaitli:     8.9600
vēl atmiņā tagad ir arī mainīgais x =      80.2816000
>>> type(x)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj,lūdzu,ievadi daļskaitli : 1
mans_mainiigais = 1.00000010.3
respektīvi,Tu esi ievadījis skaitli:     1.0000
vēl atmiņā tagad ir arī mainīgais x =       1.0000000
>>> type(mans_mainiigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj,lūdzu,ievadi simbolu rindu : 25

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 

