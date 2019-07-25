from classes import accesspoint

class Repeater(accesspoint.AccessPoint):
        def __init__(self, gateway_num):
            accesspoint.AccessPoint.__init__(self)
            self.gateway_pointer = gateway_num
