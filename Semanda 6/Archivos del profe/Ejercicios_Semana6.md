# 48 EJERCICIOS DE REPASO — SEMANA 6

**Curso:** Fundamentos de programación
**Semana:** 6 · del martes 17 al viernes 20 de noviembre de 2026 (el lunes 16 es día festivo)
**Alcance:** temas 1 a 16, preparados para el examen final de *Python Essentials 1* de Cisco
**No son evaluables.** Se resuelven en clase en `semana6/repaso.ipynb`.

---

## Cómo se trabajan

Cada día tiene dos partes:

1. **Modo examen (8 ejercicios):** fragmentos cortos como los del examen de Cisco. **Antes de ejecutar**, escribe en una celda Markdown lo que crees que imprime. Después ejecútalo y compara. Si fallaste, escribe en una línea por qué.
2. **Taller (4 ejercicios):** problemas que combinan varios temas. Tienen entradas de prueba y salida esperada para que te revises solo.

**Los que llevan ⚠️ Cisco** tocan algo que el examen pregunta y que no vimos a fondo en el curso. La explicación corta está en el material y en la presentación de la semana ("Lo que Cisco pregunta").

**Nivel del taller:** 🟢 calentamiento · 🟡 en forma · 🔴 modo experto


---

## MARTES 17 · TEMAS 1 A 8: TIPOS, OPERADORES, DECISIONES Y CICLOS

### Modo examen: ¿qué imprime?

#### 1. La potencia que se lee al revés ⚠️ Cisco
```python
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
```

#### 2. División entera con números negativos ⚠️ Cisco
```python
print(7 // 2, -7 // 2)
print(7 % 3, -7 % 3)
```

#### 3. ¿Entero o decimal?
```python
print(10 / 2)
print(type(10 / 2))
print(10 // 2)
```

#### 4. print() con sep y end ⚠️ Cisco
```python
print("A", "B", "C", sep="-", end="!\n")
print("rock", end=" ")
print("pesado")
```

#### 5. Operadores abreviados ⚠️ Cisco
```python
x = 5
x += 3
x *= 2
x -= 1
print(x)
```

#### 6. and, or y not juntos
```python
print(not 3 > 5 and 2 == 2)
print(True or False and False)
print(10 > 5 > 1)
```

#### 7. Texto que se multiplica
```python
print("ja" * 3 + "!")
print("5" + "5", 5 + 5)
print(int("5") + 5)
```

#### 8. range hacia atrás con continue
```python
for i in range(10, 0, -3):
    if i == 4:
        continue
    print(i, end=" ")
```


### Taller

#### 9. 🟢 El radar de la carretera
Pide velocidades (en km/h) hasta que el usuario escriba `0`. Clasifica cada una: hasta 80 → `OK`; de 81 a 100 → `Precaución`; más de 100 → multa de **$25 por cada km/h arriba de 100**. Al final muestra cuántas multas hubo y cuánto suman.
**Usa:** `while True` + `break`, `if/elif/else`, contador y acumulador.
**Entradas de prueba:** `75`, `95`, `120`, `130`, `0`
**Salida esperada:**
```
OK
Precaución
Multa: $500
Multa: $750
Multas: 2 · Total: $1250
```

#### 10. 🟡 Cambio exacto en la taquilla
Pide un monto entero y desglósalo en la menor cantidad de billetes (`500, 200, 100, 50, 20`) y monedas (`10, 5, 2, 1`). Muestra solo las denominaciones que se usan.
**Usa:** listas, `for`, `//` y `%`, `if`.
**Entrada de prueba:** `1987`
**Salida esperada:**
```
3 billete(s) de $500
2 billete(s) de $200
1 billete(s) de $50
1 billete(s) de $20
1 moneda(s) de $10
1 moneda(s) de $5
1 moneda(s) de $2
```

