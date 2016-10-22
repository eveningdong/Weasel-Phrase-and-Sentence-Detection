import nltk
import os
import glob


def isEmptyLine(line):
    if line.strip() == '':
        return True
    else:
        return False

def breakIntoSentences(f):

	sentences = []
	temp = [] 

	file = open(f)

	for line in file:
		if not isEmptyLine(line):
			sentence = line.strip().lower().split('\t')
		
			if sentence[0] != '?' and sentence[0] and '!' and sentence[0] != '.' and '\n' not in sentence[0]:
				temp.append((sentence[0], sentence[2]))
			
			else:
				temp.append((sentence[0], sentence[2]))
				sentences.append(temp)
				temp = []

	return sentences


def countCues(f):

	uncertaintyCueCount = 0
	nonUncertaintycueCount = 0

	sentences = breakIntoSentences(f)

	for sentence in sentences:

		for i, v in enumerate(sentence):

			if "cue-" in v[1]:
				uncertaintyCueCount  += 1
				break
			else:
				nonUncertaintycueCount += 1
				break

	print "Number of uncertain cue sentences", uncertaintyCueCount
	print "Number of non-uncertain cue sentences", nonUncertaintycueCount


def main():
	countCues('aggregated_training.txt')

	
if __name__ == '__main__':
    main()




