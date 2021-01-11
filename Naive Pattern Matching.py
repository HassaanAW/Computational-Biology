# HASSAAN AHMAD WAQAR
# 22100137
# Naive pattern matching for DNA sequences in Python using for/while loops



prompt = input("Enter File name (eg abc.txt): ")

try:
	myfile = open(prompt, "r") #opening a file
	data = myfile.read() # reading file
	myfile.close()
except:
	print(" File not found ")
	sys.exit()

listform = list(data.split(" ")) #converting file content to list separated by spaces

del listform[0:6] # deleting the first line of the file because it doesnt have the sequence. So removing those many # of elements from list
data = " ".join(listform) #converting list back to string form

count = 0
checker = 0 
for char in data:
	if checker == 0:
		count= count + 1
		if char == 'a':
			checker = 1
data = data[count-1:]
data = data.replace('\n','')

print("The sequence is: ")
print(data)
print(" ")
search = input("Enter string to search: ")
length = len(search)

n = 0
match = 0
for char in data:
	takeout = data[n:n+length] #taking substrings from position n to length of string
	if search == takeout: # comparing seach input to substrings
		match = match + 1 # increment match if search is true 
		n = n + 1
	else:
		n = n + 1

print("Matches: " + str(match) )
