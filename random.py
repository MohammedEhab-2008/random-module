from os import urandom

class random_me:

	def randint(start, end):
			
		if start > end:
			
			plus = start
			
			start = end
			
			end = plus
			
		plus = 0
			
		state = ""
			
		if start < 0 and end < 0:
			
			start = abs(start)
			
			end = abs(end)
			
			state = "--"
			
		if start < 0 and end >= 0:
			
			start_val = start
			
			start = 0
			
			state = "-"
	
		rand_var = urandom(1)
		
		check = rand_var
		
		if start > end:
			
			plus = start
			
			start = end
			
			end = plus
		
		rand_var = int.from_bytes(rand_var, byteorder='big')
		
		rand_var = (rand_var ** 33.71789865443456777627) * 2.345566775332716267
		
		result = 0
		
		if state == "-":
			
			result = rand_var % abs(end + 1)
			
		else:
		
			result = rand_var % (end + 1)
		
		if result < abs(start):
			
			if result > 1000:
				
				while result < abs(start):
					
					result += 1000
				
			else:
				
				while result < abs(start):
				
					result += 1
					
		if state == "--":
				
			return int(-abs(result))
				
		elif state == "-":
				
			if int(-abs(result)) >= -abs(start_val) and check % 2 == 0:
					
				return int(-abs(result))
					
			else:
					
				return int(abs(result))
		
		return int(result)