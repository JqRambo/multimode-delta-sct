import numpy as np

def doubleModediscern(period1,period2):
    if period1>period2:
        ratio=period2/period1
        if ratio>0.89 or ratio<0.46:
            period1_Mode=0
            period2_Mode=0
        elif 0.82<ratio<0.85:
            period1_Mode='2O'
            period2_Mode='3O'
        elif 0.79<ratio<0.82:
            period1_Mode='1O'
            period2_Mode='2O'
        elif 0.75<ratio<0.79:
            period1_Mode='F'
            period2_Mode='1O'
        elif 0.65<ratio<0.71:
            period1_Mode='1O'
            period2_Mode='3O'
        elif 0.58<ratio<0.65:
            period1_Mode='F'
            period2_Mode='2O'
        elif 0.48<ratio<0.55:
            period1_Mode='F'
            period2_Mode='3O'
        else:
            period1_Mode=0
            period2_Mode=0
    else:
        ratio=period1/period2
        if ratio>0.89 or ratio<0.46:
            period2_Mode=0
            period1_Mode=0
        elif 0.82<ratio<0.85:
            period2_Mode='2O'
            period1_Mode='3O'
        elif 0.79<ratio<0.82:
            period2_Mode='1O'
            period1_Mode='2O'
        elif 0.75<ratio<0.79:
            period2_Mode='F'
            period1_Mode='1O'
        elif 0.65<ratio<0.71:
            period2_Mode='1O'
            period1_Mode='3O'
        elif 0.58<ratio<0.65:
            period2_Mode='F'
            period1_Mode='2O'
        elif 0.48<ratio<0.55:
            period2_Mode='F'
            period1_Mode='3O'
        else:
            period2_Mode=0
            period1_Mode=0
    return period1_Mode,period2_Mode