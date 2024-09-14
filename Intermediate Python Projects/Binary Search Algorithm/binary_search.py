# 14.  Binary Search Algorithm   
#     *Description*: Implement a binary search algorithm to search for an element in a sorted list.  
#     *Skills*: Loops, conditionals, algorithms.

def binary_search(search,numberlist):
    
    low = 0
    high = len(numberlist)-1
    
    while (low<=high):
        mid = (low+high)//2
        
        if numberlist[mid] == search:
            print(f'The element {search} is at {mid} index.')
            return mid
        elif numberlist[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    print(f'The element {search} is not in the list.')
    return -1

binary_search(5,[1,2,3,4,5,6,7,8,9])