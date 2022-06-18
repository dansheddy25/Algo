def findMin(V, deno):
	divRes = 0
	ans = []

	for element in sorted(deno, key=int, reverse=True):
		# Find denominations
		if (V >= element):
			divRes = (V // element)
			ans.append(divRes)
			V = V % element
		else :
			ans.append(0)

	return (ans)
		

resl = findMin(57,[1,20,5,2])
for i in range(len(resl)):
    print(resl[i], end=" ")





    