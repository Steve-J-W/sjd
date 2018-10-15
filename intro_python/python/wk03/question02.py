# Ask Question from data Dictionary (hash)
data = {"Q": "Is it an aquatic animal"}

# A simple Y/N validation function
# q_text = Question text
# Get question from data

def get_answer (question):
    gotanswer = False
    while gotanswer == False:
        x = str(input(question + '? [Y/N]: ')) 
        if x.upper() == 'Y':
            return True
            gotanswer = True
        elif x.upper() == 'N':
            return False
            gotanswer = True



# Ask question and define result
if get_answer(data['Q']):
    print('YES')
else:
    print('No')