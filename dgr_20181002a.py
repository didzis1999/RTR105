Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x=5
>>> if x<10:
	print('Smaller')

	
Smaller
>>> if x>20:
	print('Bigger')

	
>>> print('Finish')
Finish
>>> x=5
>>> if x == 5:
	print('Equals 5')

	
Equals 5
>>> if x >= 5:
	print('Greater than 4')

	
Greater than 4
>>> if x>= 5:
	print('Greater than or Equals 5')

	
Greater than or Equals 5
>>> if x < 6 : print('Less than 6')

Less than 6
>>> if x <=5:
	print('Less than or Equals 5')

	
Less than or Equals 5
>>> if x != 6 :
	print('Not equal 6')

	
Not equal 6
>>> x=5
>>> print('Before 5')
Before 5
>>> if x == 5:
	print('Is 5')
	print('Is Still 5')
	print('Third 5')

	
Is 5
Is Still 5
Third 5
>>> print('Afterwards 5')
Afterwards 5
>>> print('Before 6')
Before 6
>>> if x == 6:
	print('Is 6')
	print('Is still 6')
	print('Third 6')

	
>>> print('Afterwards 6')
Afterwards 6
>>> x=5
>>> if x>2:
	print('Bigger than 2')
	print('Still bigger')

	
Bigger than 2
Still bigger
>>> print('Done with 2')
Done with 2
>>> 
================== RESTART: /home/user/RTR105/if_test_1.py ==================
0
1
2
3
Bigger than2
4
Bigger than2
>>> 
================== RESTART: /home/user/RTR105/if_test_1.py ==================
0
1
2
3
Bigger than2
4
Bigger than2
>>> 
================== RESTART: /home/user/RTR105/if_test_1.py ==================
Bigger than 2
Still bigger
Done with 2
0
('Done with i', 0)
1
('Done with i', 1)
2
('Done with i', 2)
3
Bigger than2
('Done with i', 3)
4
Bigger than2
('Done with i', 4)
All done
>>> x=5
>>> if x>2:
	print('Bigger than2')
	print('Still bigger')

	
Bigger than2
Still bigger
>>> print('Done with 2')
Done with 2
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
0
('Done with i', 0)
1
('Done with i', 1)
2
('Done with i', 2)
3
Bigger than 2
('Done with i', 3)
4
Bigger than 2
('Done with i', 4)
All done
>>> x=42
>>> if x>1:
	print('More than one')
	if x<100:
		print('Less than 100')

		
More than one
Less than 100
>>> print('All done')
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
0
('Done with i', 0)
1
('Done with i', 1)
2
('Done with i', 2)
3
Bigger than 2
('Done with i', 3)
4
Bigger than 2
('Done with i', 4)
All done
More than one
Less than 100
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
More than one
Less than 100
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Bigger
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Bigger
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/if_test_2.py", line 42, in <module>
    if x<2:
NameError: name 'x' is not defined
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
small
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Below 2
>>> 
