# the pos with the slot = 0
# one sec as the capsule passes through a disc

class Disc(object):
	def __init__(self, num, pos):
		self.num_positions = num
		self.position = pos

	def passed_through(self, time):
		if self.position != 0:
			left_to_reset = self.num_positions - self.position
			
			if time > left_to_reset:
				time -= left_to_reset
			elif time == left_to_reset:
				return True
			elif time < left_to_reset:
				return False
	
		if time % self.num_positions == 0:
			return True

		return False


def simulate(time, discs):
	for disc in discs:
		time += 1
		if not disc.passed_through(time):
			return False
			
	return True


if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		data = f.readlines()

	num_discs = len(data)

	discs = []

	for index in range(num_discs):
		line = data[index]
		num = int(line.split('positions')[0].split('has')[-1].strip())
		pos = int(line.split('position')[-1].replace('.', '').strip())
		
		d = Disc(num, pos)
		discs.append(d)

	time = 0

	while not simulate(time, discs):
		time +=1

	print time

	discs.append(Disc(11, 0))

	while not simulate(time, discs):
		time +=1

	print time


	

