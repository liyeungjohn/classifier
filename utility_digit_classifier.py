import sys, logging, csv

def write_features(csv_file, answer):
	with open(csv_file, 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for label in answer:
			spamwriter.writerow([str(label)])


def read_features(csv_file):
	with open(csv_file, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		#spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		observations = []
		for row in spamreader:
			features = row[0].split(",")
			observations.append([float(feature) for feature in features])
	return observations

def read_labels(csv_file):
	with open(csv_file, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		#spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		observations = []
		for row in spamreader:
			observations.append(digit_classifier.parse_class(row[0])
	return observations

def enforce_lists_length_equality(list1, list2):
	if len(digit1) != len(digit2):
		print("unequal length for digits in function calc_euclidean_distance")
		sys.exit(1)

def print_usage():
	print("USAGE:	*Features.csv 	*Labels.csv 	test_file.csv")
	sys.exit(1)