mylist = [5,2,9,1]

def mysort(unsorted: list):
    mysorted = False
    tempvar = None
    max_index = len(unsorted)-1

    while mysorted == False:
        for x in range(len(unsorted)):
            print(x, unsorted)
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
        mysorted = True
        return unsorted

new = mysort(mylist)
print(new)
