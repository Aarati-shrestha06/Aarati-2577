#writea program to detect space in a string
text="Dear Student,  This python course is going well. Thanks"
if " " in text:
    print("double space is detected")

else:
    print("no double space")


#replace the double space from problem 3 with problem 3 with single space

replaced=text.replace("  "," ")
print(replaced)

# write a program to format the following letter using escape sequences character
text1="Dear Student,\nThis python course is going well.\n\tThanks"
print(text1)