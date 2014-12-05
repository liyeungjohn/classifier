from utility_digit_classifier import *
from math import sqrt
import sys, logging

logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)

def calc_euclidean_distance(digit1, digit2):
	enforce_lists_length_equality(digit1, digit2)
	distance = 0
	for i in range(len(digit1)):
	 	distance += pow((digit1[i] - digit2[i]), 2)
	return sqrt(distance)

class digit_classifier(object):
	COMPUTE_MODE = 0
	VERIFY_MODE = 1

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
		self.mode = config["mode"]
		self.train_features = read_features(config["feature_file"])
		self.train_labels = read_labels(config["label_file"])
		self.test_features = read_features(config["test_file"])
		self.k = int(config["k"])
		enforce_lists_length_equality(self.train_features, self.train_labels)
		logging.debug("config:  " + str(self.config) + "\n")

	def solve(self):
		answer = []
		for test_number in self.test_features:
			answer.append(self.solve_class(test_number))
		return answer

	def treat_answer(self, answer):
		write_features("digitsOutput" + str(self.k) + ".csv", answer)		
		if self.mode == digit_classifier.VERIFY_MODE:
			solution = read_labels(config["solution_file"])
			enforce_lists_length_equality(answer, solution)

			total = len(answer)
			diff = 0
			for i in range(total):
				if answer[i] != solution[i]:
					diff += 1
			f = open("error_rate.txt", "a")
			f.write("config:  " + str(self.config) + "\n")
			f.write("Error rate: " + str(diff/total) + " diff: " + str(diff) + " total: " + str(total) + "\n")
			f.close()

	def solve_class(self, feature):
		distance_list = []
		for i in range(len(self.train_features)):
			distance = calc_euclidean_distance(feature, self.train_features[i])
			distance_list.append((distance, self.train_labels[i]))
		distance_list = sorted(distance_list, key=lambda number: number[0])
		distance_list = distance_list[:self.k]
		return self.resolve_votes(distance_list)

	def resolve_votes(self, votes):
		candidates = dict()
		for vote in votes:
			candidate_key = vote[1]
			if not candidate_key in candidates:
				candidates[candidate_key] = 0
			candidates[candidate_key] += 1 
		return max(candidates, key=candidates.get)

	@staticmethod
	def parse_class(csv_class):
		return int(csv_class)

#main logic
if __name__ == "__main__":

	#Command line parsing
	argv = sys.argv[1:]
	if not (len(argv) == 4 or len(argv) == 5):
		print_usage()

	config = dict()
	config["mode"] = digit_classifier.COMPUTE_MODE
	config["feature_file"] = argv[0]
	config["label_file"] =  argv[1]
	config["test_file"] =  argv[2]
	config["k"] = argv[3]
	if len(argv) == 5:
		config["mode"] = digit_classifier.VERIFY_MODE
		config["solution_file"] = argv[3]
		config["k"] = argv[4]

	solver = digit_classifier(config)
	answer = solver.solve()
	solver.treat_answer(answer)
	sys.exit(0)