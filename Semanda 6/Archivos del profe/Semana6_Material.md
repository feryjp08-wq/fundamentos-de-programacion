# SEMANA 6 — REPASO INTEGRAL Y CERTIFICACIÓN DE CISCO

**Curso:** Fundamentos de programación
**Semana:** 6 · del martes 17 al viernes 20 de noviembre de 2026 (el lunes 16 es día festivo)
**Actividad 5:** Certificación de Cisco Networking Academy · entrega el viernes 20 a las 23:59 h

> Esta semana no hay temas nuevos. Repasamos los 16 temas para que llegues afinado al examen final de *Python Essentials 1* de Cisco, y vemos las piezas que el examen pregunta y que en clase solo tocamos de pasada.

---

## ÍNDICE

1. El repaso exprés de los 16 temas
2. Lo que Cisco pregunta (y no vimos a fondo)
3. Cómo contestar un "¿qué imprime?"
4. Guía rápida de netacad.com
5. El plan de la semana

---

# 1. EL REPASO EXPRÉS DE LOS 16 TEMAS

| # | Tema | La analogía | Lo que no se te puede olvidar |
| :---: | :--- | :--- | :--- |
| 1 | Algoritmos y modelo EPS | La receta | Entrada → Proceso → Salida. Pasos finitos, ordenados y sin ambigüedad. |
| 2 | Pseudocódigo | El borrador del setlist | Primero se piensa y luego se programa. |
| 3 | Variables, tipos y operadores | La caja con etiqueta | `int`, `float`, `str`, `bool`. `/` siempre da `float`; `//` es división entera; `%` es el residuo; `**` es la potencia. |
| 4 | Entrada y salida | La taquilla que pregunta | `input()` **siempre** regresa texto: conviértelo con `int()` o `float()`. |
| 5 | Decisiones | El cadenero | `if`, `elif`, `else`, combinados con `and`, `or` y `not`. |
| 6 | `while` | Mientras haya gasolina, sigue rodando | Contador, acumulador, `break` (salida de emergencia) y `continue` (saltar la canción). |
| 7 | Detective de bugs | El detective | Error de sintaxis, de ejecución y de lógica. Lee **la última línea** del error. |
| 8 | `for` y `range()` | El setlist | `range(inicio, fin, paso)`: el fin **no** se incluye. |
| 9 | Listas | El setlist del pizarrón | Índices desde 0; los negativos cuentan desde el final; `append()`, `remove()`, `sort()`, `len()`. |
| 10 | Matrices | Los asientos del concierto | `m[fila][columna]` y dos `for`, uno dentro del otro. |
| 11 | Funciones sin `return` | El roadie | Hace su trabajo pero no te entrega nada. Si guardas su resultado, guardas `None`. |
| 12 | Funciones con `return` | La taquilla | Calcula y te **entrega** el resultado. Sus variables son locales. |
| 13 | Tuplas | El disco ya grabado | `( )` inmutables. `(5,)` es tupla y `(5)` es un número: **la coma** hace la tupla. |
| 14 | Diccionarios | El guardarropa | `{clave: valor}`. Se busca por clave; `in` y `get()` evitan el `KeyError`. |
| 15 | Excepciones | El casco | `try` / `except` con el nombre del error. Un `except` para cada falla. |
| 16 | Strings | El cartel | Inmutables. `len`, `upper`, `lower`, `title`, `replace`, `split`, `strip`. |

---

# 2. LO QUE CISCO PREGUNTA (Y NO VIMOS A FONDO)

El examen de Cisco sigue el temario de la certificación PCEP, que es un poco más amplio que el nuestro. Estas piezas aparecen seguido en sus preguntas de "¿qué imprime?". Todos los ejemplos están probados.

### 2.1 Operadores
```python
x = 5
x += 3            # x = x + 3  → 8   (también existen -=, *=, /=, //=, %=)
print(2 ** 3 ** 2)    # 512 → la potencia se resuelve de DERECHA a izquierda: 3**2 primero
print(-7 // 2)        # -4  → // redondea hacia ABAJO, no hacia el cero
print(-7 % 3)         # 2   → el residuo toma el signo del divisor
print(-2 ** 2)        # -4  → primero la potencia, luego el signo
```

