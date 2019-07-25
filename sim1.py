import time
from classes import gateway, repeater

ap = gateway.Gateway(22)


start = time.time()

ap.check_in_1()
ap.check_in_2()
ap.check_in_3()

end = time.time()
total_time = end - start
print('total time - ', round(total_time, 2))