import random
import time

class AccessPoint:
    def __init__(self):
        self.check_in_offset =  round(random.uniform(0, 5), 2)
        self.download_time =  round(random.uniform(0, 5), 2)
        self.upgrade_time =  round(random.uniform(0, 5), 2)
        self.download_firmware = False
        self.download_complete = False
        self.upgrade_complete = False
    
    def upgrade(self):
        time.sleep(self.upgrade_time)

    def download(self):
        time.sleep(self.download_time)

    def check_in(self):
        if self.download_firmware==False and self.download_complete==False and self.upgrade_complete==False:
            time.sleep(self.check_in_offset)
            self.download_firmware = True
            print('download started', self.check_in_offset)
        elif self.download_firmware==True and self.download_complete==False and self.upgrade_complete==False:
            self.download_complete = True
            print('download complete', self.download_time)
        elif self.download_firmware==True and self.download_complete==True and self.upgrade_complete==False:
            self.upgrade_complete = True
            print('upgrade complete', self.upgrade_time)