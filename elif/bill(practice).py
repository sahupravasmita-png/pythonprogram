unit=int(input("enter total electricity units consumed"))
bill=0
if unit<=100:
	bill=unit*1.5
elif unit<=200:
	bill=(100*1.5)+(unit-100)*2.5
elif unit<=300:
	bill=(100*1.5)+(100*2.5)+(unit-200)*4.0
else:
	bill=(100*1.5)+(100*2.5)+(100*4.0)+(unit-300)*6.0
print("total bill=",round(bill,2))
