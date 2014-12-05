import sys, logging, csv




def read_csv(csv_file):
	with open(csv_file, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		#spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in spamreader:
			print(row)
			sys.exit(0)

def print_usage():
	print("please supply one feature file and one label file with Features and Labels in file names")
	sys.exit(1)