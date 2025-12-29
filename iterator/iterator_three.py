class Sentence:
	def __init__(self,sentence):
		self.sentence=sentence
		self.index=0
		self.words=self.sentence.split()
	def __iter__(self):
		return self
	def __next__(self):
		if self.index>=len(self.words):
			raise StopIteration
			#break
		current_word=self.words[self.index]
		self.index+=1
		return current_word

sen=Sentence("Hi i am chandraaditya currently a intern at zoho")
iter_sen=iter(sen)
print(next(iter_sen))
print(next(iter_sen))


#for s in sen:
#	print(s)
