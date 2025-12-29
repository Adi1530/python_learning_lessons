import random
import time

import memory_profiler
from memory_profiler import profile
names=["Adi","Ram","Tom","Bradley","Tamil","Anbu","Arasan"]
major=["ECE","CSE","IT","CSBS","MECT","CIVIL"]

print("Memory (Initial) : {}Mb".format(memory_profiler.memory_usage()))

def people_list(end):
    result=list()
    for i in range(end):
        person={
            "id":i ,
            "name" : random.choice(names) ,
            "major" : random.choice(major)
        }
        result.append(person)
    return result

def people_generator(end):

    for i in range(end):
        person={
            "id":i ,
            "name" : random.choice(names) ,
            "major" : random.choice(major)
        }
        yield person


'''t1=time.perf_counter()
cpu=time.process_time()
people=people_list(1000000)
t2=time.perf_counter()
cpu_post_exec=time.process_time()'''

t1=time.perf_counter()
cpu=time.process_time()
people=people_generator(1000000)
t2=time.perf_counter()
cpu_post_exec=time.process_time()

#generated_list=list(people)

print("Memory (Final) : {}Mb".format(memory_profiler.memory_usage()))
print(f"Time taken for execution : {t2-t1}")
print(f"{cpu}")
print(f"{cpu_post_exec}")


'''
    perfcounter function --> to measure high resolution wall clock time
    processtime function --> to measure cpu time only used by the current process
    memory_profiler.memory_usage function --> to measure RAM usage of the code
'''
