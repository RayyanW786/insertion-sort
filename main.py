mylist = ["z", "c", "t", "l", "a", "m", "v", "k", "f", "g", "y", "p"]

def mysort(unsorted: list) -> list:
    mysorted = False
    tempvar = None
    max_index = len(unsorted)-1

    while mysorted == False:
        
        for x in range(len(unsorted)):
            current_val = mylist[x]
            if x < max_index:
                next_val = mylist[x+1]
                if current_val > next_val:
                    tempvar = current_val
                    unsorted.remove(tempvar)
                    for y in range(len(unsorted)):
                        my = unsorted[y]
                        if my > tempvar:
                            unsorted.insert(y, tempvar)
                            break
                        else:
                            if y == len(unsorted)-1:
                                unsorted.insert(len(unsorted), tempvar)

            else:
                 break
                
        for x in range(len(unsorted)):
            current_val = mylist[x]
            if x < max_index:
                next_val = mylist[x+1]
                if current_val > next_val:
                    break
            else:
                mysorted = True
                return unsorted
                    
            
                           

new = mysort(mylist)
print(new)
