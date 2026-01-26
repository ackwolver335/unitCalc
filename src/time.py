# here is another python module containing time convertions units
# the units that would work on this are written as follow
# Year, Weeks, Days, hour, min, sec, millisec, microsec, picosec

class year:
    year = 0

    def __init__(self):
        pass

    def yr2month(self,yr):
        self.year = yr * 12
        return self.year

    def yr2wk(self,yr):
        self.year = yr * 52
        return self.year

    def yr2days(self,yr):
        self.year = yr * 365
        return self.year

    def yr2h(self,yr):
        self.year = yr * 8760
        return self.year

    def yr2min(self,yr):
        self.year = yr * 525600
        return self.year

    def yr2sec(self,yr):
        self.year = yr * 31536000
        return self.year

    def yr2millsec(self,yr):
        self.year = yr * (3.1536 * (10 ** 10))
        return self.year

    def yr2microsec(self,yr):
        self.year = yr * (3.1536 * (10 ** 13))
        return self.year

    def yr2picosec(self,yr):
        self.year = yr * (3.1536 * (10 ** 19))
        return self.year

class week:
    week = 0

    def __init__(self):
        pass

    def wk2yr(self,wk):
        self.week = wk / 52
        return self.week

    def wk2month(self,wk):
        self.week = wk / 4
        return self.week

    def wk2days(self,wk):
        self.week = wk * 7
        return self.week

    def wk2h(self,wk):
        self.week = wk * 168
        return self.week

    def wk2min(self,wk):
        self.week = wk * 10080
        return self.week

    def wk2sec(self,wk):
        self.week = wk * 604800
        return self.week

    def wk2millsec(self,wk):
        self.week = wk * (6048 * (10 ** 5))
        return self.week

    def wk2microsec(self,wk):
        self.week = wk * (6.048 * (10 ** 11))
        return self.week

    def wk2picosec(self,wk):
        self.week = wk * (6.048 * (10 ** 17))
        return self.week

class days:
    days = 0

    def __init__(self):
        pass

    def dy2yr(self,dys):
        self.days = dys / 365
        return self.days

    def dy2month(self,dys):
        self.days = dys / 30
        return self.days

    def dy2wk(self,dys):
        self.days = dys / 7
        return self.days

    def dy2h(self,dys):
        self.days = dys * 24
        return self.days

    def dy2min(self,dys):
        self.days = dys * 1440
        return self.days

    def dy2sec(self,dys):
        self.days = dys * 86400
        return self.days

    def dy2millsec(self,dys):
        self.days = dys * (864 * (10 ** 5))
        return self.days

    def dy2microsec(self,dys):
        self.days = dys * (8.64 * (10 ** 10))
        return self.days

    def dy2picosec(self,dys):
        self.days = dys * (8.64 * (10 ** 16))
        return self.days

class hour:
    hour = 0

    def __init__ (self):
        pass
    
    def h2yr(self,hrs):
        self.hour = hrs / 8760
        return self.hour

    def h2month(self,hrs):
        self.hour = hrs / (24 * 30)
        return self.hour

    def h2wk(self,hrs):
        self.hour = hrs / 168
        return self.hour

    def h2days(self,hrs):
        self.hour = hrs / 24
        return self.hour

    def h2min(self,hrs):
        self.hour = hrs * 60
        return self.hour

    def h2sec(self,hrs):
        self.hour = hrs * 3600
        return self.hour

    def h2millsec(self,hrs):
        self.hour = hrs * (36 * (10 ** 5))
        return self.hour

    def h2microsec(self,hrs):
        self.hour = hrs * (3.6 * (10 ** 9))
        return self.hour

    def h2picosec(self,hrs):
        self.hour = hrs * (3.6 * (10 ** 15))
        return self.hour

class minute:
    minute = 0

    def __init__(self):
        pass

    def min2yr(self,min):
        self.minute = min / 525600
        return self.minute

    def min2month(self,min):
        self.minute = min / (60 * 24 * (30))
        return self.minute

    def min2wk(self,min):
        self.minute = min / 10080
        return self.minute

    def min2days(self,min):
        self.minute = min / 1440
        return self.minute

    def min2h(self,min):
        self.minute = min / 60
        return self.minute

    def min2sec(self,min):
        self.minute = min * 60
        return self.minute 

    def min2millsec(self,min):
        self.minute = min * 60000
        return self.minute

    def min2microsec(self,min):
        self.minute = min * (60 * (10 ** 6))
        return self.minute

    def min2picosec(self,min):
        self.minute = min * (60 * (10 ** 11))
        return self.minute

