import csv
with open ('','rb') as f:
	reader=csv.reader(f)
	for row in reader:
		print row[1]
	



