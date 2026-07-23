class time:
	def __init__(self,hour=0,minutes=0,second=0):
		self.hour=hour
		self.minutes=minutes
		self.second=second
		self.normalization_time()  #ensure time is in proper format
	def normalization_time(self):
#normalizes time so second <60 and minutes <60
		self.minutes+=self.second//60
		self.second%=60
		self.hour+=self.minutes//60
		self.minutes%=60
	def __add__(self,other):
#overloads the +operator to add two time objects
		if isinstance(other,time):   #isinstance is for to check give no are both same type or not (both int or not)
			return time( 
				self.hour+other.hour,
				self.minutes+other.minutes,
				self.second+other.second)
		raise TypeError("unsupported type for addition with time object")
	def __str__(self):
		return f"{self.hour:02d}:{self.minutes:02d}:{self.second:02d}"
#example usage
time1=time(1,45,50) #1hr 45 min 50second 
time2=time(2,30,40)
total_time=time1+time2  #time1.__add__(time2)
print("time1:",time1)
print("time2:",time2)
print("tital time=",total_time)
