# HASSAAN AHMAD WAQAR
# 22100137

# Reads a FASTA file and calculates nucleotide, and di-nucleotide frequencies.

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

Adenine = 0
Thymine = 0
Cytosine = 0
Guanine = 0
# check to count nucleotides
count = 0
checker = 0 

for char in data:
	if char == "A" or char == "a":
		Adenine = Adenine + 1
	elif char == "C" or char == "c":
		Cytosine = Cytosine + 1
	elif char == "T":
		Thymine = Thymine + 1
	elif char == "G":
		Guanine = Guanine + 1
	elif checker == 0:
		count= count + 1
		if char == 'a':
			checker = 1		
data = data[count-28:]
data = data.replace('\n','')

print("The Sequence is:" )
print(data)
print(" ")
print("Adenine", Adenine)
print("Cytosine", Cytosine)
print("Thymine", Thymine)
print("Guanine", Guanine)

j = 0

AA = 0
AC = 0 
AT = 0
AG = 0

CA = 0
CC = 0
CT = 0
CG = 0

GA = 0
GG = 0
GC = 0
GT = 0

TA = 0 
TT = 0
TG = 0
TC = 0

other = 0

#check to count di-nucleotides

for char in data:
	first = data[j:j+1]
	second = data[j+1:j+2]
	#print(first,second)
	# giving all 16 match conditions
	if (first == "A" or first == "a") and (second == "A" or second == "a"):
		AA = AA + 1
		j = j + 1
	elif (first == "A" or first == "a") and (second == "C" or second == "c"):
		AC = AC + 1
		j = j + 1
	elif (first == "A" or first == "a") and (second == "T" or second == "t"):
		AT = AT + 1
		j = j + 1
	elif (first == "A" or first == "a") and (second == "G" or second == "g"):
		AG = AG + 1
		j = j + 1
	elif (first == "C" or first == "c") and (second == "A" or second == "a"):
		CA = CA + 1
		j = j + 1
	elif (first == "C" or first == "c") and (second == "C" or second == "c"):
		CC = CC + 1
		j = j + 1
	elif (first == "C" or first == "c") and (second == "T" or second == "t"):
		CT = CT + 1
		j = j + 1
	elif (first == "C" or first == "c") and (second == "G" or second == "g"):
		CG = CG + 1
		j = j + 1
	elif (first == "G" or first == "g") and (second == "A" or second == "a"):
		GA = GA + 1
		j = j + 1
	elif (first == "G" or first == "g") and (second == "C" or second == "c"):
		GC = GC + 1
		j = j + 1
	elif (first == "G" or first == "g") and (second == "T" or second == "t"):
		GT = GT + 1
		j = j + 1
	elif (first == "G" or first == "g") and (second == "G" or second == "g"):
		GG = GG + 1
		j = j + 1
	elif (first == "T" or first == "t") and (second == "A" or second == "a"):
		TA = TA + 1
		j = j + 1
	elif (first == "T" or first == "t") and (second == "C" or second == "c"):
		TC = TC + 1
		j = j + 1
	elif (first == "T" or first == "t") and (second == "T" or second == "t"):
		TT = TT + 1
		j = j + 1
	elif (first == "T" or first == "t") and (second == "G" or second == "g"):
		TG = TG + 1
		j = j + 1
	else:
		other = other +1
		j = j + 1

# printing data

print("AA:",AA)
print("AG:",AG)
print("AC:",AC)
print("AT:",AT)

print("GA:",GA)
print("GG:",GG)
print("GC:",GC)
print("GT:",GT)

print("CA:",CA)
print("CG:",CG)
print("CC:",CC)
print("CT:",CT)

print("TA:",TA)
print("TG:",TG)
print("TC:",TC)
print("TT:",TT)
print("Other", other)



