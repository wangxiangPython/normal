import queue

q = queue.Queue(2)
list1 = [1,2]
q.put(list1)
q.put(list1)

print(q.get())
print(q.get())