import copy
import random
# Consider using the modules imported above.

class Hat:
	
	def __init__(self, **kwargs):
		self.color_number = {**kwargs}
		self.contents = []
		for x in self.color_number:
			i = 0
			while i < self.color_number[x]:
				self.contents.append(x)
				i += 1
				
		self.numberOfBallsInTheHat = len(self.contents)
	
	def draw(self, numberOfBallsToDraw):
		
		drawnBalls = []
		
		if numberOfBallsToDraw > self.numberOfBallsInTheHat:
			return self.contents
		
		i = 0
		while i < numberOfBallsToDraw:
			ball = random.choice(self.contents)
			self.contents.remove(ball)
			drawnBalls.append(ball)
			i += 1
			
		return drawnBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	
	expected = []

	for c, a in expected_balls.items():
		i = 0
		while i < a:
			expected.append(c)
			i += 1
			
	j = 0
	m = 0
	while j < num_experiments:
		chat = copy.deepcopy(hat)
		drawn = chat.draw(num_balls_drawn)
		ex = copy.copy(expected)
		dr = copy.copy(drawn)
		compared = []
		
		for d in sorted(dr):
			for e in sorted(ex):
					if d == e and dr.count(d) == ex.count(e):
						dr.remove(d)
						ex.remove(e)
						compared.append(d)
					else:
						for d in sorted(dr):
							for e in sorted(ex):
								if d == e and (dr.count(d) > 0 and ex.count(e) > 0):
									dr.remove(d)
									ex.remove(e)
									compared.append(d)
											
		if sorted(expected) == sorted(compared):
			m += 1
			
		j += 1

	return m / num_experiments
