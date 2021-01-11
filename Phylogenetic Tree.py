

def main():
	""" 
	Matrix is assumed to be like this:
		A 	B 	C 	D
	A 	0	2	3	7
	B 	2	0	6	4
	C 	3	6	0	1
	D 	7	4	1	0

	Sample test files have also been uploaded
	"""
	filename = input(" Enter filename (e.g. tree.txt):")
	#Extraction of data
	listform = []
	myFile = open(filename, "r" )
	for Row in myFile:
	    curr = Row.split('\t') 
	    listform.append(curr)
	myFile.close()
	#print(listform)

	#Extraction of distances
	data = []
	distances = []
	for i in range(0, len(listform) ):
		for j in listform[i]:
			data.append(j.strip())
			try:
				curr = int(j)
				distances.append(curr) # creation of a distance list
			except:
				pass
	#print(distances)

	# Making dictionary to store headers
	row = {}
	col = {}
	converted =[]
	for i in listform[0]:
		converted.append(i.strip())

	store = []
	count = 0
	for i in  converted:
		if(i != ''):
			store.append(i)
			row.update({count:i})
			col.update({count:i})
			count = count + 1
	# print(row)
	# print(col)

	# Making 2D matrix for distances
	num_row = len(row)
	num_col = len(col)
	size = num_row
	matrice = []
	new = []
	count = 0
	for i in range(num_row):
		for j in range(num_col):
			new.append(distances[count])
			count = count + 1
		matrice.append(new) 
		new = []
	#print(matrice[2][1])
	# print(row[0]+col[0])

	check = termination(matrice, num_row, num_col) # check termination condition intially
	while(check == True ):
		target_row, target_col, smallest = Find_Min(matrice, num_row, num_col) # finding minimum value and its corresponding row and col
		new_entry = "(" + col[target_col] + ","  + row[target_row] + ")" # add a new entry to the dictionary which is in newick format
		
		row.update({num_row: new_entry})
		col.update({num_col: new_entry})
		#update row and col size
		num_row = len(row)
		num_col = len(col)

		matrice = Update_Tables(matrice, num_row, num_col, target_row, target_col) # updating tables include setting used entries to 0s and calculating new distances
		check = termination(matrice, num_row, num_col) # check termination condition again

	get_newick = len(row)-1 # last value will be newick notation itself
	print(" Newick notation:", row[get_newick] )
	
def Find_Min(table, rows, cols):
	target_row = 0
	target_col = 0
	curr_min = 10000 # arbitrary number assuming no distance will be greater than this. If distance is greater than this, change curr_min to a higher number  
	for i in range(rows):
		for j in range(cols):
			if(table[i][j] < curr_min and table[i][j] != 0):
				curr_min = table[i][j]
				target_row = i
				target_col = j
	# print(curr_min)
	# print(target_row,target_col)
	return target_row, target_col, curr_min

def Update_Tables(matrix, rows, cols, target_row, target_col):
	# create a new distance matrix
	new_matrix = []
	new = []
	for i in range(rows):
		for j in range(cols):
			try:
				new.append(matrix[i][j])
			except:
				new.append(0)
		new_matrix.append(new)
		new = []

	# Update Col
	for i in range(0,cols):
		if(i == target_row or i == target_col):
			new_matrix[i][cols-1] = 0
		elif(i == cols-1):
			new_matrix[i][cols-1] = 0
		else:
			new_matrix[i][cols-1] = ( new_matrix[i][target_row] + new_matrix[i][target_col] )/ 2
	
	# Update Row
	for i in range(0,rows):
		if(i == target_row or i == target_col):
			new_matrix[rows-1][i] = 0
		elif(i == rows-1):
			new_matrix[rows-1][i] = 0
		else:
			new_matrix[rows-1][i] = ( new_matrix[target_row][i] + new_matrix[target_col][i] )/ 2

	# making target_row and target_col entries 0 
	for i in range(rows):
		new_matrix[target_col][i] = 0
		new_matrix[target_row][i] = 0
	for i in range(cols):
		new_matrix[i][target_row] = 0
		new_matrix[i][target_col] = 0

	# print(new_matrix)
	return new_matrix

def termination(matrix, rows, cols):
	# repeat loop until all values are 0 in the matrix
	count = 0
	for i in range(rows):
		for j in range(cols):
			if(matrix[i][j] != 0):
				count = count + 1
	if(count == 0):
		return  False
	else:
		return True 


main()














