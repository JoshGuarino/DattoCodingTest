import run_upgrade
from classes import gateway, repeater
import time
import threading
import global_vars

num_of_gates = global_vars.num_of_gates
repeat_per_gate = global_vars.repeat_per_gate

def thread_alive(the_thread):
    alive = True 
    while alive:
        if the_thread.is_alive() == False:
            alive = False


for i in range(num_of_gates):    
    global_vars.network_arr.append(gateway.Gateway(str(i+1), 'gateway'))
    global_vars.thread_arr.append(threading.Thread(target=run_upgrade.run, args=[global_vars.network_arr[i]]))
    for j in range(repeat_per_gate):
        global_vars.network_arr[i].repeaters.append(repeater.Repeater(str(i+1), 'repeater', str(j+1)))
        global_vars.network_arr[i].repeat_threads.append(threading.Thread(target=run_upgrade.run, args=[global_vars.network_arr[i].repeaters[j]]))


#<-start the clock->
start = time.perf_counter()
#<-start the clock->

for i in range(num_of_gates):
    global_vars.thread_arr[i].start()
    for j in global_vars.network_arr[i].repeat_threads:
        j.start()

for i in range(num_of_gates):
    thread_alive(global_vars.thread_arr[i])
    for j in range(repeat_per_gate):
        thread_alive(global_vars.network_arr[i].repeat_threads[j])

#<-end the clock->
end = time.perf_counter()
#<-end the clock->

print('total time - ', round(end-start, 2), 'mins')
