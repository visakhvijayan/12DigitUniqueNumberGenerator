################################################################
# Unique 12 Digit Number Generation                            #
# generating unique 12 digit number & store it in a file       #
# by visakh v                                                  #
# 19/08/2018                                                   #
################################################################
import itertools
import timeit
from itertools import permutations
from random import shuffle

def main():
    
    start = timeit.default_timer()
    FirstHalfGeneration([3,9,8,4,1,7])
    SecondHalfGeneration([9,0,2,6,5,4])
    CombineBothHalf()
    Store12DigitFile()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    # Remove the Following comment for testing uniqueness
    # TestingUnique()
    

def TestingUnique():
    if len(merged) > len(set(merged)):
        print("Elements Not unique")
    else:
        print("Unique")

def Store12DigitFile():
    count =0
    f= open("DigitFile.txt","w+")
    for item in merged:
        if(count>=100000):
            break
        f.write("%s\n" % item)
        count = count + 1

    f.close()

def FirstHalfGeneration(arg):
    for item in permutations (arg):
        FirstHalf.append("".join( map(str, item) ))

def SecondHalfGeneration(arg):
    for item in permutations (arg):
        SecondHalf.append("".join( map(str, item) ))

def CombineBothHalf():
    for i in range(len(FirstHalf)):
        for j in range(len(SecondHalf)):
            temp_.append(map(int,[FirstHalf[i]+SecondHalf[j]]))
    for sublist in temp_: # for removing the [] insidenthe list of list
         for val in sublist:
             merged.append(val)
    shuffle(merged)   


FirstHalf=[]
SecondHalf=[]
temp_=[] # temperory list for storing the list
merged =[] # final result stored
if __name__== "__main__":
  main()
  
 

