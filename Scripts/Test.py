import Motor
import Keyboard as km

km.init()

while True:
    if km.getKey('w'):
        print('avancer')
        Motor.avancer(75)
    elif km.getKey('s'):
        print('recule')
        Motor.reculer(100)
    elif km.getKey('q'):
        print('avGauche')
        Motor.avGauche(100)
    elif km.getKey('e'):
        print('avDroit')
        Motor.avDroit(100)
    elif km.getKey('a'):
        print('arGauche')
        Motor.arGauche(100)
    elif km.getKey('d'):
        print('arDroit')
        Motor.arDroit(100)
    else:
        Motor.stop(0)