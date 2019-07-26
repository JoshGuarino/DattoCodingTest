import time
from classes import gateway, repeater
import threading


x = gateway.Gateway(22)

def download(time_amount):
    time.sleep(time_amount)

def upgrade(time_amount):
    time.sleep(time_amount)


def run(ap):
    t1 = threading.Thread(target = download, args=[ap.download_time])
    t2 = threading.Thread(target = upgrade, args=[ap.upgrade_time])
    while ap.upgrade_complete == False:
        if t1.is_alive() == False and t2.is_alive() == False:
            ap.check_in()
        if ap.download_firmware == True and ap.download_complete == False and ap.upgrade_complete == False and t1.is_alive() == False:
            t1.start()
        if ap.download_firmware == True and ap.download_complete == True and ap.upgrade_complete == False and t2.is_alive() == False:
            t2.start()
        if ap.upgrade_complete == True:
            break    
        time.sleep(5)


start = time.time()
run(x)
end = time.time()
print('total time - ', round(end-start, 2), 'mins')