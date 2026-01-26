# Here is another Library of Python which contains the conversion of Volume's units
# The units used in this one are as follow
# mtr3, dm3, cm3, mm3, hl, ltr, dcltr, cntltr, mlltr, ft3, inch3, yd3, af3

class metre3:
    meter_cub = 0

    def __init__(self):
        pass

    def mcub2dmcub(self,m3):
        self.meter_cub = m3 * 1000
        return self.meter_cub

    def mcub2cmcub(self,m3):
        self.meter_cub = m3 * (10 ** 6)
        return self.meter_cub

    def mcub2mmcub(self,m3):
        self.meter_cub = m3 * (10 ** 9)
        return self.meter_cub

    def mcub2hctl(self,m3):
        self.meter_cub = m3 * 10
        return self.meter_cub

    def mcub2ltr(self,m3):
        self.meter_cub = m3 * 1000
        return self.meter_cub

    def mcub2dcltr(self,m3):
        self.meter_cub = m3 * (10 ** 4)
        return self.meter_cub

    def mcub2mltr(self,m3):
        self.meter_cub = m3 * (10 ** 6)
        return self.meter_cub

    def mcub2ft3(self,m3):
        self.meter_cub = m3 * 35
        return self.meter_cub

    def mcub2inch3(self,m3):
        self.meter_cub = m3 * 61023
        return self.meter_cub

    def mcub2yd3(self,m3):
        self.meter_cub = m3 * 1.307
        return self.meter_cub

    def mcub2af3(self,m3):
        self.meter_cub = m3 / 1234
        return self.meter_cub

class decimtr3:
    decimtr3 = 0

    def __init__(self,dcm3):
        pass

    def decimcub2mtr3(self,dcm3):
        self.decimtr3 = dcm3 / 1000
        return self.decimtr3

    def decimcub2cm3(self,dcm3):
        self.decimtr3 = dcm3 * 1000
        return self.decimtr3

    def decimcub2mm3(self,dcm3):
        self.decimtr3 = dcm3 * (10 ** 6)
        return self.decimtr3

    def decimcub2hl(self,dcm3):
        self.decimtr3 = dcm3 / 100
        return self.decimtr3

    def decimcub2l(self,dcm3):
        self.decimtr3 = dcm3 * 1
        return self.decimtr3

    def decimcub2dl(self,dcm3):
        self.decimtr3 = dcm3 * 10
        return self.decimtr3

    def decimcub2cl(self,dcm3):
        self.decimtr3 = dcm3 * 100
        return self.decimtr3

    def decimcub2ml(self,dcm3):
        self.decimtr3 = dcm3 * 1000
        return self.decimtr3

    def decimcub2ft3(self,dcm3):
        self.decimtr3 = dcm3 / 28
        return self.decimtr3

    def decimcub2inch3(self,dcm3):
        self.decimtr3 = dcm3 * 61
        return self.decimtr3

    def decimcub2yd3(self,dcm3):
        self.decimtr3 = dcm3 / 764
        return self.decimtr3

    def decimcub2af3(self,dcm3):
        self.decimtr3 = dcm3 / 1234000
        return self.decimtr3

class centimtr3:
    centimtr3 = 0

    def __init__(self):
        pass

    def cmcub2m3(self,cm3):
        self.centimtr3 = cm3 / (10 ** 6)
        return self.centimtr3

    def cmcub2dm3(self,cm3):
        self.centimtr3 = cm3 / 1000
        return self.centimtr3

    def cmcub2mm3(self,cm3):
        self.centimtr3 = cm3 * 1000
        return self.centimtr3

    def cmcub2hl(self,cm3):
        self.centimtr3 = cm3 / (10 ** 5)
        return self.centimtr3

    def cmcub2l(self,cm3):
        self.centimtr3 = cm3 / 1000
        return self.centimtr3

    def cmcub2dl(self,cm3):
        self.centimtr3 = cm3 / 100
        return self.centimtr3

    def cmcub2cl(self,cm3):
        self.centimtr3 = cm3 / 10
        return self.centimtr3

    def cmcub2ml(self,cm3):
        self.centimtr3 = cm3 * 1
        return self.centimtr3

    def cmcub2ft3(self,cm3):
        self.centimtr3 = cm3 / 28316
        return self.centimtr3

    def cmcub2inch3(self,cm3):
        self.centimtr3 = cm3 / 16
        return self.centimtr3

    def cmcub2yd3(self,cm3):
        self.centimtr3 = cm3 / 764554
        return self.centimtr3

    def cmcub2af3(self,cm3):
        self.centimtr3 = cm3 / (1.234 * (10 ** 9))
        return self.centimtr3

