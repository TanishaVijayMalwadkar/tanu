def str(str1,str2):
    return str1,str2   
str1=input("enter the first string:")
str2=input("enter the second string:")
if(sorted(str1)==sorted(str2)):
    print("both strings are an Anagram:")
else:
    print("both strings are not an Anagram:")    
