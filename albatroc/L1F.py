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

MotorMecaD.run_angle(350,-140)
wait(1500)
notname.settings(straight_acceleration=900,straight_speed=900)
notname.straight(1440)

#preara el mineraft para despues
notname.turn(-90)
notname.straight(270)
notname.settings(turn_acceleration=200)
notname.turn(180)
notname.straight(190)

#se prepara para la impresora
notname.straight(-280)
notname.turn(-60)
notname.straight(270)
alinear_en_linea()

#roba la impresion 3d
notname.settings(50,50)
notname.straight(110)
notname.straight(-120)

#se prepara para tirar el filamento
notname.turn(32)
notname.straight(130)

#tira el filamento
MotorMecaD.run_angle(1200,240)
MotorMecaD.run_angle(720,-440)

#se va para base con todo
notname.settings(700,700)
notname.turn(70)
notname.straight(200)
notname.turn(20)
notname.straight(1400)