import random
import time

class AccessPoint:
    def __init__(self):
        self.check_in_time =  round(random.uniform(0, 5), 2)
        self.download_time =  round(random.uniform(0, 5), 2)
        self.upgrade_time =  round(random.uniform(0, 5), 2)
        self.download_firmware = False
        self.download_complete = False
        self.upgrade_complete = False

    def check_in_1(self):
        time.sleep(self.check_in_time)
        self.download_firmware = True
        print('download started - ', self.check_in_time, self.download_firmware)

    def check_in_2(self):
        time.sleep(self.download_time)
        self.download_complete = True
        print('download complete, upgrade started - ', self.download_time, self.download_complete)

    def check_in_3(self):
        time.sleep(self.upgrade_time)
        self.upgrade_complete = True
        print('upgrade complete - ', self.upgrade_time, self.upgrade_complete)