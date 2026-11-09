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


#crear el robot base 

notname = DriveBase(mti, mtd, 56,78)
notname.use_gyro(True)

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




#Va hacia adelante y gira
MotorMecaD.run_angle(400,85)
notname.settings(720)
notname.straight(680)

alinear_en_linea()
notname.straight(-50)
notname.turn(-90)
notname.straight(340)
alinear_en_linea()
notname.straight(134)
notname.turn(30)
notname.straight(-25)
MotorMecaD.run_angle(480,150)

notname.turn(140)

notname.straight(350)
notname.turn(-60)
notname.straight(200)
notname.turn(30)
notname.straight(80)
notname.straight(-80)
notname.turn(43)
notname.settings(100,100)
notname.straight(-200)
notname.settings(720,720)
notname.straight(120)
notname.turn(80)
notname.straight(900)