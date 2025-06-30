f = open('manas.txt','r')
# f.close()
# print(f.name)
# print(f.mode)
# print(f.closed) 
b = f.read()    
print(b)
f.close()
# os ->path ->isfile  this checks whether a file exists or not with the help of os module
import os
print(os.path.isfile('manas.txt'))

# file closing multiple ways
# 1st - try exception 
# 2nd - with statement


# readline -  reads single line
# readlines - full
# tell()-tellls the cursor position 
# suppose we have to count number of words length characters
f = open('manas.txt','r')
word_s = 0
char_s = 0
line_s = 0
for line in  f:
    line_s+=1
    line = line.strip('\n')
    char_s += len(line)
    list1 = line.split()
    word_s += len(list1)
f.close()
print(word_s ,char_s ,line_s )