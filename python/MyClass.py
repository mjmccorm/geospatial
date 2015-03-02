""" Summary of Program Function Goes Here """
__version__ = '1.0'

import logging

_log = logging.getLogger(__name__)

class MyClass(object):

	def __init__(self):
		_log.warning("Created")
		
	def myFunction(self):
		_log.warning("myFunction")
		
		
	