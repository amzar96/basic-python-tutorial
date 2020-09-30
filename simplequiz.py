##############################
# SIMPLE QUIZ USING PYTHON
# BY MOHAMAD AMZAR
##############################

##############################
# SET THE SCORE TO 0
##############################
score = 0
correct = 0
correct = int(correct)
score = int(score)

##############################
# WELCOME BACK
##############################
name = input("Your name is? ")
print("============\nHi %s, welcome to simple quiz game!"%(name))
print("Your score now is %d \n============"%(score))


##############################
#QUESTION 1
##############################
print("\nQ1) The language spoken by the people in Pakistan is ?")
print("A) Hindi \nB) Palauan \nC) Sindhi \nD) Nauruan")
ans1 = input("\n     Your answer is ---->")

if (ans1 is "C"):
	score+=5
	correct+=1
	print("\nYES! You are correct %s :)"%(name))
else :
	score+=0
	print("\nOOPS! You are wrong %s :("%(name))



##############################
#QUESTION 2
##############################

print("\nQ2) What is the standard taste of the water ?")
print("A) No taste \nB) Sour \nC) Sweet \nD) Salty")
ans2 = input("\n     Your answer is ---->")

if (ans2 is "A"):
	score+=5
	correct=+1
	print("\nYES! You are correct %s :)"%(name))

else :
	score+=0
	print("\nOOPS! You are wrong %s :("%(name))

##############################
#TOTAL MARK & GRADE
##############################
'''
avg = 0.0
avg = float(avg)
totalQuestion = 2
avg = ((correct/totalQuestion)*100)
print(avg)
print(correct)
'''
print("Your total score is %d out of 10"%(score))






