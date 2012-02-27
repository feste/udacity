t1 = 'all zip files are zipped'
t2 = 'all zip files are compressed'
t3 = ''
t4 = 'apple'
t5 = 'zip'

def eight(text):
	zip1 = text.find('zip')
	print text.find('zip', zip1 + 1)
	
eight(t1)
eight(t2)
eight(t3)
eight(t4)
eight(t5)