class millimtr3:
    millimtr3 = 0

    def __init__(self):
        pass

    def mmcub2m3(self,mm3):
        self.millimtr3 = mm3 / (10 ** 9)
        return self.millimtr3
    
    def mmcub2dm3(self,mm3):
        self.millimtr3 = mm3 / (10 ** 6)
        return self.millimtr3

    def mmcub2cm3(self,mm3):
        self.millimtr3 = mm3 / 1000
        return self.millimtr3
        
    def mmcub2hl(self,mm3):
        self.millimtr3 = mm3 / (10 ** 8)
        return self.millimtr3

    def mmcub2l(self,mm3):
        self.millimtr3 = mm3 / (10 ** 6)
        return self.millimtr3

    def mmcub2dl(self,mm3):
        self.millimtr3 = mm3 / (10 ** 5)
        return self.millimtr3

    def mmcub2cl(self,mm3):
        self.millimtr3 = mm3 / (10 ** 4)
        return self.millimtr3

    def mmcub2ml(self,mm3):
        self.millimtr3 = mm3 / 1000
        return self.millimtr3

    def mmcub2ft3(self,mm3):
        self.millimtr3 = mm3 / 28316846
        return self.millimtr3

    def mmcub2inch3(self,mm3):
        self.millimtr3 = mm3 / 16387
        return self.millimtr3

    def mmcub2yd3(self,mm3):
        self.millimtr3 = mm3 / 764554858
        return self.millimtr3

    def mmcub2af3(self,mm3):
        self.millimtr3 = mm3 / (1234 * (10 ** 12))
        return self.millimtr3

class hectltr:
    hectltr = 0

    def __init__(self):
        pass

    def hltr2m3(self,hctl):
        self.hectltr = hctl / 10
        return self.hectltr

    def hltr2dm3(self,hctl):
        self.hectltr = hctl * 100
        return self.hectltr
    
    def hltr2cm3(self,hctl):
        self.hectltr = hctl * (10 ** 5)
        return self.hectltr

    def hltr2mm3(self,hctl):
        self.hectltr = hctl * (10 ** 8)
        return self.hectltr

    def hltr2l(self,hctl):
        self.hectltr = hctl * 100
        return self.hectltr

    def hltr2dl(self,hctl):
        self.hectltr = hctl * 1000
        return self.hectltr

    def hltr2cl(self,hctl):
        self.hectltr = hctl * (10 ** 4)
        return  self.hectltr 

    def hltr2ml(self,hctl):
        self.hectltr = hctl * (10 ** 5)
        return self.hectltr

    def hltr2ft3(self,hctl):
        self.hectltr = hctl * 3.5
        return self.hectltr

    def hltr2inch3(self,hctl):
        self.hectltr = hctl * 6102
        return self.hectltr

    def hltr2yd3(self,hctl):
        self.hectltr = hctl / 7
        return self.hectltr

    def hltr2af3(self,hctl):
        self.hectltr = hctl / 12340
        return self.hectltr

class ltr:
    litre = 0

    def __init__(self):
        pass

    def ltr2m3(self,ltr):
        self.litre = ltr / 1000
        return self.litre

    def ltr2dm3(self,ltr):
        self.litre = ltr * 1
        return self.litre

    def ltr2cm3(self,ltr):
        self.litre = ltr * 1000
        return self.litre

    def ltr2mm3(self,ltr):
        self.litre = ltr * (10 ** 6)
        return self.litre

    def ltr2hl(self,ltr):
        self.litre = ltr / 100
        return self.litre

    def ltr2dl(self,ltr):
        self.litre = ltr * 10
        return self.litre

    def ltr2cl(self,ltr):
        self.litre = ltr * 100
        return self.litre

    def ltr2ml(self,ltr):
        self.litre = ltr * 1000
        return self.litre

    def ltr2ft3(self,ltr):
        self.litre = ltr / 28
        return self.litre

    def ltr2inch3(self,ltr):
        self.litre = ltr * 61
        return self.litre

    def ltr2yd3(self,ltr):
        self.litre = ltr * 764
        return self.litre

    def ltr2af3(self,ltr):
        self.litre = ltr / 1234000
        return self.litre

