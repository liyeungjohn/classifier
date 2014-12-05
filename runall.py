import sys, subprocess, os

p = subprocess.call([sys.executable, "digit_classifier.py", "trainFeatures.csv", "trainLabels.csv", "valFeatures.csv", "valLabels.csv", "1"])
p = subprocess.call([sys.executable, "digit_classifier.py", "trainFeatures.csv", "trainLabels.csv", "valFeatures.csv", "valLabels.csv", "2"])
p = subprocess.call([sys.executable, "digit_classifier.py", "trainFeatures.csv", "trainLabels.csv", "valFeatures.csv", "valLabels.csv", "5"])
p = subprocess.call([sys.executable, "digit_classifier.py", "trainFeatures.csv", "trainLabels.csv", "valFeatures.csv", "valLabels.csv", "10"])
p = subprocess.call([sys.executable, "digit_classifier.py", "trainFeatures.csv", "trainLabels.csv", "valFeatures.csv", "valLabels.csv", "25"])