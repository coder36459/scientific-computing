def arithmetic_arranger(problems, solutions=False):
	arranged_problems = ""
	sh = solutions
	p = problems
	lp = len(p)
	a = []
	if lp < 6:
		for x in p:
			b = x.split()
			if b[1] == "+" or b[1] == "-":
				if b[0].isnumeric() and b[2].isnumeric():
					o1 = int(b[0])
					o2 = int(b[2])
					if  o1 < 10e3 and o2 < 10e3:
						l1 = len(b[0])
						l2 = len(b[2])
						if l1 == l2:
							a.append(2 * " " + b[0])
							a.append(b[1] + " " + b[2])
							a.append((l1 + 2) * "-")
						if l1 > l2:
							a.append(2 * " " + b[0])
							a.append(b[1] + (l1 - l2 + 1) * " " + b[2])
							a.append((l1 + 2) * "-")
						if l1 < l2:
							a.append((l2 - l1 + 2) * " " + b[0])
							a.append(b[1] + " " + b[2])
							a.append((l2 + 2) * "-")
						if b[1] == "+" and sh == True:
							o3 = o1 + o2
							l3 = len(str(o3))
							if (l1 == l2 and l1 == l3) or (l1 > l2 and l1 == l3) or (l1 < l2 and l2 == l3):
								a.append(2 * " " + str(o3))
							else:
								a.append(" " + str(o3))
						if b[1] == "-" and sh == True:
							o3 = o1 - o2
							l3 = len(str(o3))
							if l3 == l1:
								a.append(2 * " " + str(o3))
							else:
								a.append(" " + str(o3))
					else:
						arranged_problems = "Error: Numbers cannot be more than four digits."
				else:
					arranged_problems = "Error: Numbers must only contain digits."
			else:
				arranged_problems = "Error: Operator must be '+' or '-'."
	else:
		arranged_problems = "Error: Too many problems."
	i = 0
	la = len(a)
	if sh == True:
		if la == 4:
			while i < 4:
				print(a[i])
				i += 1
		if la == 8:
			while i < 4:
				if i == 0 or i == 1 or i == 2:
					arranged_problems += a[i] + 4 * " " + a[i + 4] + "\n"
				if i == 3:
					arranged_problems += a[i] + 4 * " " + a[i + 4]
				i += 1
		if la == 12:
			while i < 4:
				print(a[i] + 4 * " " + a[i + 4] + 4 * " " + a[i + 8])
				i += 1
		if la == 16:
			while i < 4:
				print(a[i] + 4 * " " + a[i + 4] + 4 * " " + a[i + 8] + 4 * " " + a[i + 12])
				i += 1
		if la == 20:
			while i < 4:
				if i == 0 or i == 1 or i == 2:
					arranged_problems += a[i] + 4 * " " + a[i + 4] + 4 * " " + a[i + 8] + 4 * " " + a[i + 12] + 4 * " " + a[i + 16] + "\n"
				if i == 3:
					arranged_problems += a[i] + 4 * " " + a[i + 4] + 4 * " " + a[i + 8] + 4 * " " + a[i + 12] + 4 * " " + a[i + 16]
				i += 1
	else:
		if la == 3:
			while i < 3:
				print(a[i])
				i += 1
		if la == 6:
			while i < 3:
				if i == 0 or i == 1:
					arranged_problems += a[i] + 4 * " " + a[i + 3] + "\n"
				if i == 2:
					arranged_problems += a[i] + 4 * " " + a[i + 3]
				i += 1
		if la == 9:
			while i < 3:
				print(a[i] + 4 * " " + a[i + 3] + 4 * " " + a[i + 6])
				i += 1
		if la == 12:
			while i < 3:
				if i == 0 or i == 1:
					arranged_problems += a[i] + 4 * " " + a[i + 3] + 4 * " " + a[i + 6] + 4 * " " + a[i + 9] + "\n"
				if i == 2:
					arranged_problems += a[i] + 4 * " " + a[i + 3] + 4 * " " + a[i + 6] + 4 * " " + a[i + 9]
				i += 1
		if la == 15:
			while i < 3:
				if i == 0 or i == 1:
					arranged_problems += a[i] + 4 * " " + a[i + 3] + 4 * " " + a[i + 6] + 4 * " " + a[i + 9] + 4 * " " + a[i + 12] + "\n"
				if i == 2:	
					arranged_problems += a[i] + 4 * " " + a[i + 3] + 4 * " " + a[i + 6] + 4 * " " + a[i + 9] + 4 * " " + a[i + 12]
				i += 1
	return arranged_problems