**Operadores de bits** (trabajan con el número en binario):

| Operador | Nombre | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| `&` | Y (and de bits) | `5 & 3` → `101 & 011` | `1` |
| `\|` | O (or de bits) | `5 \| 3` | `7` |
| `^` | O exclusivo (xor) | `5 ^ 3` | `6` |
| `~` | Negación | `~5` | `-6` |
| `<<` / `>>` | Recorrer bits | `1 << 3` / `16 >> 2` | `8` / `4` |

> `<< n` multiplica por 2ⁿ y `>> n` divide entre 2ⁿ (división entera).

### 2.2 `print()` con `sep` y `end`
```python
print("A", "B", "C", sep="-")   # A-B-C   → sep: qué va ENTRE los valores (por defecto, un espacio)
print("rock", end=" ")          # end: qué va AL FINAL (por defecto, un salto de línea)
print("pesado")                 # rock pesado
```

### 2.3 Ciclos: `else` y `pass`
```python
n = 3
while n > 0:
    n -= 1
else:
    print("terminó", n)   # terminó 0 → el else corre si el ciclo acabó SIN break

for i in range(3):
    if i == 1:
        break
else:
    print("nunca")        # no se imprime: hubo break

if True:
    pass                  # pass = "aquí no hago nada"; sirve para dejar un bloque vacío
```

### 2.4 Listas: rebanadas, `insert`, `del`, `index`, `sorted`
```python
nums = [10, 20, 30, 40, 50]
nums[1:3]      # [20, 30]      → del índice 1 al 3, SIN incluir el 3
nums[:2]       # [10, 20]      → desde el inicio
nums[-2:]      # [40, 50]      → los dos últimos
nums[::2]      # [10, 30, 50]  → de dos en dos
nums[::-1]     # [50, 40, 30, 20, 10] → al revés

l = [1, 2, 3]
l.insert(1, 9)    # [1, 9, 2, 3] → inserta en la posición 1
del l[0]          # [9, 2, 3]    → borra por posición
l.index(2)        # 1            → ¿en qué posición está el 2?
s = sorted(l)     # sorted() regresa una lista NUEVA; sort() cambia la original
"bateria" not in l    # True
```

### 2.5 La trampa de las dos etiquetas (copiar listas)
```python
a = [1, 2, 3]
b = a          # ¡NO es una copia! Son dos etiquetas pegadas a la MISMA lista
b.append(4)
print(a)       # [1, 2, 3, 4]
c = a[:]       # esto sí es una copia
```
> Analogía: `b = a` es ponerle otra etiqueta a la misma caja. Lo que metas por una etiqueta aparece en la otra.

Lo mismo pasa al mandar una lista a una función: si la función le hace `append()`, cambia la lista original.

### 2.6 Listas por comprensión
```python
dobles = [x * 2 for x in range(4)]          # [0, 2, 4, 6]
sin_o = [c for c in "moto" if c != "o"]     # ['m', 't']
```
> Se lee: "dame `x * 2` por cada `x` en `range(4)`". Es un `for` + `append` en una sola línea.

### 2.7 Funciones: valores por defecto, argumentos por nombre y `global`
```python
def saludo(nombre, ciudad="Qro"):       # ciudad tiene valor por defecto
    return nombre + " de " + ciudad

saludo("Ana")                           # Ana de Qro
saludo("Luis", "Mty")                   # Luis de Mty
saludo(ciudad="Gdl", nombre="Mía")      # por nombre, el orden no importa

x = 10
def g():
    global x      # "uso la x de afuera, no creo una nueva"
    x = 99
g()
print(x)          # 99
```

**Recursión:** una función que se llama a sí misma. Siempre necesita un caso que la detenga.
```python
def factorial(n):
    if n <= 1:
        return 1                  # caso que detiene
    return n * factorial(n - 1)   # se llama a sí misma con un problema más chico
```

