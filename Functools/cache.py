from functools import cache 
import time 


def fib_without_cache(n): 
	if n < 2: 
		return n 
	return fib_without_cache(n-1) + fib_without_cache(n-2) 
	

begin = time.time() 
fib_without_cache(30) 
end = time.time() 

print("Time taken to execute the function without cache is", end - begin) 


@cache 
def fib_with_cache(n): 
	if n < 2: 
		return n 
	return fib_with_cache(n-1) + fib_with_cache(n-2) 
	
begin = time.time() 
fib_with_cache(30) 
end = time.time() 

print("Time taken to execute the function with cache is", end - begin) 
