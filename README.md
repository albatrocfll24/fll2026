# 🤖 Albatroc — FIRST LEGO League 2026

Programas del robot del equipo **Albatroc**, de la Escuela Técnica de Bella Unión (Artigas, Uruguay), para la instancia final de FIRST LEGO League Challenge 2026.

**Equipo:** Melissa González · Lara López · Valentín Sosa · Lucas Silva · Benjamín Argain

---

## Contenido

- [Estructura del repositorio](#estructura-del-repositorio)
- [El robot](#el-robot)
- [Por qué programamos con Pybricks](#por-qué-programamos-con-pybricks)
- [Estrategia del juego del robot](#estrategia-del-juego-del-robot)
- [Programas de este repositorio](#programas-de-este-repositorio)
- [Documentos (`docs/`)](#documentos-docs)
- [Correspondencia lanzamiento ↔ programa ↔ planilla](#correspondencia-lanzamiento--programa--planilla)
- [Técnicas de programación](#técnicas-de-programación)
- [Cómo probamos los lanzamientos](#cómo-probamos-los-lanzamientos)
- [Lo que aprendimos](#lo-que-aprendimos)

---

## Estructura del repositorio

```
fll/
├── README.md                          ← este archivo
├── albatroc/                          ← programas del robot (Pybricks / Python)
│   ├── L1F.py                         ← Lanzamiento 1
│   ├── L2F.py                         ← Lanzamiento 2
│   ├── L3F.py                         ← Lanzamiento 3
│   ├── L4F.py                         ← Lanzamiento 4
│   └── L5F.py                         ← Lanzamiento 5
└── docs/
    └── Prueba de misiones Albatroc.xlsx  ← registro de las 21 pruebas de cada lanzamiento
```

La **F** del nombre de cada programa significa **Final**: son las versiones que usamos en la instancia final.

---

## El robot

Pasamos por tres versiones. Cada una salió de lo que vimos que fallaba en la pista.

| Versión | Etapa | Características |
|---|---|---|
| Robot inicial | Práctica | Base básica con mecanismos fijos (sin motor), sobre todo para misiones de empuje |
| **Pepe** | Etapa virtual | Cuadrado y modular, encaje rápido, doble salida para mecanismos (laterales y superiores). 17 × 15,1 × 6,5 cm |
| **Robot final** | Instancia final | Más compacto: 14 × 14 × 6,5 cm, 2 ruedas anchas y sin rueda loca |

### De Pepe al robot final

| Aspecto | Pepe | Robot final | Por qué lo cambiamos |
|---|---|---|---|
| Tamaño | 17 × 15,1 cm | 14 × 14 cm | No pasaba por los lugares estrechos de la pista |
| Apoyo | Rueda loca | 2 ruedas anchas | La rueda loca nos trababa en Checkpoints |
| Sensores | Mal ubicados | En los extremos | No leían bien la línea |
| Motores y brick | Brick entre las ruedas | Brick arriba | Así las ruedas quedan más juntas |
| Salidas | Laterales y superiores | Sin laterales | Las laterales eran incómodas y lentas para colocar mecanismos |

Mantuvimos lo que funcionaba: la **estructura modular** y el **encaje rápido**. Todos los mecanismos se construyen sobre un mismo **casco base**.

### Componentes

- 1 SPIKE Prime Hub
- 2 motores de tracción y 2 motores para mecanismos
- 2 sensores de color
- 2 ruedas anchas de 56 mm

### Puertos

| Puerto | Uso | Nombre en el código |
|---|---|---|
| A | Motor de tracción izquierdo | `mti` |
| E | Motor de tracción derecho | `mtd` |
| B | Motor de mecanismo izquierdo | `MotorMecaI` |
| F | Motor de mecanismo derecho | `MotorMecaD` |
| C | Sensor de color izquierdo | `sensorIzq` |
| D | Sensor de color derecho | `sensorDer` |

La base del robot (`DriveBase`) se llama `notname` en todos los programas.

---

## Por qué programamos con Pybricks

Buscábamos **más precisión** en los movimientos del robot. Pybricks nos permite programar en **Python** y resuelve el manejo del giroscopio:

- **DriveBase:** le indicamos el diámetro de las ruedas y la distancia entre ellas, y calcula solo los movimientos.
- **Giroscopio:** giros y rumbo más exactos.
- **Sensores de color:** para alinearnos con las líneas negras y seguirlas.

Los integrantes nuevos del equipo tuvieron que aprender Python para usarlo.

---

## Estrategia del juego del robot

### 1. Elegimos las misiones con una fórmula de costo-beneficio

Para decidir qué misiones hacer y en qué orden, creamos esta fórmula:

```
Resultado = dificultad × distancia ÷ puntos
```

| Dato | Qué significa |
|---|---|
| Dificultad | Del 1 al 5, según cuánto nos costaba la misión |
| Distancia | Qué tan lejos está la misión |
| Puntos | Lo que otorga la misión |

**Cuanto menor es el resultado, más nos conviene la misión.**

| Misión | Cálculo | Resultado | Conclusión |
|---|---|---|---|
| Robótica | 1 × 64 ÷ 20 | 3,2 | Conviene |
| Prueba de precisión | 5 × 135 ÷ 20 | 33,75 | Conviene menos |

Para la instancia final **actualizamos la dificultad y los puntos**. Por ejemplo, Robótica pasó a 1 × 64 ÷ 30 = **2,13**.

### 2. Agrupamos las misiones en 5 lanzamientos

| Lanzamiento | Qué hace | Puntos | Tiempo | Pts/s |
|---|---|---|---|---|
| **L1** | Filamento; recoge 2 Minecraft e impresión 3D | 40 | 32 s | 1,3 |
| **L2** | Dron, conectores y 2 cubos | 80 | 23 s | 3,5 |
| **L3** | Robótica, 3 cubos, micro:bit y modelo 3D | 110 | 12 s | **9,2** |
| **L4** | 1 cubo, bloques de código y 2 checkpoints | 55 | 35 s | 1,6 |
| **L5** | Prueba de fuerza y prueba de precisión | 75 | 13 s | 5,8 |

**Puntaje objetivo: 445 puntos**

- 360 puntos de lanzamientos (115 s de recorrido)
- 60 puntos de fichas de precisión
- 25 puntos de inspección

### 3. Por qué ese orden

- **L1 va primero** porque recolecta en la impresora y deja más piezas para L3.
- **L3, junto a Robótica, es el lanzamiento que más rinde** (9,2 puntos por segundo).
- **L2 despeja la pista** para que L4 pase por los checkpoints sin chocar.

---

## Programas de este repositorio

Cada lanzamiento es un programa independiente dentro de la carpeta `albatroc/`. No dependen entre sí: cada archivo inicializa sus propios motores, sensores y `DriveBase`.

| Archivo | Lanzamiento | Misiones | Qué usa |
|---|---|---|---|
| [`albatroc/L1F.py`](albatroc/L1F.py) | L1 | Filamento, Minecraft e impresión 3D | Alineación con línea, motor de mecanismo derecho para tirar el filamento |
| [`albatroc/L2F.py`](albatroc/L2F.py) | L2 | Dron, conectores y cubos | Dos alineaciones con línea en el recorrido, motor de mecanismo derecho |
| [`albatroc/L3F.py`](albatroc/L3F.py) | L3 | Robótica, cubos, micro:bit y modelo 3D | Solo movimientos con giroscopio, a alta velocidad (el más corto y rápido) |
| [`albatroc/L4F.py`](albatroc/L4F.py) | L4 | Cubo, bloques de código y checkpoints | Sensores normalizados, seguidor de línea PD, funciones `avanzar`/`girar`, tiempos máximos |
| [`albatroc/L5F.py`](albatroc/L5F.py) | L5 | Prueba de fuerza y precisión | Alineación con línea y motor de mecanismo derecho al final |

> **Nota:** la distancia entre ruedas (`axle_track`) del `DriveBase` no es igual en todos los programas: L2, L3 y L4 usan **78 mm** y L1 y L5 usan **96 mm**. Son los valores con los que cada lanzamiento quedó calibrado; si se cambia uno, hay que volver a probar los giros de ese lanzamiento.

### Cómo correr un lanzamiento

1. Abrir [Pybricks Code](https://code.pybricks.com) en Chrome o Edge.
2. Conectar el SPIKE Prime Hub (con el firmware de Pybricks instalado).
3. Abrir el archivo del lanzamiento y ejecutarlo.
4. Dejar el robot **quieto en Home** al arrancar, para que el giroscopio se calibre.

---

## Documentos (`docs/`)

### `Prueba de misiones Albatroc.xlsx`

Es la planilla donde registramos las **21 tiradas de cada lanzamiento**. Tiene una hoja por lanzamiento y una plantilla:

| Hoja | Contenido |
|---|---|
| `plantilla` | Hoja vacía para copiar cuando se prueba un lanzamiento nuevo |
| `l1` | Pruebas del Lanzamiento 1 |
| `l2` | Pruebas del Lanzamiento 2 |
| `l3` | Pruebas del Lanzamiento 3 |
| `l4` | Pruebas del Lanzamiento 4 |
| `l5` | Pruebas del Lanzamiento 5 |

Cada hoja tiene las mismas columnas:

| Columna | Qué se anota |
|---|---|
| Intentos | Número de tirada (1 a 21) |
| Éxito | `1` si la tirada cumplió el criterio de éxito, `0` si no |
| Puntos | Puntos que hizo el robot en esa tirada |
| Items / observaciones | Notas sobre lo que pasó (por ejemplo, en L5: *"la fuerza puede no quedar el seguro"*) |

Al pie de cada hoja se calculan solos el **porcentaje de éxito** y la **media de puntos**.

---

## Correspondencia lanzamiento ↔ programa ↔ planilla

| Lanzamiento | Programa | Hoja en `docs/Prueba de misiones Albatroc.xlsx` | Fecha de las pruebas |
|---|---|---|---|
| L1 | [`albatroc/L1F.py`](albatroc/L1F.py) | `l1` | 8/11 |
| L2 | [`albatroc/L2F.py`](albatroc/L2F.py) | `l2` | 16/6 |
| L3 | [`albatroc/L3F.py`](albatroc/L3F.py) | `l3` | 9/11 |
| L4 | [`albatroc/L4F.py`](albatroc/L4F.py) | `l4` | 16/6 |
| L5 | [`albatroc/L5F.py`](albatroc/L5F.py) | `l5` | 16/6 |

Cuando se modifica un programa, hay que repetir sus 21 tiradas y actualizar su hoja, para que los datos correspondan a la versión del código que está en el repositorio.

---

## Técnicas de programación

### Alineación con la línea negra (`alinear_en_linea`)

Está en L1, L2, L4 y L5.

El robot retrocede un poco y avanza despacio. **Cada rueda frena cuando su propio sensor ve la línea negra**, así el robot queda derecho sobre la línea. Después reiniciamos el rumbo del giroscopio: desde ese punto, "recto" es exactamente como quedó alineado.

Nos sirve para **borrar el error acumulado** en la mitad de un recorrido.

### Sensores normalizados (L4)

Cada sensor lee distinto, así que convertimos sus lecturas a una escala de **0 (negro) a 100 (blanco)**. Así los dos sensores responden igual.

### Seguidor de línea PD (L4)

Para los checkpoints, el robot sigue una **línea curva** con un control **proporcional-derivativo**:

- **P:** corrige según cuánto se desvió de la línea.
- **D:** corrige según qué tan rápido se está desviando, para que no oscile.

También dejamos una versión con **dos sensores** (`seguir_linea_dos_sensores`), donde la línea va entre ambos.

### Aceleración controlada

Ajustamos velocidad y aceleración en cada tramo: **rápido en los recorridos largos** y **lento y suave en las misiones delicadas**, para que el robot no patine. En L4 esto está dentro de las funciones `avanzar()` y `girar()`.

### Seguridad (L4)

Las rutinas con sensores de L4 tienen un **tiempo máximo** o una **distancia máxima**. Si el robot no encuentra la línea, sigue igual en vez de quedarse trabado. En L1, L2 y L5 la alineación todavía no tiene ese límite.

---

## Cómo probamos los lanzamientos

Repetimos **cada lanzamiento 21 veces**, para saber qué tan confiable es y no quedarnos con una sola prueba que salió bien. Los datos completos están en [`docs/Prueba de misiones Albatroc.xlsx`](docs/Prueba%20de%20misiones%20Albatroc.xlsx).

| Criterio | Qué cuenta como éxito |
|---|---|
| L1 a L4 | El robot vuelve a la base |
| L5 | El robot no rompe las misiones |

| Lanzamiento | Éxitos (de 21) | % de éxito | Promedio de puntos |
|---|---|---|---|
| L1 | 21 | 100 % | 71,9 |
| L2 | 20 | 95 % | 55,2 |
| L3 | 21 | 100 % | 101,4 |
| L4 | 16 | 76 % | 46,0 |
| L5 | 21 | 100 % | 57,9 |

Lo que nos dicen estos números:

- **L3** es el más confiable y el que más puntos hace, como esperábamos por la estrategia.
- **L4** es el que más falla (5 de 21). Es el recorrido más largo y el que depende de seguir la línea en los checkpoints.
- **L5** siempre vuelve sin romper nada, pero la prueba de fuerza no siempre queda trabada: por eso a veces hace 75 puntos y a veces 30.

---

## Lo que aprendimos

- **Peso:** los engranajes dejaban de agarrar por mala distribución del peso. Sumamos ruedas o piezas similares para repartirlo.
- **Engranajes:** de chico a grande ganamos fuerza; de grande a chico, velocidad.
- **Diseño:** un robot más chico y con el peso bien repartido nos dio acceso a más misiones.
- **Programación:** aprendimos Python, a usar el giroscopio y a seguir líneas.
- **Organización:** usamos Trello para repartir tareas. Las terminadas pasaban a "En revisión" y las decisiones las tomábamos entre todos.

---

Guardamos las versiones de los programas en Google Drive y las publicamos acá para que cualquiera pueda ver nuestro código. 🐦
