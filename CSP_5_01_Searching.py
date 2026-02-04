
import random
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    j=0
    if target not in items:
        print(j)
        return -1
    while True:
        i=random.randint(0,len(items)-1)
        j+=1
        if(items[i]==target):
            print(j)
            return i
    pass

def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
  check=0
  for i in range(len(items)):
      check+=1
      if items[i]==target:
            return i, check
  return -1,check

pass


def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it binary search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    low=0
    check=0
    high=len(items)-1
    while low<=high:
        mid=(high+low)//2
        check += 1
        if (items[mid]==target):
            return mid, check
        elif(items[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return -1,  check

    pass
