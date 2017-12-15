import gc

class Station():
	"""docstring for ClassName"""

	def __init__(self,name,label,importance,location,neighbours):
		self.name = name
		self.label = label
		self.importance = importance
		self.location = location
		self.neighbours = neighbours

		# super(ClassName, self).__init__()
		# self.arg = arg

	def information(self):
		return '{} {} {} {}'.format(self.name, self.label, self.importance, self.location, self.neighbours)

	def update_single(self,name,prefix):
		""" update the label to the given label"""
		full_name= self.label
		short_name= full_name.replace(name,'')
		new_label= prefix+short_name
		self.label = new_label

	def reset_label(self):
		full_name= self.name
		self.label = full_name





		#[(obj.name,n[0],n[1]) for obj in gc.get_objects() if isinstance(obj, st.Station) for n in obj.neighbours]




