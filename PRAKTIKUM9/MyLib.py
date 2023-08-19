import Globals
def CheckOnOff():
    return Globals.g_onoff

def TurnOnoff():
    if Globals.g_onoff == True:
        Globals.g_onoff = False
    else :
        Globals.g_onoff = True

def TempUp():
    if CheckOnOff() == True:
        if Globals.g_temp < 30 and Globals.g_temp > 18:
            Globals.g_temp += 1
       
def TempDown():
    if CheckOnOff() == True:
        if Globals.g_temp < 30 and Globals.g_temp > 18:
            Globals.g_temp -= 1

def FanSpeed():
    if CheckOnOff() == True:
        if Globals.g_fanlevel == 4:
            Globals.g_fanlevel = 1
        else:
            Globals.g_fanlevel += 1

def PowerChill():
    if CheckOnOff() == True:
         Globals.g_temp = 18
         Globals.g_fanlevel = 4
      
def Display():
    if CheckOnOff() == True:
        print("Temperatur Suhu :", Globals.g_temp)
        print("Level Kipas :", Globals.g_fanlevel)