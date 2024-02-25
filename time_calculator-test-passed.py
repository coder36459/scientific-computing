def add_time(start, duration=False, optional=False):
	
	if duration == False:
		duration = "0:00"
	
	startTime = start
	durationTime = duration
	startingDayOfTheWeek = optional
	new_time = ""
	
	clockFormat = ["AM", "PM"]
	dayOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	
	splitStartTime = startTime.split()
	oneStartTime = splitStartTime[0].split(":")
	hourStartTime = int(oneStartTime[0])
	minuteStartTime = int(oneStartTime[1])
	clockFormatStartTime = splitStartTime[1]
	
	splitDurationTime = durationTime.split()
	oneDurationTime = splitDurationTime[0].split(":")
	hourDurationTime = int(oneDurationTime[0])
	minuteDurationTime = int(oneDurationTime[1])
	
	if clockFormatStartTime == "AM":
		hourStartTime
	elif clockFormatStartTime == "PM":
		hourStartTime += 12
	
	resultHour = hourStartTime + hourDurationTime
	resultMinute = minuteStartTime + minuteDurationTime
	
	if resultMinute < 60:
		resultHour
	else:
		resultHour += 1
		m = resultMinute
		resultMinute -= 60
	
	sResultMinute = ""
	
	if resultMinute < 10:
		sResultMinute += "0" + str(resultMinute)
	else:
		sResultMinute = str(resultMinute)
	
	resultDay = resultHour // 24
	resultDayHour = resultHour % 24
	
	if startingDayOfTheWeek != False:
		startingDayOfTheWeek = startingDayOfTheWeek.lower()
		
		i = 0
		thatDay = ""
		
		if resultDay > 1:
			ra = resultDay % 7
			while i < len(dayOfTheWeek):
				if startingDayOfTheWeek == dayOfTheWeek[i].lower():
					if i + ra < 7:
						thatDay = dayOfTheWeek[i + ra]
					else:
						thatDay = dayOfTheWeek[7 - ra - 1]
				i += 1
		elif resultDay == 1:
			while i < len(dayOfTheWeek):
				if startingDayOfTheWeek == dayOfTheWeek[i].lower():
					if i + 1 < 7:
						thatDay = dayOfTheWeek[i + 1]
					else:
						print(">7")
				i += 1
	else:
		startingDayOfTheWeek = False
		
	if resultDay > 1:
		if startingDayOfTheWeek != False:
			if clockFormatStartTime == "AM":
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[1]}, {thatDay.capitalize()} ({resultDay} days later)"
			elif clockFormatStartTime == "PM":
				if resultDayHour == 0:
					resultDayHour += 12
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[0]}, {thatDay.capitalize()} ({resultDay} days later)"
				
		elif startingDayOfTheWeek == False:
			if clockFormatStartTime == "AM":
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[1]} ({resultDay} days later)"
			elif clockFormatStartTime == "PM":
				if resultDayHour == 0:
					resultDayHour += 12
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[0]} ({resultDay} days later)"

	elif resultDay == 1:
		
		if startingDayOfTheWeek != False:
			if clockFormatStartTime == "AM":
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[0]}, {thatDay.capitalize()} (next day)"
			else:
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[0]} (next day)"
		elif startingDayOfTheWeek == False:
			if clockFormatStartTime == "AM":
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[0]} (next day)"
			else:
				new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[0]} (next day)"
	
	else:
		if resultDay == 0:
			if resultHour > 12:
				resultHour -= 12
				clockFormatStartTime = clockFormat[1]
				if startingDayOfTheWeek != False:
					new_time = f"{resultHour}:{sResultMinute} {clockFormatStartTime}, {startingDayOfTheWeek.capitalize()}"
				else:
					new_time = f"{resultHour}:{sResultMinute} {clockFormatStartTime}"
			elif resultHour == 12:
				if m > 60:
					if clockFormatStartTime == "AM":
						new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[1]}"
					else:
						new_time = f"{resultDayHour}:{sResultMinute} {clockFormat[0]}{startingDayOfTheWeek.capitalize()}"
			else:
				new_time = f"{resultHour}:{sResultMinute} {clockFormatStartTime}"
		else:
			new_time = f"{resultHour}:{sResultMinute} {clockFormatStartTime} {startingDayOfTheWeek.capitalize()}"
			
	return new_time
