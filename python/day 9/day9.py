def decompress(compressed):
	decompressed_list = []

	i = 0
	while i < len(compressed):
		tmep = compressed[i]
		if compressed[i].isalpha():
			decompressed_list.append(compressed[i])
			i += 1
			print decompressed_list
		elif compressed[i] == '(':
			for j in range(i, len(compressed[i:]), 1):
				if compressed[j] == ')':
					marker_close = j
					break
			marker = compressed[i+1:marker_close]
			x, y = [int(num) for num in marker.split('x')]
			for repeat in range(y):
				decompressed_list.append(compressed[marker_close+1:marker_close+x+1])
			i = marker_close + x + 1

	return ''.join(decompressed_list)


if __name__ == '__main__':
	with open('input', 'r') as f:
		compressed = [line.strip('\n') for line in  f.readlines()][0]
