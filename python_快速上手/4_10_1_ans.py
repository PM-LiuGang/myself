def PrintList(oList):
    if isinstance(oList,list):
        oLen = len(oList)
        Temp = oList[0:-1]
        oStr = ''
        for i in range(len(Temp)):
            t = Temp[i] + ', '
            oStr += t
        return oStr + 'and ' + oList[-1]
    else:
        return 'Error'
 
t = ['apple','banana','tofu','cat']
 
print (PrintList(t))