class decilitre:
    decltr = 0

    def __init__(self):
        pass

    def decl2m3(self,dltr):
        self.decltr = dltr / 10000
        return self.decltr

    def decl2dm3(self,dltr):
        self.decltr = dltr / 10
        return self.decltr

    def decl2cm3(self,dltr):
        self.decltr = dltr * 100
        return self.decltr

    def decl2mm3(self,dltr):
        self.decltr = dltr * (10 ** 5)
        return self.decltr

    def decl2hl(self,dltr):
        self.decltr = dltr / 1000
        return self.decltr

    def decl2l(self,dltr):
        self.decltr = dltr / 10
        return self.decltr

    def decl2cl(self,dltr):
        self.decltr = dltr * 10
        return self.decltr
    
    def decl2ml(self,dltr):
        self.decltr = dltr * 100
        return self.decltr

    def decl2ft3(self,dltr):
        self.decltr = dltr / 283
        return self.decltr
    
    def decl2inch3(self,dltr):
        self.decltr = dltr * 6
        return self.decltr

    def decl2yd3(self,dltr):
        self.decltr = dltr / 7645
        return self.decltr

    def decl2af3(self,dltr):
        self.decltr = dltr / (1234 * (10 ** 4))
        return self.decltr

class centiltr:
    cntlt = 0

    def __init__(self):
        pass
    
    def cntlt2m3(self,cltr):
        self.cntlt = cltr / (10 ** 5)
        return self.cntlt

    def cntlt2dm3(self,cltr):
        self.cntlt = cltr / 100
        return self.cntlt

    def cntlt2cm3(self,cltr):
        self.cntlt = cltr * 10
        return self.cntlt

    def cntlt2mm3(self,cltr):
        self.cntlt = cltr * (10 ** 4)
        return self.cntlt

    def cntlt2hl(self,cltr):
        self.cntlt = cltr / (10 ** 4)
        return self.cntlt

    def cntlt2l(self,cltr):
        self.cntlt = cltr / 100
        return self.cntlt

    def cntlt2dl(self,cltr):
        self.cntlt = cltr / 10
        return self.cntlt

    def cntlt2ml(self,cltr):
        self.cntlt = cltr * 10
        return self.cntlt
    
    def cntlt2ft3(self,cltr):
        self.cntlt = cltr / 2831
        return self.cntlt
    
    def cntlt2inch3(self,cltr):
        self.cntlt = cltr / 1.6
        return self.cntlt
    
    def cntlt2yd3(self,cltr):
        self.cntlt = cltr / 76455
        return self.cntlt

    def cntlt2af3(self,cltr):
        self.cntlt = cltr / (1234 * (10 ** 4))
        return self.cntlt

class milliltr:
    mlltr = 0

    def __init__(self):
        pass

    def ml2m3(self,mltr):
        self.mlltr = mltr / (10 ** 6)
        return self.mlltr
    
    def ml2dm3(self,mltr):
        self.mlltr = mltr / 1000
        return self.mlltr

    def ml2cm3(self,mltr):
        self.mlltr = mltr * 1
        return self.mlltr

    def ml2mm3(self,mltr):
        self.mlltr = mltr * 1000
        return self.mlltr

    def ml2hl(self,mltr):
        self.mlltr = mltr / (10 ** 5)
        return self.mlltr

    def ml2l(self,mltr):
        self.mlltr = mltr / 1000
        return self.mlltr

    def ml2cl(self,mltr):
        self.mlltr = mltr / 10
        return self.mlltr

    def ml2dl(self,mltr):
        self.mlltr = mltr / 100
        return self.mlltr

    def ml2ft3(self,mltr):
        self.mlltr = mltr / 28316
        return self.mlltr

    def ml2inch3(self,mltr):
        self.mlltr = mltr / 16
        return self.mlltr
    
    def ml2yd3(self,mltr):
        self.mlltr = mltr / 765554
        return self.mlltr

    def ml2af3(self,mltr):
        self.mlltr = mltr / (1234 * (10 ** 9))
        return self.mlltr
    
class footcub:
    ftcub = 0

    def __init__(self):
        pass

    def ftcub2m3(self,ft3):
        self.ftcub = ft3 / 35
        return self.ftcub

    def ftcub2dm3(self,ft3):
        self.ftcub = ft3 * 28
        return self.ftcub

    def ftcub2cm3(self,ft3):
        self.ftcub = ft3 * 28316
        return self.ftcub

    def ftcub2mm3(self,ft3):
        self.ftcub = ft3 * 28316846
        return self.ftcub
    
    def ftcub2hl(self,ft3):
        self.ftcub = ft3 / 3.5
        return self.ftcub

    def ftcub2l(self,ft3):
        self.ftcub = ft3 * 28
        return self.ftcub

    def ftcub2dl(self,ft3):
        self.ftcub = ft3 * 283
        return self.ftcub

    def ftcub2cl(self,ft3):
        self.ftcub = ft3 * 2831
        return self.ftcub
    
    def ftcub2ml(self,ft3):
        self.ftcub = ft3 * 28316
        return self.ftcub
    
    def ftcub2inch3(self,ft3):
        self.ftcub = ft3 * 1728
        return self.ftcub

    def ftcub2yd3(self,ft3):
        self.ftcub = ft3 / 27
        return self.ftcub

    def ftcub2af3(self,ft3):
        self.ftcub = ft3 / 43578
        return self.ftcub
    
