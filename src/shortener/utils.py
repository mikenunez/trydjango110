import random
import string

#from shotener.models import KirrURL # data error porque importas algo q se importa a si mismo

def code_generator (size=6 ,chars=string.ascii_lowercase + string.digits):
	return  ''.join(random.choice(chars) for _ in range (size))
	'''
	new_code = ''
	for _ in range (size): # _ sirve para variable temp q no se va a usar
		new_code += randowm.choice(chars)
	return new_code
	'''

def create_shortcode (instance):
	new_code = code_generator()
	#print(instance) # get de instance name of the created class of model
	#print(instance.__class__)
	#print(instance.__class__.__name__)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode()
	return new_code