#### 11. 🟡 Los números del sorteo
Pide un número `n`. Muestra en una sola línea los números del 1 al `n` que sean múltiplos de 3 **o** de 5, y al final cuántos fueron y cuánto suman.
**Usa:** `for` con `range`, `%`, `or`, `end=" "`, contador y acumulador.
**Entrada de prueba:** `20`
**Salida esperada:**
```
3 5 6 9 10 12 15 18 20
Cantidad: 9 · Suma: 98
```

#### 12. 🔴 ¿Me alcanza la gasolina?
Tu moto carga 15 litros y rinde 18 km/l. Pide los km de cada tramo hasta que el usuario escriba `fin`. Si un tramo es más largo que la autonomía que te queda, avisa en qué tramo te quedaste sin gasolina y termina. Si llegas a `fin`, muestra cuántos km de autonomía te quedan.
**Usa:** `while True`, comparar el texto **antes** de convertirlo con `int()`, contador de tramos, `break`.
💡 Pista: la autonomía inicial es `15 * 18`.
**Prueba 1:** `80`, `120`, `60`, `fin` → `Llegaste. Te quedan 10 km de autonomía`
**Prueba 2:** `100`, `200` → `Te quedaste sin gasolina en el tramo 2`


---

## MIÉRCOLES 18 · TEMAS 9 A 12: LISTAS, MATRICES Y FUNCIONES

### Modo examen: ¿qué imprime?

#### 13. Rebanadas de lista (slicing) ⚠️ Cisco
```python
nums = [10, 20, 30, 40, 50]
print(nums[1:3])
print(nums[:2], nums[-2:])
print(nums[::2])
```

#### 14. insert y del ⚠️ Cisco
```python
l = [1, 2, 3]
l.insert(1, 9)
del l[0]
print(l, len(l))
```

#### 15. Dos nombres, una sola lista ⚠️ Cisco
```python
a = [1, 2, 3]
b = a
b.append(4)
c = a[:]
c.append(5)
print(a)
print(c)
```

#### 16. in, not in e index
```python
banda = ["voz", "guitarra", "bajo"]
print("bateria" not in banda)
print("bajo" in banda)
print(banda.index("bajo"))
```

#### 17. sort() vs sorted() ⚠️ Cisco
```python
l = [3, 1, 2]
s = sorted(l)
print(l)
print(s)
```

#### 18. Parámetros con valor por defecto ⚠️ Cisco
```python
def saludo(nombre, ciudad="Qro"):
    return nombre + " de " + ciudad

print(saludo("Ana"))
print(saludo("Luis", "Mty"))
print(saludo(ciudad="Gdl", nombre="Mía"))
```

#### 19. Lo de la gira se queda en la gira… ¿o no? ⚠️ Cisco
```python
x = 10

def f():
    x = 5
    return x

def g():
    global x
    x = 99

print(f(), x)
g()
print(x)
```

#### 20. La función que a veces no regresa nada
```python
def signo(n):
    if n > 0:
        return "positivo"

print(signo(5))
print(signo(-1))
```


### Taller

#### 21. 🟢 Setlist sin repetidos
```python
canciones = ["Intro", "Riff", "Solo", "Riff", "Balada", "Intro", "Encore", "Solo"]
```
Arma una **lista nueva** sin canciones repetidas, en el mismo orden en que aparecen por primera vez. Muestra cuántas se quitaron.
**Usa:** lista vacía, `for`, `not in`, `append()`, `len()`.
**Salida esperada:**
```
['Intro', 'Riff', 'Solo', 'Balada', 'Encore']
Se quitaron 3 repetidas
```

#### 22. 🔴 Buscaminas
```python
tablero = [
    [".", "*", ".", "."],
    [".", ".", ".", "*"],
    ["*", ".", ".", "."],
    [".", ".", "*", "."],
]
```
Crea `contar_vecinas(m, f, c)` que **regrese** cuántas minas (`*`) hay alrededor de la casilla `[f][c]` (las 8 de alrededor, sin salirte del tablero). Imprime el tablero cambiando cada `.` por su número.
**Usa:** matriz, `for` anidados, función con `return`, `and` para revisar los bordes.
💡 Pista: recorre `df` y `dc` en `[-1, 0, 1]` y salta el caso en que los dos son 0.
**Salida esperada:**
```
1 * 2 1
2 2 2 *
* 2 2 2
1 2 * 1
```

