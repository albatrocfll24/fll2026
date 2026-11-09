from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#iniciciazión 
mti = Motor(Port.A,Direction.COUNTERCLOCKWISE)
mtd = Motor(Port.E,Direction.CLOCKWISE)

MotorMecaD = Motor (Port.F,Direction.CLOCKWISE)
MotorMecaI = Motor (Port.B,Direction.CLOCKWISE)

sensorIzq = ColorSensor(Port.C)
sensorDer = ColorSensor(Port.D)
NEGRO = 10
BLANCO = 90
UMBRAL = (NEGRO + BLANCO) / 2

def alinear_en_linea(velocidad=150):
    """Retrocede un poco y avanza: cada rueda frena cuando SU sensor ve negro."""
    notname.straight(-25)
    izq_listo = False
    der_listo = False
    mti.run(velocidad)
    mtd.run(velocidad)
    while not (izq_listo and der_listo):
        if not izq_listo and sensorIzq.reflection() < UMBRAL:
            mti.hold()
            izq_listo = True
        if not der_listo and sensorDer.reflection() < UMBRAL:
            mtd.hold()
            der_listo = True
        wait(2)
    notname.reset()  # desde acá: rumbo 0 = recto como quedó alinead





#crear el robot base 

notname = DriveBase(mti, mtd, 56,96)
notname.use_gyro(True)

#Va hacia adelante y gira
notname.settings(700,700)

notname.straight(200)
notname.turn(-55)
notname.straight(900)
notname.turn(30)
notname.straight(150)
notname.turn(72)
notname.straight(400)

notname.turn(-45)
notname.straight(200)
notname.turn(70)
notname.straight(-40)
alinear_en_linea()
notname.straight(-20)

MotorMecaD.run_angle(450,250)
notname.straight(-20)
