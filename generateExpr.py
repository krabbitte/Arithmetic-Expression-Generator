from random import randrange, random

if __name__ == "__main__":
	charCount = 0
	maxC = 200


def generateExpression():
	global charCount, maxC

	charCount = 0

	return expression(0.5, 0)


def expression(b, n):
	global charCount

	if charCount > maxC - 10:
		return number()

	outcome = random()

	if outcome < b:
		charCount += 1
		return binary()
	elif outcome >= b and outcome <= 1-n:
		charCount += 2
		return grouping()
	else:
		charCount += 1
		return number()


def grouping():
	return "(" + expression(1, 0) + ")"


def binary():
	return expression(0.25, 0.5) + operator() + expression(0.25, 0.5)


def operator():
	outcome = randrange(5)
	match outcome:
		case 0: return "^"
		case 1: return "*"
		case 2: return "/"
		case 3: return "+"
		case 4: return "-"
		case _: return "error"


def number():
	return str(randrange(9) + 1)

print(generateExpression() + "\n")