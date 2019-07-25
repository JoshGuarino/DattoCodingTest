from classes import accesspoint

class Gateway(accesspoint.AccessPoint):
    def __init__(self, ident):
        accesspoint.AccessPoint.__init__(self)
        self.ident_num = ident