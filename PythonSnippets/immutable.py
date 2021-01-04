counters = {"func_calls": 0}
def bar():
    counters["func_calls"] +=1

def foo():
    counters["func_calls"] +=1
    bar()

foo()
print(counters["func_calls"])