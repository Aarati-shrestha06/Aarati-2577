# take a secret word as input (without space)
# then encodes the word using a custom cipher
# replace all vowels with *
# reveerse the entire SyntaxWarningthen shift each letter 2 place ahead in the alphabet (wrap around if needed, eg, y ->a, z->b)
# finally print the resulting encoded word

word=input("enter the secret word : ")
if " " in word:
    print("the word should be without space")
else:
    print("secret word has been taken")

#replace all vowels with *

replaced=word.replace("w","*")
print(replaced)


