from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# ---------- Inicialización ----------
# Si el hub NO está acostado con la pantalla hacia arriba, descomentá y ajustá:
# from pybricks.parameters import Axis
# hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
hub = PrimeHub()

mti = Motor(Port.A, Direction.COUNTERCLOCKWISE)
mtd = Motor(Port.E, Direction.CLOCKWISE)
MotorMecaD = Motor(Port.F, Direction.CLOCKWISE)
MotorMecaI = Motor(Port.B, Direction.CLOCKWISE)
sensorIzq = ColorSensor(Port.C)
sensorDer = ColorSensor(Port.D)

# --- Valores calibrados: PONÉ LOS TUYOS ---
WHEEL = 56          # diámetro de rueda (mm), medido con straight(250)
AXLE_TRACK = 78   # calibrado con turn(720) sin gyro

notname = DriveBase(mti, mtd, WHEEL, AXLE_TRACK)
notname.use_gyro(True)

# Lecturas de CADA sensor sobre negro y sobre blanco (medir con print)
I_NEGRO, I_BLANCO = 10, 90   # sensor C (izquierdo)
D_NEGRO, D_BLANCO = 10, 90   # sensor D (derecho)


# ---------- Sensores normalizados (0 = negro, 100 = blanco) ----------
def norm_i():
    v = (sensorIzq.reflection() - I_NEGRO) * 100 / (I_BLANCO - I_NEGRO)
    return max(0, min(100, v))


def norm_d():
    v = (sensorDer.reflection() - D_NEGRO) * 100 / (D_BLANCO - D_NEGRO)
    return max(0, min(100, v))


# ---------- Movimientos ----------
def avanzar(mm, vel=500, acel=500, then=Stop.HOLD):
    """Recta con aceleración controlada (arranca y frena suave)."""
    notname.settings(straight_speed=vel, straight_acceleration=acel)
    notname.straight(mm, then=then)
    if then == Stop.HOLD:
        wait(50)


def girar(grados, vel=150, acel=300, then=Stop.HOLD):
    """Giro suave con gyro. Más bajo vel/acel = más preciso."""
    notname.settings(turn_rate=vel, turn_acceleration=acel)
    notname.turn(grados, then=then)
    if then == Stop.HOLD:
        wait(80)


# ---------- Línea ----------
def alinear_en_linea(velocidad=150, tiempo_max=3000):
    """Retrocede y avanza: cada rueda frena cuando SU sensor ve negro."""
    notname.straight(-25)
    notname.stop()  # soltar el DriveBase antes de usar los motores sueltos
    izq_listo = False
    der_listo = False
    reloj = StopWatch()
    mti.run(velocidad)
    mtd.run(velocidad)
    while not (izq_listo and der_listo):
        if reloj.time() > tiempo_max:   # nunca se queda colgado
            break
        if not izq_listo and norm_i() < 50:
            mti.hold()
            izq_listo = True
        if not der_listo and norm_d() < 50:
            mtd.hold()
            der_listo = True
        wait(2)
    mti.hold()
    mtd.hold()
    wait(100)
    notname.reset()  # desde acá: rumbo 0 = recto como quedó alineado


def buscar_linea(distancia_max=150, velocidad=80):
    """Avanza despacio hasta que el sensor D ve negro (o se acaba la distancia)."""
    inicio = notname.distance()
    notname.drive(velocidad, 0)
    while norm_d() > 50:
        if abs(notname.distance() - inicio) > distancia_max:
            break
        wait(5)
    notname.stop()


def seguir_linea_un_sensor(distancia_mm, sentido=-1, objetivo=50,
                           vel=120, kp=1.0, kd=2,
                           giro_max=50, tiempo_max=10000):
    # Giro positivo = derecha.
    # sentido = -1 -> sensor D sobre el borde DERECHO de la línea:
    #                 ve negro -> gira a la derecha (curva a la derecha)
    # sentido =  1 -> sensor sobre el borde IZQUIERDO de la línea
    reloj = StopWatch()
    inicio = notname.distance()
    error_anterior = norm_d() - objetivo
    while abs(notname.distance() - inicio) < distancia_mm:
        if reloj.time() > tiempo_max:
            break
        error = norm_d() - objetivo
        derivada = error - error_anterior
        giro = (kp * error + kd * derivada) * sentido
        giro = max(-giro_max, min(giro_max, giro))
        notname.drive(vel, giro)
        error_anterior = error
        wait(10)
    notname.stop()


def seguir_linea_dos_sensores(distancia_mm, vel=120, kp=0.8, kd=2.0,
                              giro_max=60, tiempo_max=10000):
    """Alternativa (método OFDL Taiwan): la línea va ENTRE los dos sensores.
    Si D ve negro -> gira a la derecha. Para usarla, cambiá la llamada del run."""
    reloj = StopWatch()
    inicio = notname.distance()
    err_old = norm_i() - norm_d()
    while abs(notname.distance() - inicio) < distancia_mm:
        if reloj.time() > tiempo_max:
            break
        err = norm_i() - norm_d()
        corr = err * kp + kd * (err - err_old)
        corr = max(-giro_max, min(giro_max, corr))
        notname.drive(vel, corr)
        err_old = err
        wait(10)
    notname.stop()


# ---------- RUN ----------
wait(1000)  # robot quieto para que el gyro se asiente

# Va hacia adelante
MotorMecaD.run_angle(350, 120)
avanzar(240, vel=700, acel=600)

# Dobla hacia el minecraft
girar(-65)
avanzar(770, vel=700, acel=600)
girar(45,60)
avanzar(250)
girar(20)

notname.stop()
notname.reset()

# Deja el minecraft
avanzar(980, vel=700, acel=600)


avanzar(-110)



# Dobla hacia la línea negra
girar(90)
avanzar(240)
alinear_en_linea()

# Hace bloques de código
girar(-90)
avanzar(25)
MotorMecaD.run_angle(400, -150)
avanzar(-90)
MotorMecaD.run_angle(400, 200)
avanzar(60)

# Gira para alinearse y hacer los checkpoints
girar(90)
alinear_en_linea()
avanzar(240, vel=250, acel=250)
girar(25)

# Curva a la derecha con el sensor D
buscar_linea()
seguir_linea_un_sensor(150, sentido=-1)
girar(25)

# Vuelve a home
avanzar(200)
avanzar(1400, vel=700, acel=600)