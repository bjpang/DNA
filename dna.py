def dna(currSeq, dnaList):
	if not dnaList:
		return currSeq
	else:
		max_overlap = 0
		nextSeq = dnaList[0]

		for x in range(0, len(dnaList)):
			curr_overlap1 = commonOverlap(currSeq, dnaList[x])
			curr_overlap2 = commonOverlap(dnaList[x], currSeq)
			curr_overlap = max(curr_overlap1, curr_overlap2)
			if max_overlap < curr_overlap:
				max_overlap = curr_overlap
				nextSeq = dnaList[x]

		dnaList.remove(nextSeq)
		if currSeq[-max_overlap:] == nextSeq[:max_overlap]:
			direction = 1
		else:
			direction = 0
		currSeq = combine(currSeq, nextSeq, max_overlap, direction)

		return dna(currSeq, dnaList)

def commonOverlap(seq1, seq2):
	seq1_length = len(seq1)
	seq2_length = len(seq2)

	if seq1_length == 0 or seq2_length == 0:
		return 0
	if seq1_length > seq2_length:
		seq1 = seq1[-seq2_length:]
	elif seq1_length < seq2_length:
		seq2 = seq2[:seq1_length]

	max_overlap = 0
	overlap_length = 1

	while True:
		overlap_seq = seq1[-overlap_length:]
		match_index = seq2.find(overlap_seq)
		if match_index == -1:
			return max_overlap
		overlap_length += match_index
		if seq1[-overlap_length:] == seq2[:overlap_length]:
			max_overlap = overlap_length
			overlap_length += 1

def combine(seq1, seq2, overlap, direction):
	if direction == 1: #direction = 1: seq1 first
		return seq1 + seq2[overlap:]
	return seq2 + seq1[overlap:] #direction = 0: seq2 first

if __name__ == "__main__":
	fragments = open("reads5.txt")
	dnaList = []
	tempList = []
	for line in fragments:
		line = line.strip()
		tempList.append(line)
	for i in range(0, len(tempList)):
		substring = True
		if tempList[i]:
			seq = tempList[i]
			for dnaSeq in dnaList:
				if dnaSeq.find(seq) != -1:
					substring = False
					break
				if seq.find(dnaSeq) != -1:
					dnaList.remove(dnaSeq)
			if substring:
				dnaList.append(seq)

	start_sequence = dnaList[0]
	seq_list = dnaList[1:]
	original_sequence = dna(start_sequence, seq_list)
	print original_sequence
	



