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
notname.settings(720,720,360,360)

#mover el robot!
#Va hacia adelante y gira
notname.straight(240)
notname.turn(-90)


#Va hacia el minecraft  y dobla para dejar el minecraft 1 y la microbit
notname.straight(550)
notname.turn(45)
notname.straight(50)

#se prepara para hacer la mision robotica
notname.straight(-170)
notname.turn(75)
notname.stop()
notname.straight(140)

#hace la mision robotica

notname.settings(960,960)
notname.straight(-275)

#se va para home 
notname.straight(100)
notname.turn(50)
notname.straight(550)