class inchcub:
    inchcube = 0

    def __init__(self):
        pass

    def inchcub2m3(self,inch3):
        self.inchcube = inch3 / 61023
        return self.inchcube

    def inchcub2dm3(self,inch3):
        self.inchcube = inch3 / 61
        return self.inchcube

    def inchcub2cm3(self,inch3):
        self.inchcube = inch3 * 16
        return self.inchcube

    def inchcub2mm3(self,inch3):
        self.inchcube = inch3 * 16387
        return self.inchcube

    def inchcub2hl(self,inch3):
        self.inchcube = inch3 / 6102
        return self.inchcube

    def inchcub2l(self,inch3):
        self.inchcube = inch3 / 61
        return self.inchcube

    def inchcub2dl(self,inch3):
        self.inchcube = inch3 / 6
        return self.inchcube

    def inchcub2cl(self,inch3):
        self.inchcube = inch3 * 1.63
        return self.inchcube

    def inchcub2ml(self,inch3):
        self.inchcube = inch3 * 16
        return self.inchcube

    def inchcub2ft3(self,inch3):
        self.inchcube = inch3 / 1728
        return self.inchcube

    def inchcub2yd3(self,inch3):
        self.inchcube = inch3 / 46656
        return self.inchcube

    def inchcub2af3(self,inch3):
        self.inchcube = inch3 / 75303300
        return self.inchcube

class yardcub:
    ydcub = 0
    
    def __init__(self):
        pass

    def ydcub2m3(self,yd):
        self.ydcub = yd / 1.3
        return self.ydcub

    def ydcub2dm3(self,yd):
        self.ydcub = yd * 764
        return self.ydcub

    def ydcub2cm3(self,yd):
        self.ydcub = yd * 764554
        return self.ydcub

    def ydcub2mm3(self,yd):
        self.ydcub = yd * 764554858
        return self.ydcub

    def ydcub2hl(self,yd):
        self.ydcub = yd * 7.6
        return self.ydcub

    def ydcub2l(self,yd):
        self.ydcub = yd * 764
        return self.ydcub

    def ydcub2dl(self,yd):
        self.ydcub = yd * 7645
        return self.ydcub

    def ydcub2cl(self,yd):
        self.ydcub = yd * 76455
        return self.ydcub

    def ydcub2ml(self,yd):
        self.ydcub = yd * 764554
        return self.ydcub

    def ydcub2ft3(self,yd):
        self.ydcub = yd * 27
        return self.ydcub

    def ydcub2inch3(self,yd):
        self.ydcub = yd * 46656
        return self.ydcub

    def ydcub2af3(self,yd):
        self.ydcub = yd / 1614
        return self.ydcub

class areafoot3:
    aftcub = 0

    def __init__(self):
        pass

    def aftcub2m3(self,af3):
        self.aftcub = af3 * 1234
        return self.aftcub

    def aftcub2dm3(self,af3):
        self.aftcub = af3 * 1234000
        return self.aftcub

    def aftcub2cm3(self,af3):
        self.aftcub = af3 * (1.234 * (10 ** 9))
        return self.aftcub

    def aftcub2mm3(self,af3):
        self.aftcub = af3 * (1.234 * (10 ** 12))
        return self.aftcub

    def aftcub2hl(self,af3):
        self.aftcub = af3 * 12340
        return self.aftcub

    def aftcub2l(self,af3):
        self.aftcub = af3 * 1234000
        return self.aftcub

    def aftcub2dl(self,af3):
        self.aftcub = af3 * (1234 * (10 ** 4))
        return self.aftcub

    def aftcub2cl(self,af3):
        self.aftcub = af3 * (1234 * (10 ** 5))
        return self.aftcub

    def aftcub2ml(self,af3):
        self.aftcub = af3 * (1.234 * (10 ** 9))
        return self.aftcub

    def aftcub2ft3(self,af3):
        self.aftcub = af3 * 43578
        return self.aftcub

    def aftcub2inch3(self,af3):
        self.aftcub = af3 * 75303300
        return self.aftcub

    def aftcub2yd3(self,af3):
        self.aftcub = af3 * 1614
        return self.aftcub