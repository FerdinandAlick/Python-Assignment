#Write a program that uses input to prompt a user for their name and then welcomes them.
score = input("Enter Score: ")
try:
    s=float(score)
except:
    print("Bad Score")
    quit()
if s>1.0 or s<0.0 :
	x="Error"
elif s >= 0.9:
	x = 'A'
elif s >=0.8:
	x='B'
elif s>=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < 0.6:
	x ='F'
else:
	x ="Bad score"
print (x)