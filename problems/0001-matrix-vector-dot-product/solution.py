import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	arr_a = np.array(a)
	arr_b = np.array(b)

	if any(len(row) != len(arr_b) for row in arr_a):
		return -1
	
	return (arr_a @ arr_b).tolist()