#### 23. 🟡 Rotar el setlist
Crea `rotar(lista, n)` que **regrese una lista nueva** con los primeros `n` elementos movidos al final. Si `n` es mayor que el largo de la lista, debe seguir funcionando. La lista original no cambia.
**Usa:** slicing (`lista[n:] + lista[:n]`), `%`, función con `return`.
```python
setlist = ["Intro", "Riff", "Solo", "Balada", "Encore"]
print(rotar(setlist, 2))
print(rotar(setlist, 7))
print(setlist)
```
**Salida esperada:**
```
['Solo', 'Balada', 'Encore', 'Intro', 'Riff']
['Solo', 'Balada', 'Encore', 'Intro', 'Riff']
['Intro', 'Riff', 'Solo', 'Balada', 'Encore']
```

#### 24. 🟡 Boleta con funciones que se llaman entre sí
Crea tres funciones:
- `promedio(cals)`: con `return`, redondeado a 1 decimal.
- `letra(prom, minimo=70)`: con `return`. 90 o más → `A`, 80 o más → `B`, `minimo` o más → `C`, si no → `F`.
- `reporte(nombre, cals, minimo=70)`: sin `return`; usa las otras dos e imprime el resultado.

**Usa:** parámetros con valor por defecto, argumentos por nombre (`minimo=60`), funciones que llaman a otras.
```python
reporte("Ana", [95, 88, 92])
reporte("Luis", [70, 65, 72])
reporte("Luis", [70, 65, 72], minimo=60)
reporte("Mía", [85, 79, 81])
```
**Salida esperada:**
```
Ana: 91.7 → A
Luis: 69.0 → F
Luis: 69.0 → C
Mía: 81.7 → B
```


---

## JUEVES 19 · TEMAS 13 A 16: TUPLAS, DICCIONARIOS, EXCEPCIONES Y STRINGS

### Modo examen: ¿qué imprime?

#### 25. ¿Tupla o paréntesis?
```python
print(type((5)))
print(type((5,)))
print(len(("rock",)), len(("rock")))
```

#### 26. Operaciones con tuplas
```python
t = (1, 2, 3)
print(t[1:])
print(t + (4,))
print(t * 2)
```

#### 27. Agregar, cambiar y borrar claves ⚠️ Cisco
```python
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 10
del d["b"]
print(d, len(d))
```

#### 28. Recorrer un diccionario
```python
precios = {"x": 1, "y": 2}
for k, v in precios.items():
    print(k * v, end=" ")
print()
print("z" in precios, 2 in precios)
```

#### 29. Rebanadas de texto ⚠️ Cisco
```python
s = "Metallica"
print(s[0], s[-1])
print(s[2:5])
print(s[::-1])
```

#### 30. ¿Se puede cambiar una letra?
```python
s = "rock"
s[0] = "R"
print(s)
```

#### 31. El orden de los except ⚠️ Cisco
```python
try:
    print(10 / 0)
except ArithmeticError:
    print("A")
except ZeroDivisionError:
    print("B")
```

#### 32. El error que viaja hacia afuera ⚠️ Cisco
```python
def dividir(a, b):
    return a / b

try:
    print(dividir(5, 0))
except ZeroDivisionError:
    print("Atrapado afuera")
print("Fin")
```


### Taller

#### 33. 🟢 El termómetro de las reseñas
```python
positivas = ["brutal", "increíble", "épico", "bueno"]
negativas = ["aburrido", "malo", "caro", "lento"]
resenas = ["Un concierto brutal y épico", "El sonido malo y la cerveza cara",
           "Bueno pero algo lento y caro", "Ni fu ni fa"]
```
A cada reseña súmale 1 por cada palabra positiva y réstale 1 por cada negativa (sin importar mayúsculas). Clasifícala como positiva, negativa o neutral.
**Usa:** `lower()`, `split()`, `in`, `for` anidados, `if/elif/else`.
**Salida esperada:**
```
Un concierto brutal y épico → 2 (positiva)
El sonido malo y la cerveza cara → -1 (negativa)
Bueno pero algo lento y caro → -1 (negativa)
Ni fu ni fa → 0 (neutral)
```
> En una celda Markdown: ¿por qué "cara" no se contó como negativa?

#### 34. 🟡 El mensaje cifrado del backstage
Crea `cifrar(texto, n)` que recorra **cada letra** y la mueva `n` posiciones en el alfabeto (`"abcdefghijklmnopqrstuvwxyz"`), dando la vuelta al llegar a la z. Lo que no sea letra se queda igual. Con `n` negativo, descifra.
**Usa:** `for` sobre un string, `find()`, `%`, construir un string nuevo, función con `return`.
```python
secreto = cifrar("backstage a las ocho", 3)
print(secreto)
print(cifrar(secreto, -3))
print(cifrar("xyz", 3))
```
**Salida esperada:**
```
edfnvwdjh d odv rfkr
backstage a las ocho
abc
```

#### 35. 🔴 Agenda por comandos
```python
agenda = {"Ana": "555-0101"}
comandos = ["agregar Luis 555-0102", "buscar Luis", "buscar Pedro", "borrar Ana",
            "borrar Ana", "agregar Mía", "cantar"]
```
Procesa cada comando con `split()`. `agregar` guarda un contacto, `buscar` muestra el teléfono y `borrar` lo elimina con `del`. Atrapa los nombres que no existen (`KeyError`) y los comandos a los que les faltan datos (`IndexError`). Si el comando no existe, avisa.
**Usa:** diccionario, `split()`, `del`, `try` con dos `except`, `if/elif/else`.
**Salida esperada:**
```
Agregado: Luis
Luis: 555-0102
Pedro no está en la agenda
Borrado: Ana
Ana no está en la agenda
Faltan datos en: 'agregar Mía'
Comando desconocido: cantar
{'Luis': '555-0102'}
```

#### 36. 🟡 ¿Placa válida?
Una placa válida tiene el formato `LLL-NNN-L`: 3 letras, guion, 3 dígitos, guion y 1 letra. Crea `placa_valida(placa)` que primero limpie la placa (`strip()` y `upper()`) y **regrese** `True` o `False`. Prueba con la tupla de abajo y cuenta las válidas.
```python
placas = ("UAB-123-A", "qro-456-b", "AB-123-C", "XYZ-12A-D", "MOT-650-K ", "LMN123Z")
```
**Usa:** tupla, `split("-")`, `len()`, función con `return`.
💡 Pista: `"ABC".isalpha()` da `True` y `"123".isdigit()` da `True`.
**Salida esperada:**
```
'UAB-123-A': válida
'qro-456-b': válida
'AB-123-C': inválida
'XYZ-12A-D': inválida
'MOT-650-K ': válida
'LMN123Z': inválida
Válidas: 3 de 6
```


---

## VIERNES 20 · SIMULACRO MIXTO E INTEGRADORES

### Modo examen: ¿qué imprime?

#### 37. Operadores de bits ⚠️ Cisco
```python
print(5 & 3, 5 | 3)
print(5 ^ 3, 1 << 3, 16 >> 2)
```

#### 38. Caracteres especiales en strings ⚠️ Cisco
```python
print("Hola\nMundo")
print(len("a\nb"))
print('Rock "pesado"')
```

#### 39. while y for con else ⚠️ Cisco
```python
n = 3
while n > 0:
    n -= 1
else:
    print("terminó", n)
for i in range(3):
    if i == 1:
        break
else:
    print("nunca")
print("i =", i)
```

#### 40. Una lista dentro de una tupla ⚠️ Cisco
```python
t = ([1, 2], 3)
t[0].append(9)
print(t)
```

#### 41. Conversiones que engañan
```python
print(int("7") + float("2.5"))
print(int(3.99), round(2.567, 2))
print(int("3.5"))
```

#### 42. Listas por comprensión ⚠️ Cisco
```python
print([x * 2 for x in range(4)])
print([c for c in "moto" if c != "o"])
```

#### 43. Una función que modifica tu lista ⚠️ Cisco
```python
def agrega(lista):
    lista.append(1)
    return len(lista)

a = []
print(agrega(a), agrega(a))
print(a)
```

#### 44. Ciclos anidados: cuenta las vueltas
```python
c = 0
for i in range(3):
    for j in range(i):
        c += 1
print(c)
k = 0
while k < 10:
    k += 4
print(k)
```


### Taller

#### 45. 🟡 Taquilla por zonas
```python
sala = [["A"] * 5, ["B"] * 5, ["C"] * 5]
precios = {"A": 1200, "B": 800, "C": 450}
pedidos = [(0, 2), (2, 4), (0, 2), (5, 1), (1, 0)]
```
Cada pedido es una tupla `(fila, columna)`. Si el asiento existe y está libre, cóbralo según su zona y márcalo con `"X"`; si ya está vendido, avisa; si no existe, atrapa el `IndexError`. Muestra el total y la sala final sin corchetes.
**Usa:** matriz, diccionario, lista de tuplas, desempaquetar, `try/except IndexError`, `for` anidados con `end=" "`.
**Salida esperada:**
```
(0, 2) zona A: $1200
(2, 4) zona C: $450
(0, 2) ya está vendido
(5, 1) no existe
(1, 0) zona B: $800
Total vendido: $2450
A A X A A
X B B B B
C C C C X
```

#### 46. 🟡 Las palabras que más se repiten
```python
letra_cancion = """Rueda la noche, rueda el motor,
la noche es larga y el motor es mi voz.
Rueda, rueda, que la noche no acaba."""
```
Pasa el texto a minúsculas, quita comas y puntos, y cuenta cuántas veces aparece cada palabra con un diccionario. Muestra cuántas palabras distintas hay y el **top 3**, sin usar `sort()` ni `sorted()`. Si hay empate, gana la palabra que apareció primero.
**Usa:** string de varias líneas (`"""`), `replace()`, `split()`, diccionario contador, lista de "ya usadas", ciclos anidados.
**Salida esperada:**
```
Palabras distintas: 13
1. rueda (4)
2. la (3)
3. noche (3)
```

#### 47. 🟡 Servicio de la moto
```python
cada = {"aceite": 3000, "cadena": 1000, "bujías": 12000, "llantas": 15000}
ultimo = {"aceite": 21000, "cadena": 23500, "bujías": 12000, "llantas": 10000}
km = 24300
```
`cada` dice cada cuántos km toca cada servicio y `ultimo` en qué kilometraje se hizo por última vez. Crea `faltan(servicio, km_actual)` que **regrese** cuántos km faltan (puede ser negativo). Muestra el estado de cada servicio.
**Usa:** dos diccionarios con las mismas claves, función con `return`, `if/else`, número negativo.
**Salida esperada:**
```
aceite: ¡ya toca! (vencido por 300 km)
cadena: faltan 200 km
bujías: ¡ya toca! (vencido por 300 km)
llantas: faltan 700 km
```

#### 48. 🔴 Números romanos
Crea dos funciones con `return`:
- `a_romano(n)`: recorre una tupla de parejas `((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))` y, mientras `n` alcance, agrega el símbolo y resta su valor.
- `de_romano(texto)`: usa un diccionario `{"I": 1, "V": 5, ...}`. Si un símbolo vale menos que el que sigue, **réstalo**; si no, **súmalo**.

Atrapa el `KeyError` de un símbolo que no existe.
**Usa:** tupla de tuplas, desempaquetar, `while`, diccionario, índices de string, `try/except KeyError`.
**Prueba:** `1987`, `2026` y `49` a romano; `"XLII"`, `"MCMXCIX"` y `"XQ"` a número.
**Salida esperada:**
```
1987 → MCMLXXXVII
2026 → MMXXVI
49 → XLIX
XLII → 42
MCMXCIX → 1999
Símbolo inválido: 'Q'
```
