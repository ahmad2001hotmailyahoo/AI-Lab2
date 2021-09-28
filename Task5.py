# Write a list comprehension which, from a list, generates a lowercased version of each string that
# has length greater than five.

def LowerCaseVersion(listOFString):
    for i in range(len(listOFString)):
        if len(listOFString[i]) > 5 :
            listOFString[i] = listOFString[i].lower()
    return listOFString

listsOfString = ["Kamran","Butter","UpperCaseLetter","HighVoltage"]

print(LowerCaseVersion(listsOfString))