### 2.8 Tuplas, diccionarios y strings
```python
t = ([1, 2], 3)
t[0].append(9)       # ([1, 2, 9], 3) → la tupla no cambia, pero la LISTA de adentro sí

d = {"a": 1, "b": 2}
del d["b"]           # borra la clave

s = "Metallica"
s[2:5]               # 'tal' → las rebanadas también funcionan en strings
s[::-1]              # 'acillateM'
print("Hola\nMundo") # \n es un salto de línea; len("a\nb") es 3
print('Rock "pesado"')   # comillas dentro de comillas: alterna simples y dobles
```

### 2.9 Excepciones: la familia y el orden
```
BaseException
 └─ Exception
     ├─ ArithmeticError
     │   └─ ZeroDivisionError
     ├─ LookupError
     │   ├─ IndexError
     │   └─ KeyError
     ├─ TypeError
     └─ ValueError
```
- Python revisa los `except` **en orden** y entra **solo al primero que coincide**. Un `except ArithmeticError:` atrapa también el `ZeroDivisionError`, así que si va primero, el `except ZeroDivisionError:` de abajo nunca se usa.
- Si el error ocurre dentro de una función que no lo atrapa, **viaja hacia afuera** hasta el `try` que la llamó.

---

# 3. CÓMO CONTESTAR UN "¿QUÉ IMPRIME?"

1. **No adivines: rastrea.** Haz en papel una tabla con las variables y ve cambiando sus valores línea por línea, como hacíamos en el detective de bugs.
2. **Busca la trampa.** Casi siempre está en: `/` contra `//`, el fin de `range()` o de una rebanada que no se incluye, `b = a` con listas, `end=` y `sep=`, el orden de los `except` o una función sin `return`.
3. **Cuenta las vueltas** de los ciclos antes de calcular nada.
4. **Si hay `input()`**, recuerda que todo llega como texto: `"5" + "5"` da `"55"`.
5. **Si una opción dice "error"**, pregúntate: ¿se intenta cambiar una tupla o un string? ¿se pide un índice o una clave que no existe? ¿`int("3.5")`?

---

# 4. GUÍA RÁPIDA DE NETACAD.COM

1. Entra a [netacad.com](https://www.netacad.com) y crea tu cuenta con tu correo institucional. *Skills for All ya está integrado ahí.*
2. Escribe tu **nombre completo real**: es el que aparecerá en la insignia.
3. Inscríbete a **Python Essentials 1** con la liga del grupo o búscalo en el catálogo.
4. Avanza los **4 módulos** en orden:
   1. Introducción a Python y a la programación
   2. Tipos de datos, variables, operadores y entrada/salida
   3. Booleanos, condicionales, ciclos, listas y operaciones lógicas y de bits
   4. Funciones, tuplas, diccionarios, excepciones y procesamiento de datos
5. Presenta el **examen final** cuando termines los módulos. **Toma la captura del resultado en ese momento.**
6. Reclama tu **insignia** en Credly (te llega un correo) y copia su liga pública.
7. Arma el reporte en PDF y súbelo a `semana6/`.

> ⏱️ Cisco calcula unas **30 horas** para el curso. Haz por lo menos un módulo por día.

---

# 5. EL PLAN DE LA SEMANA

| Día | En clase | En netacad.com (tarea) |
| :--- | :--- | :--- |
| **Lun 16** | Día festivo | Avanzar los módulos 1 y 2 |
| **Mar 17** | Temas 1–8 + "Lo que Cisco pregunta" de operadores, `print` y ciclos · ejercicios 1–12 | Terminar el módulo 3 |
| **Mié 18** | Temas 9–12 + listas, copias y funciones · ejercicios 13–24 | Terminar el módulo 4 |
| **Jue 19** | Temas 13–16 + excepciones y strings · ejercicios 25–36 | **Presentar el examen final** |
| **Vie 20** | Simulacro mixto · ejercicios 37–48 · resolver dudas del reporte | Entregar el reporte antes de las 23:59 |
