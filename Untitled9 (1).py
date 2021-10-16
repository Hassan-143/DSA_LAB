#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[10]:



openl=["(","[","{"] #initializing list for open prenthesis
closel=[")","]","}"]#initializing list for close prenthesis
#defining function to check string
def check(myStr):
    stack=[]
    for i in myStr:
        if i in openl:
            stack.append(i)
        elif i in closel:
            pos = closel.index(i)
            if ((len(stack) > 0) and (openl[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "not ballance"
    if len(stack)==0:
            return "Ballance"
        
    else:
        return "not Ballance"
#call functions
string = "({a+b})"
print(string,"---", check(string))
string = "))((a+b}{"
print(string,"---", check(string))
string = "((a+b))"
print(string,"---", check(string))
string = "))"
print(string,"---", check(string))
string = "[a+b]*(x+2y*{gg+kk})"
print(string,"---", check(string))


# In[ ]:




