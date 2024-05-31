# a fun riddle
# 1. What is the output of the following code?
# 2. Can you explain why?

def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3, [3, 2, 1])
f(3)
# 1. What is the output of the following code?
# 2. Can you explain why?

# Output:
