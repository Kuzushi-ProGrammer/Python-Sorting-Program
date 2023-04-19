def Search(array, query, length, start, previousIndex):          
    index = int(length + (start - length) // 2)             
    if (index != previousIndex):                      
        if (array[index] == query):
            return print(f"Your chosen villain {query} was found at position {index+1} in the database!\n")
      
        elif (array[index] > query):                            
            previousIndex = index                                
            return Search(array, query, index, start, previousIndex)   
                                                                    
        elif (array[index] < query):                               
            previousIndex = index                                   
            return Search(array, query, length, index, previousIndex)             
    else:
        return print("Sorry, that villain does not seem to be in the list, please try selecting a different villain.\n")