
#name = 'shubhr'
#lastname = 'bhadauria'
#print(name,lastname)
#a = int(input())
#b=int(input())
#print(a+b)
#a= input('enter a number')
#print(int('a')) :: does not print the ascii value
#name=input()
#print('what you up to,', name,'?')
#l=list('abcdefg')
 #print(l*3)
#for x in l:  #no space b/f for
 #print(x)    #space before print necessary
# l1= [c*2 for c in l]
# print(l1)
#l[0:3]=['x','$']
#print(l)
#print(l[:1])
# l=['3','5','32','54','28','98','33','91']
# print(l[1::2])  #starting from index 1 to end, taking every second character.


#l=list('gfshfeofeihtfewfw')
#l.sort()
#print(l)
#l=['a','aa','abb','abab','aaaa','abbb']
#l.sort()
#print(l)
#l.sort(reverse=True)
#print(l)

#a=int(input())
#b=int(input())
#if a<b:
    #print('the sum is :',a+b)  #the space b/f print is imp
#else:
   #print('the diff is',a-b)    #indent reqd
#if(a<b and                     #how to write multiple if statements
   #a%2==0):
   #print('done')
#while True:                     #interactive shell
    #reply=input('So now what? ')     #it's True not true
    #if reply=='break_it':            #common indentation implies within the brackets
        #break
    #elif reply=='No!':          #no else if : use elif
        #break

#l=['a','b','c','d'] #declaring list, simple way.
#print(l)
#str="hello everybody"
#l=list(str)              #convert string to list.
#print(l)
#l.reverse()
#print(l)
#l=['3','1','5','23','45']
#print(reversed(l))  #returns a reverse iterator object's location
#rint(list(reversed(l))) #returns the reversed list using iterator. No changes, no copy.
#l.append('92')
#print(l)
#print(l.pop(2))    #returns the removed element.
#l.remove('3')      #removes the element by value.
#print(l)

#range function.
#for i in range(7): #selects elements from 0 to n-1
 #print(i)

#for i in range(2,10): #from 2 to n-1
    #print(i)

# for i in range(0,34,4): #prints 0,0+i,0+2i,0+3i.. if 0 is the starting index.
#     print(i)

#connecting range and lists.
#avg=['34','12.45','32.5','85','18','51','90']
# for i in range(0,len(avg),2): #range(len(list_name)) is the tool.
#     print(avg[i])

# for i in range(len(avg)-1,-1,-1): #end should be -1 to traverse the first element.
#     print(avg[i])
# l=list(reversed(list(range(10)))) #convert range to list.
# print(l)

# ------------FUNCTIONS------------------
# def sum(a,b):
#     return a+b
# print(sum(5,4))
# print(sum('padhai',' ho rahi hai:D')) #a and b can be of any type :)

# --------call by value as in c++, numbers don't change
# def swap(a,b):
#     temp=a
#     a=b
#     b=temp
#     print('swaaaaped',a,' ',b)
# x=6
# y=9
# swap(x,y)   #original values don't swap.
# print('the original ones are :',x,' ',y)

#   ------call by reference, list changes
# def assign(a,b):
#     a=2
#     b[1]=':=()'
#     print('inside ',a)
#     print('inside ',b)
# a=3
# b=['2','4','5','7']
# assign(a,b)
# print('outside ',a) #a doesn't change.
# print('outside ',b) #b gets changed.

# ---to avoid changing list
# use assign(a,b[:])
