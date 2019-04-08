#Damani A.Philip


"""Request: Create a program that receives a string from the user and output the acronym of that string 
in all caps. For example, If you typed in “This is a test”, the output should be TIAT"""

#Introduction
print('Acronym Creator.\n')

#storage
acronym = []

def operation(sentence):
    sentence_storage = sentence.title().split()
    global acronym
    for x in sentence_storage:
        acronym.append(x[0][0])
    return


#Input
user_input = str(input('Please enter sentence:\n'))

#Secondary Process
operation(user_input)
final_process = "".join(acronym)
final_process2 = ".".join(acronym)

#output
print("The acronym of your input is \"{0}\", unless you prefer it punctuated, which would be \"{1}\".".format(final_process,final_process2))


