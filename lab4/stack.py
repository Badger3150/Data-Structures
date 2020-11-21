# Q3 - Stack
import queue

seq = "()()()((()))"


def Stack(seq):
    stack = queue.LifoQueue()
    length = len(seq)
    for i in range(length):
        if seq[i] == "(":
            stack.put("1")
        elif seq[i] == ")":
            if not stack.empty():
                stack.get()
            else:
                return False
    return stack.empty()

print(Stack(seq))
