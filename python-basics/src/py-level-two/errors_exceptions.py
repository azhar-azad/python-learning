# Erros & Exceptions handling

## NOTES:
##      1. Use try to handle user error, not syntax error
##      2. If try is successfull, else and finally will executed
##      3. If try code has an error, except and finally code will executed
##      4. finally code will always execute, no matter what


try:
    f = open("sample_txt_file", "r")
    f.write("Test Write to sample txt file") # This line has error
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
except:
    print("ERROR: DON'T KNOW WHICH ERROR")
else:
    print("SUCCESS")
    f.close()
finally:
    print("THIS BLOCK ALWAYS EXECUTED, NO MATTER WHAT!!")

print("To see if my code comes here while there is an error")