def find_max_min(ArrayValues):
	Result = []
	if isinstance(ArrayValues, list) == True:
		ArrayValues.sort()	
		minValue = ArrayValues[0]
		maxValue = ArrayValues[-1]
            
        Result.append(minValue)

		if ArrayValues[-1] == minValue:
		return Result

		else:
		Result.append(maxValue)
		return Result
	else:
		raise TypeError('Parameter provided is not a list')
