MM_IN_INCH = 25.4
MM_IN_FOOT = 304.8
MM_IN_YARD = 914.4
MM_IN_MILE = 1609344

def cm2inches(cm, rounding = 2, addUnit = False):
    if addUnit:
        return str (round (cm * 0.393, rounding)) + " inches "
    else:
        return round(cm * 0.393, rounding)
    
def m2feet(m, rounding = 2, addUnit = False):
    if addUnit:
        return str ( round (m * 3.281, rounding)) + " feet "
    else:
        return round(m * 3.281, rounding)
    
def m2yards(m, rounding = 2, addUnit = False):
    if addUnit:
        return str ( round (m * 1.094, rounding)) + " yards "
    else:
        return round(m * 1.094, rounding)
    
def km2miles(km, rounding = 2, addUnit = False):
    if addUnit:
        return str ( round (km * 0.621, rounding)) + " miles "
    else:
        return round(km * 0.621, rounding)