class second:
    seconds = 0

    def __init__(self):
        pass

    def sec2yr(self,scds):
        self.seconds = scds / 31536000
        return self.seconds

    def sec2wk(self,scds):
        self.seconds = scds / 604800
        return self.seconds

    def sec2days(self,scds):
        self.seconds = scds / 86400
        return self.seconds

    def sec2hour(self,scds):
        self.seconds = scds / 3600
        return self.seconds

    def sec2min(self,scds):
        self.seconds = scds / 60
        return self.seconds
    
    def sec2millsec(self,scds):
        self.seconds = scds * 1000
        return self.seconds

    def sec2micorsec(self,scds):
        self.seconds = scds * (10 ** 6)
        return self.seconds

    def sec2picosec(self,scds):
        self.seconds = scds * (10 ** 12)
        return self.seconds

class millisec:
    millisec = 0

    def __init__(self):
        pass

    def milsec2yr(self,millsec):
        self.millisec = millsec / (3.1536 * (10 ** 10))
        return self.millisec

    def milsec2wk(self,millsec):
        self.millisec = millsec / (6048 * (10 ** 5))
        return self.millisec

    def milsec2days(self,millsec):
        self.millisec = millsec / (864 * (10 ** 5))
        return self.millisec

    def milsec2hr(self,millsec):
        self.millisec = millsec / (36 * (10 ** 5))
        return self.millisec

    def milsec2min(self,millsec):
        self.millisec = millsec / 60000
        return self.millisec

    def milsec2sec(self,millsec):
        self.millisec = millsec / 1000
        return self.millisec

    def milsec2microsec(self,millsec):
        self.millisec = millsec * 1000
        return self.millisec

    def milsec2picosec(self,millsec):
        self.millisec = millsec * (10 ** 9)
        return self.millisec

class microsec:
    microsec = 0

    def __init__(self):
        pass

    def usec2yr(self,mcrsec):
        self.microsec = mcrsec / (3.1536 * (10 ** 13))
        return self.microsec

    def usec2wk(self,mcrsec):
        self.microsec = mcrsec / (6.048 * (10 ** 11))
        return self.microsec

    def usec2days(self,mcrsec):
        self.microsec = mcrsec / (8.64 * (10 ** 10))
        return self.microsec

    def usec2hr(self,mcrsec):
        self.microsec = mcrsec / (3.6 * (10 ** 9))
        return self.microsec

    def usec2min(self,mcrsec):
        self.microsec = mcrsec / (6 * (10 ** 7))
        return self.microsec

    def usec2sec(self,mcrsec):
        self.microsec = mcrsec / (10 ** 6)
        return self.microsec

    def usec2millisec(self,mcrsec):
        self.microsec = mcrsec / 1000
        return self.microsec

    def usec2picosec(self,mcrsec):
        self.microsec = mcrsec * (10 ** 6)
        return self.microsec

class picosec:
    picosec = 0

    def __init__(self):
        pass

    def pcsec2yr(self,psec):
        self.picosec = psec / (3.1536 * (10 ** 19))
        return self.picosec
    
    def pcsec2wk(self,psec):
        self.picosec = psec / (6.048 * (10 ** 17))
        return self.picosec

    def pcsec2day(self,psec):
        self.picosec = psec / (8.64 * (10 ** 16))
        return self.picosec

    def pcsec2hr(self,psec):
        self.picosec = psec / (3.6 * (10 ** 15))
        return self.picosec

    def pcsec2min(self,psec):
        self.picosec = psec / (6 * (10 ** 13))
        return self.picosec
    
    def pcsec2sec(self,psec):
        self.picosec = psec / (10 ** 12)
        return self.picosec

    def pcsec2millisec(self,psec):
        self.picosec = psec / (10 ** 9)
        return self.picosec

    def pcsec2microsec(self,psec):
        self.picosec = psec / (10 ** 6)
        return self.picosec