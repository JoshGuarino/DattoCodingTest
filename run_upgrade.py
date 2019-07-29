import time
from classes import gateway, repeater
import threading
import global_vars

def download(time_amount):
    time.sleep(time_amount)

def upgrade(time_amount):
    time.sleep(time_amount)

def run(ap):
    t1 = threading.Thread(target = download, args=[ap.download_time])
    t2 = threading.Thread(target = upgrade, args=[ap.upgrade_time])
    if ap.AP_type == 'repeater':
        gw = global_vars.network_arr[ap.gw_pointer]
    while ap.upgrade_complete == False:
        if ap.AP_type == 'repeater':
            if t1.is_alive()==False and t2.is_alive()==False:
                if gw.download_firmware==True and gw.download_complete==True and gw.upgrade_complete==False:
                   continue 
                ap.check_in()
            if ap.download_firmware==True and ap.download_complete==False and ap.upgrade_complete == False and t1.is_alive() == False:
                t1.start()
            if ap.download_firmware==True and ap.download_complete==True and ap.upgrade_complete==False and t2.is_alive()==False:
                t2.start()
            if ap.upgrade_complete==True:
                break    
            time.sleep(5)
        else:
            if t1.is_alive()==False and t2.is_alive()==False:
                ap.check_in()
            if ap.download_firmware==True and ap.download_complete==False and ap.upgrade_complete==False and t1.is_alive()==False:
                t1.start()
            if ap.download_firmware==True and ap.download_complete==True and ap.upgrade_complete==False and t2.is_alive()==False:
                t2.start()
            if ap.upgrade_complete==True:
                break    
            time.sleep(5)
