import re

print("="*10 + " Welcome to my Calculator" + "="*10)
print("="*10 + " Press quit to exit " + "="*10)
run = True
previous = 0
def calculator():
	# Accessing global variables	
	global run
	global previous
	# We will define a blank equation first 	
	equation = ""
	# Existing equation values are stored in previous
	if previous == 0:
		equation = input("Enter Equation : ")
	else:
		equation = input(str(previous))
	
	# If user wants to quit

	if equation == "quit":
		print("GOODBYE")
		run = False
	else:
		equation = re.sub("[a-zA-Z:;,.' '(){}]",'',equation)

	
	try:	
		if previous == 0:
			previous = eval(equation)
		else:
			# Previous equations are concatenated with current equations			
			previous = eval(str(previous) + equation)
	except: 
		print('You entered wrong query!')
		
while run:
	calculator()	
