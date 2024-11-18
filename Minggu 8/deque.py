from collections import deque

q = deque([20,30,30,40])
q.appendleft(67)
q.append(1)
print(q)
q.pop()
q.popleft()
print(q)