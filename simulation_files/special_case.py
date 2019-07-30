from simulation_files import run_upgrade, global_vars
from classes import gateway, repeater
import time
import threading

def populate_counters(AP, index, upgrade_not_started, downloading, upgrading, complete):
    if AP.download_firmware==False and AP.download_complete==False and AP.upgrade_complete==False:
        upgrade_not_started[index] = upgrade_not_started[index]+1
    elif AP.download_firmware==True and AP.download_complete==False and AP.upgrade_complete==False:
        downloading[index] = downloading[index]+1
    elif AP.download_firmware==True and AP.download_complete==True and AP.upgrade_complete==False:
        upgrading[index] = upgrading[index]+1
    elif AP.download_firmware==True and AP.download_complete==True and AP.upgrade_complete==True:
        complete[index] = complete[index]+1

def _8_min_mark(the_thread, AP, start, upgrade_not_started, downloading, upgrading, complete):
    alive = True 
    while alive:
        end = time.perf_counter()
        total = end-start
        if total >= 8:
            if AP.AP_type == 'gateway':
                populate_counters(AP, 0, upgrade_not_started, downloading, upgrading, complete)
            elif AP.AP_type == 'repeater':
                populate_counters(AP, 1, upgrade_not_started, downloading, upgrading, complete)
            alive = False

def run_test(gw, rp, off):
    global_vars.num_of_gates = gw
    global_vars.repeat_per_gate = rp
    global_vars.offest = off

    upgrade_not_started = [0,0]
    downloading = [0,0]
    upgrading = [0,0]
    complete = [0,0]

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
        _8_min_mark(global_vars.thread_arr[i], global_vars.network_arr[i], start, upgrade_not_started, downloading, upgrading, complete)
        for j in range(global_vars.repeat_per_gate):
            _8_min_mark(global_vars.network_arr[i].repeat_threads[j], global_vars.network_arr[i].repeaters[j], start, upgrade_not_started, downloading, upgrading, complete)

    #<-end the clock->
    end = time.perf_counter()
    #<-end the clock->

    total = end-start

    global_vars.num_of_gates = gw
    global_vars.repeat_per_gate = rp
    global_vars.offest = off
    global_vars.network_arr = []
    global_vars.thread_arr = []

    return upgrade_not_started, downloading, upgrading, complete
