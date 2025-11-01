#To check password strength
'''
To Do:- 
	How to run program on repeat if password doesnt meet specifications
'''
def main():
	
	#message
	print("Password must contain minimum: \n 1 Upprecase Character \n 1 Lowercase Character \n 1 Special Character \n 1 Digit");
	print('Password must be 8 characters long.');
	
	#Initialisation
	upper_case=0;
	lower_case=0;
	special_charac=0;
	digit=0;
	charac_count=0;

	#take input from user
	password= input("Enter a password: ");
	
	#Excess each element in password
	for x in password:

		#Uppercase
		if x.isupper():
			upper_case+=1;
	
		#Lowercase		
		elif x.islower():
			lower_case+=1;

		#Digit
		elif x.isdigit():
			digit+=1;

		#Special Character
		else:
			special_charac+=1;
		
		#Count number of characters
		charac_count+=1;

################################################################################################

	#Check if conditions met
	if upper_case>0 and lower_case>0 and digit>0 and special_charac>0 and charac_count>=8:
		print('Password meets specified conditions.');
	
	else:
		print("Password doesn't meet specific conditions.");
		
		#Showing the user what is wrong
		#uppercase
		if upper_case==0:
			print("Upper case character not entered.");

		#lowercase
		if lower_case==0:
			print("Lower case character not entered.");

		#Special Character
		if special_charac==0:
			print("Special character not entered.");

		#Digit
		if digit==0:
			print("Digit not entered.");

		#Length
		if charac_count<8:
			print('Password has to be more than or equal to 8 characters');



if __name__=="__main__":
	main();