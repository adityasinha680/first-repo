def list_output(l1,l2):
	l1.reverse()
	l2.reverse()
	element1 = int("".join(map(str, l1)))
	element2 = int("".join(map(str, l2)))
	output = str(element1+element2)
	output_list = [int(x) for x in str(output)]
	output_list.reverse()
	return 

list_output([9,9,9,9,9,9,9],[9,9,9,9])



def squareroot(num):
	output = "{:.2f}".format(num**0.5)
	return output

print(squareroot(8))
