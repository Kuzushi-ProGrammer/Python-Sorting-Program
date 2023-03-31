def sort(inputList):
    swapped = False                                 
    for x in range(len(inputList)):                
        try:                                      
            secondValue = inputList[x+1]       
            secondIndex = x+1              
            firstIndex = x                       
            firstValue = inputList[x]    
        except:
            pass
        if firstValue > secondValue:
            swapped = True
            try:
                inputList[firstIndex], inputList[secondIndex] = secondValue, firstValue 
            except:                              
                pass
    if swapped:
        return sort(inputList)                   
    else:                                       
        return inputList