'''
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count +1
print('Line Count:',count)
'''

'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
'''

'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)
'''

'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not'@uct.ac.za' in line : 
        continue
    print(line)
'''

'''
fname = raw_input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count+1
print('There were',count,'subject lines in',fname)
'''


fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('file cannot be opened',fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count +1
print('There were',count,'subject lines in',fname)        

