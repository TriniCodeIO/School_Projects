
def process(words):
	list_1 = words.title().split()
	list_1.sort()
	return (list_1)



#Input
statement = str(input('Please enter the statement that needs to rearranged:\n'))

#Optional(Not necessary)
storage = process(statement)

#Output
print('The statement has been rearranged in alphabetical order:\n%s' % ("\n".join(storage)))