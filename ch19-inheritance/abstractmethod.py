from abc import ABC ,abstractmethod
#abstract method
class animal(ABC):
	@abstractmethod
	def sound(self):
		pass
	def sleep(self):
		print("sleeping...")
#subclass implementing the abstract method
class dog(animal):
	def sound(self):
		print("bark")
class cat(animal):
	def sound(self):
		print("meow")
dog=dog()
dog.sound()
dog.sleep()
cat=cat()
cat.sound()

