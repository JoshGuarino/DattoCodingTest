from simulation_files import run_upgrade, global_vars
from classes import gateway, repeater
import time
import threading

def thread_alive(the_thread):
    alive = True 
    while alive:
        if the_thread.is_alive() == False:
            alive = False


def run_test(gw, rp, off):
    global_vars.num_of_gates = gw
    global_vars.repeat_per_gate = rp
    global_vars.offest = off

    for i in range(global_vars.num_of_gates):    
        global_vars.network_arr.append(gateway.Gateway(str(i+1), 'gateway'))
        global_vars.thread_arr.append(threading.Thread(target=run_upgrade.run, args=[global_vars.network_arr[i]]))
        for j in range(global_vars.repeat_per_gate):
            global_vars.network_arr[i].repeaters.append(repeater.Repeater(str(i+1), 'repeater', str(j+1)))
            global_vars.network_arr[i].repeat_threads.append(threading.Thread(target=run_upgrade.run, args=[global_vars.network_arr[i].repeaters[j]]))

    #<-start the clock->
    start = time.perf_counter()
    #<-start the clock->

    for i in range(global_vars.num_of_gates):
        global_vars.thread_arr[i].start()
        for j in global_vars.network_arr[i].repeat_threads:
            j.start()

    for i in range(global_vars.num_of_gates):
        thread_alive(global_vars.thread_arr[i])
        for j in range(global_vars.repeat_per_gate):
            thread_alive(global_vars.network_arr[i].repeat_threads[j])

    #<-end the clock->
    end = time.perf_counter()
    #<-end the clock->

    total = end-start

    global_vars.num_of_gates = gw
    global_vars.repeat_per_gate = rp
    global_vars.offest = off
    global_vars.network_arr = []
    global_vars.thread_arr = []

    return total