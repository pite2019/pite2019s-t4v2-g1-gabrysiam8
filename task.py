from flight import Flight

if __name__=='__main__':
	my_flight = Flight()
	for orientation in my_flight.fly():
		print(orientation)