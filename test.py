from collections import deque

a = deque()
a.append((1, 1, 3))
a.append((2,3,0))
a.append((1,deque(),30))
a.append((0, [], -4))
a.append((1, [], 3))

s = sorted(a, key = lambda x: x[0])

a = deque(s)

print(a)