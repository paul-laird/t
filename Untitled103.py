
# coding: utf-8

# In[5]:

myGlobal=5
myMaskedVariable=9

def myF():
    myLocal=3
#    global myMaskedVariable
    myMaskedVariable=7
    
myF()

def printVars():
    print(myGlobal)
#    print(myLocal)
    print(myMaskedVariable)
    
printVars()    


# In[ ]:



