from django.db import models
from django.utils.encoding import python_2_unicode_compatible # only if you need to support Python 2
from .utils import create_shortcode

# Create your models here.
class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs = super (KirrURLManager, self).all(*args, **kwargs)
		qs = qs.filter(active=True)
		return qs

	def refresh_shortcodes(self):
		qs = KirrURL.objects.filter(id__gte=1) #gte == Greater then equals to 1 >
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			q.save()
			new_codes += 1
		return "New Codes made : {i}".format(i=new_codes)

@python_2_unicode_compatible  # only if you need to support Python 2
class KirrURL(models.Model):
	url 		= models.CharField(max_length=220, )
	shortcode 	= models.CharField(max_length= 15, unique=True, null=False, blank=True)
	updated		= models.DateTimeField(auto_now=True) #everytime the model is saved
	timestamp	= models.DateTimeField(auto_now_add=True) #when model was created
	active 		= models.BooleanField(default=True)
	#empty_datetime 	= models.DateTimeField(auto_now_add=False, auto_now=False) 
	#shortcode = models.CharField(max_length= 15, null=True, blank=False) Empty database is okay
	#shortcode = models.CharField(max_length= 15, default='somthing') default value
	objects = KirrURLManager() #If you add a custom manager to a model then the default manager at objects will not be created. Either add it yourself in the class definition, or stick with using the custom manager.
	#some_random = KirrURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode =="":
			self.shortcode = create_shortcode(self)
		super(KirrURL,self).save(*args, **kwargs)
		'''
		obj = self
		obj.shortcode = code_generator()
		obj.save()
		'''

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