'''
#1) read a line from file
fo=open("f1.txt")
L=fo.read()#read entire file content
print(L)
L=fo.read(5)#read only 5 characters of file content
print(L)
L=fo.readline()#read a line
print(L)
fo.close()
'''
'''
#2) read 3 lines
fo=open("f1.txt")
for i in range(3):
  L=fo.readline()#read a line with \n(enter key/ new line character)
  print(L)
#read, write, append
#'r' : read(): 1 character
#readline()
'''
#3) count and display all the lines of file
fo=open("f1.txt")#read mode
L=fo.readline() #1st line
#line is read with \n(new line character/ enter key) at the end
c=0
while L: #line is existing
  c=c+1 #1,2
  print(L)#line has \n at the end+ print
  L=fo.readline()#next line
  
#4) display only odd lines
fo=open("f1.txt")
L=fo.readline()
#line is read with \n(new line character/enter key) at the end
c=0
while L:
  c=c+1#1
  if c%2!=0:
    print(L.rstrip())
    L=fo.readline()
    
#5) take only odd lines in another file
fr=open("f1.txt")#read mode
fw=open("f11.txt",'w')#write mode
L=fr.readline()
#line is read with \n(new line character/ enter key) at the end
c=0
while L:
  c=c+1
  if c%2!=0:
    fw.write(L)
    L=fr.readline()
fr.close()
fw.close()

#6) take only those lines which start with 't'