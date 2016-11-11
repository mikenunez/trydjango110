import random
import string


def code_generator (size=6 ,chars=string.ascii_lowercase + string.digits):
	return  ''.join(random.choice(chars) for _ in range (size))
	'''
	new_code = ''
	for _ in range (size): # _ sirve para variable temp q no se va a usar
		new_code += randowm.choice(chars)
	return new_code
	'''