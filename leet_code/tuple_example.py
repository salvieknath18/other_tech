A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

set1 = {}
set2 = {}

for a in A:
	for b in B:
		r = a + b
		if r not in set1:
			set1[r] = 0
		set1[r] = set1[r] + 1
		
for c in C:
	for d in D:
		r = c + d
		if r not in set2:
			set2[r] = 0
		set2[r] = set2[r] + 1
        
print(set1)
print(set2)
result = 0
		
for elem in set1:
		if -elem in set2:
			result = result + (set1[elem] * set2[-elem])
	return result

print(result)


