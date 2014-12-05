from digit_classifier_utility import *
import sys, logging





def calc_euclidean_distance(digit1, digit2):
	return 0

class digit_classifier(object):
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	ZERO = 0

	def __init__(self, config):
		self.config = config


	def solve_class(self, feature):




#main logic
if __name__ == "__main__":

	#Command line parsing
	argv = sys.argv[1:]
	config = dict()
	if len(argv != 2):
		print_usage()
	else:
		for file_name in argv:
			if "Features" in file_name:
				config["feature_file"] = file_name
			elif "Labels" in:
				config["label_file"] = file_name
			else:
				print_usage()

	digit_classifier(config)
	
	sys.exit(0)