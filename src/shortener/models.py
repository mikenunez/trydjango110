from django.db import models
from django.utils.encoding import python_2_unicode_compatible # only if you need to support Python 2
import random


def code_generator (size=6 ,chars='abcdefghijklmnopqrstuvwxyz'):
	return  ''.join(random.choice(chars) for _ in range (size))
	'''
	new_code = ''
	for _ in range (size): # _ sirve para variable temp q no se va a usar
		new_code += randowm.choice(chars)
	return new_code
	'''

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class KirrURL(models.Model):
	url 		= models.CharField(max_length=220, )
	shortcode 	= models.CharField(max_length= 15, unique=True, null=False, blank=False)
	updated		= models.DateTimeField(auto_now=True) #everytime the model is saved
	timestamp	= models.DateTimeField(auto_now_add=True) #when model was created
	#empty_datetime 	= models.DateTimeField(auto_now_add=False, auto_now=False) 
	#shortcode = models.CharField(max_length= 15, null=True, blank=False) Empty database is okay
	#shortcode = models.CharField(max_length= 15, default='somthing') default value

	def save(self, *args, **kwargs):
		print('something')
		self.shortcode = code_generator()
		super(KirrURL,self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

''' Python 2 support
	def __unicode__(self):
		return str(self.url)
	"""docstring for Kirr
	def __init__(self, arg):
		super(Kirr, self).__init__()
		self.arg = arg
	"""


Python manage.py makemigrations
Python manage.py migrate
'''
