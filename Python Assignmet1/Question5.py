"""Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
Score 	Grade
>= 0.9 	 A
>= 0.8 	 B
>= 0.7 	 C
>= 0.6 	 D
< 0.6 	 F
"""
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