def isomorphic():
    str1 = input("Enter first word: ").lower()
    str2 = input("Enter second word: ").lower()
    
    if len(str1) == len(str2):
        str3 = str2
        for i in range(len(str1)):
            str3 = str3.replace(str2[i], str1[i])
        
        str4 = str1
        for i in range(len(str2)):
            str4 = str4.replace(str4[i], str2[i])
        
        if str1 == str3 and str2 == str4:
            print("These strings are isomorphic.")
        else:
            print("These strings are non-isomorphic.")

    else:
        print("Length difference: Strings are non-isomorphic by default.")

isomorphic()
