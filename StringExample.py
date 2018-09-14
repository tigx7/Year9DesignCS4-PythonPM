#This File will go through the basics of 
#String manipulation

#Strings are collections of characters
#Strings are enclosed in " " or ' '
#"Tig"
#"Tigger"
#"Giannis for MVP"

#Two things we need to talk about when we
#Think about Strings

#1)Index - Always starts at 0
# 01234 012345
# Tiger Tigger

#2)Length - Amount of characters
# len("Tiger") = 5
# len("Tigger") = 6

name = "Tiger"

print(name)

sentence = name + " is cool"
print(sentence)
ptint(sentence + "!")

fletter = name[0]
print(fletter)
letters1 = name[0:2]
print(letters1)
letters2 = name[2:]
print(letters2)
letters3 = name[:2]
print(letters3)

lname = len(name)
print(lname)

for i in range(len(name))
	print(name[1])