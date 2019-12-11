import time
from ipyparallel.serialize import pack_apply_message
import dill
import inspect 
from test_functions import *

# FUNCTION 1
print("Function 1")
begin = time.time()
for i in range(100):
    pack_apply_message(func1, args1, kwargs1, buffer_threshold=1024*1024, item_threshold=1024)
end = time.time()
print("Ipyparallel.Serialize: {:2f}".format((end - begin) / 100))

begin = time.time()
for i in range(100):
    dill.dumps(func1)
end = time.time()
print("Dill: {:2f}".format((end - begin) / 100))

begin = time.time()
for i in range(100):
    inspect.getsource(func1)
end = time.time()
print("Inspect: {:2f}".format((end - begin) / 100))
print()

# FUNCTION 2
print("Function 2")
begin = time.time()
for i in range(100):
    pack_apply_message(func2, args2, kwargs2, buffer_threshold=1024*1024, item_threshold=1024)
end = time.time()
print("Ipyparallel.Serialize: {:2f}".format((end - begin) / 100))

begin = time.time()
for i in range(100):
    dill.dumps(func2)
end = time.time()
print("Dill: {:2f}".format((end - begin) / 100))

begin = time.time()
for i in range(100):
    inspect.getsource(func2)
end = time.time()
print("Inspect: {:2f}".format((end - begin) / 100))
print()

# FUNCTION 3
print("Function 3")
begin = time.time()
for i in range(100):
    pack_apply_message(func3, args3, kwargs3, buffer_threshold=1024*1024, item_threshold=1024)
end = time.time()
print("Ipyparallel.Serialize: {:2f}".format((end - begin) / 100))

begin = time.time()
for i in range(100):
    dill.dumps(func3)
end = time.time()
print("Dill: {:2f}".format((end - begin) / 100))

begin = time.time()
for i in range(100):
    inspect.getsource(func3)
end = time.time()
print("Inspect: {:2f}".format((end - begin) / 100))
