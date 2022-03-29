
#Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:

#Input -> As Soon As Possible. Output -> ASAP.
#Input -> World Health Organization. Output -> WHO.
#Input -> Out of Office. Ouput -> OOO.



x= str (input("enter the full form \n "))
if x=='As Soon As Possible':
            print("ASAP")
elif x=="World Health Organization":
         print("WHO")
elif x =="Out of Office":
         print("ooo")
else:
         print("no short form available")
         
         
