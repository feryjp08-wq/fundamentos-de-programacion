# ACTIVIDAD EVALUABLE 7 — ENTREGA FINAL DEL PROYECTO (FASE II)

**Curso:** Fundamentos de programación
**Semana:** 7 · Temas 17, 18, 19 y 20 (archivos)
**Actividad en plataforma:** 1155 - Entrega Final del Proyecto
**Ponderación:** 35% de la calificación total del curso
**Modalidad:** Individual
**Fecha límite:** viernes 27 de noviembre de 2026, 23:59 h (sin prórroga)
**Evidencia de entrega:** liga pública de **tu mismo repositorio del curso**, con la carpeta `semana7/`

> Esta semana **no hay ejercicios extra**. Los 12 ejercicios de clase son práctica y no se entregan. Toda la calificación está en tu proyecto.

---

## 1. El reto

Termina el proyecto que empezaste en el **Avance (Fase I)**: un programa que resuelve un problema real de una organización (un negocio, un taller, una tienda, una banda, un estudio…) y que ahora **guarda su información en archivos de texto**, de modo que nada se pierde al cerrarlo.

El programa se ejecuta en la terminal de VS Code (`.py`), no en un notebook.

---

## 2. Los 10 requerimientos

| # | Requerimiento | Qué debe hacer tu programa |
| :---: | :--- | :--- |
| 1 | **Identificación** | Al iniciar, pide el nombre o *nickname* del usuario. |
| 2 | **Bienvenida dinámica** | Muestra un mensaje de bienvenida formal que incluye ese nombre, armado con operaciones de strings (`+`, f-string, `title()`, etc.). |
| 3 | **Pantalla de carga** | Una **función propia** muestra un aviso de carga que se mueve en consola (barra, puntos, porcentaje) y dura **máximo 5 segundos** (`time.sleep`). |
| 4 | **Menú como matriz** | El menú principal está guardado en una **matriz** (lista de listas), se dibuja recorriéndola y se controla con un `while`. Sus opciones manejan tus archivos. |
| 5 | **Inactividad (simulada)** | Si el usuario presiona **Enter sin elegir opción**, el programa simula 10 minutos de inactividad con un **`for`** (cada vuelta = 1 minuto, con una pausa corta). Después pregunta si desea continuar: con `si` vuelve al menú y con `no` regresa a la **pantalla de inicio** (pedir el nombre otra vez). Cualquier otra respuesta se vuelve a preguntar. |
| 6 | **Fecha en tupla** | Pide la fecha de operación como `dd/mm/aaaa` y la guarda **exactamente** así: `Fecha = dia, mes, anio`. Esa fecha se escribe **automáticamente** cada vez que el programa crea un archivo o le agrega un registro. |
| 7 | **Persistencia** | Tu carpeta trae **4 o más `.txt`** con datos de tu problema. El programa: (a) **muestra** los archivos disponibles en una lista o diccionario; (b) deja **elegir uno y ver su contenido**; (c) **crea** archivos nuevos; (d) **agrega** registros a un archivo existente sin borrar lo anterior. |
| 8 | **Excepciones** | Ningún error de archivos detiene el programa: archivo que no existe, nombre mal escrito, falta de permisos y datos mal capturados (por ejemplo, la fecha) se atrapan con `try/except` y un mensaje claro. |
| 9 | **Bitácora del detective** | Documentas en el reporte **al menos 2 bugs reales** que encontraste mientras programabas, con el método del detective (ver sección 4). |
| 10 | **Comentarios de calidad** | Encabezado del programa (qué problema resuelve y quién lo hizo), comentario o *docstring* en **cada función** y comentarios en las partes difíciles. Alguien que no te conoce debería poder entender tu código. |

> 💡 Usa `encoding="utf-8"` en todos tus `open()` y ejecuta el programa abriendo en VS Code **la carpeta del proyecto**.

---

## 3. Estructura de la entrega

```
semana7/
├── proyecto/
│   ├── mi_proyecto.py          ← tu programa (ponle el nombre de tu proyecto)
│   ├── clientes.txt            ← mínimo 4 .txt con datos de TU problema
│   ├── servicios.txt
│   ├── inventario.txt
│   └── citas.txt
└── Reporte_Proyecto_Final.pdf
```

### El reporte (PDF)
| # | Sección | Qué lleva |
| :---: | :--- | :--- |
| 1 | **Portada** | Nombre, matrícula, curso, nombre del proyecto y fecha. |
| 2 | **El problema** | Organización, área, problema que resuelves y **reglas de negocio** (las restricciones con las que opera). Puedes partir de tu Avance. |
| 3 | **Diseño** | Entrada → Proceso → Salida de tu programa y un diagrama de flujo del menú principal. |
| 4 | **Mapa de requerimientos** | Una tabla con los 10 requerimientos: en qué **función** se cumple cada uno y una captura que lo demuestre. |
| 5 | **Pruebas de errores** | Capturas de al menos 3 errores atrapados: archivo inexistente, fecha mal escrita y otro a tu elección. |
| 6 | **Bitácora del detective** | Mínimo 2 bugs (ver formato abajo). |
| 7 | **Conclusiones** | Qué aprendiste, qué fue lo más difícil y qué le agregarías después. |

---

## 4. Formato de la bitácora del detective

Por cada bug:

| Campo | Ejemplo |
| :--- | :--- |
| **Síntoma** (qué viste) | "Al agregar un registro, el archivo quedaba con un solo renglón." |
| **Pista** (mensaje de error o comportamiento) | "No había error; el archivo se borraba en cada registro." |
| **Causa** (la línea culpable) | `open(nombre, "w")` en la función `anexar_registro`. |
| **Corrección** | Cambié `"w"` por `"a"`. |
| **Prueba** | Agregué dos registros y los dos aparecen (captura). |

> Son bugs **que de verdad te pasaron**. Uno que inventaste se nota y no cuenta.

---

## 5. Rúbrica (100 pts)

### Proyecto (80 pts)

| # | Criterio | Pts | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| 1–2 | **Identificación y bienvenida** | 8 | Pide el nombre y lo integra en una bienvenida formal con operaciones de strings. | Ambos, con detalles menores de formato. | Solo uno de los dos. | Ninguno. |
| 3 | **Pantalla de carga** | 4 | Función propia, aviso que se mueve, máximo 5 s. | Función correcta, pero el aviso es estático o dura un poco más. | Pausa sin función propia o sin aviso. | No existe. |
| 4 | **Menú como matriz** | 8 | Matriz + `while`; el menú se dibuja recorriendo la matriz; la opción inválida no truena. | Funciona con `while`, pero las opciones se imprimen a mano (la matriz no se usa para dibujarlo). | Menú sin matriz o sin `while`. | Sin menú. |
| 5 | **Inactividad simulada** | 8 | Enter vacío → `for` de 10 "minutos" → pregunta validada; `si` vuelve al menú y `no` a la pantalla de inicio. | Funciona, pero no valida respuestas distintas de si/no. | Falta la pregunta o `no` no regresa al inicio. | No existe. |
| 6 | **Fecha en tupla** | 8 | `Fecha = dia, mes, anio`, validada, y se escribe en **todo** archivo creado o modificado. | Tupla correcta, pero no aparece en todos los archivos. | Fecha sin tupla o sin integrarla en archivos. | No captura fecha. |
| 7 | **Persistencia** | 12 | Cumple (a), (b), (c) y (d), con 4 o más `.txt` de su problema. | Cumple 3 de 4. | Cumple 2. | Cumple 1 o ninguno. |
| 8 | **Excepciones** | 8 | Archivo inexistente, nombre mal escrito, permisos y datos mal capturados atrapados; el programa nunca se cierra solo. | Atrapa la mayoría, con detalles menores. | Solo atrapa algunos. | Sin `try/except`. |
| 9 | **Bitácora del detective** | 8 | 2 o más bugs reales con los 5 campos y prueba. | 2 bugs con algún campo incompleto. | 1 bug, o bugs sin causa ni corrección. | Sin bitácora. |
| 10 | **Comentarios** | 8 | Encabezado, docstring en cada función y comentarios en las partes difíciles. | Faltan comentarios en algunas funciones. | Comentarios escasos o que no explican nada. | Sin comentarios. |
| — | **Reporte** | 8 | PDF con las 7 secciones, mapa de requerimientos con capturas y conclusiones propias. | Completo, con detalles menores. | Le faltan secciones o capturas. | Sin reporte. |
| | **Subtotal** | **80** | | | | |

### Entrega en GitHub (20 pts)

| Criterio | Pts | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Repositorio e historial** | 20 | Mismo repositorio del curso, estructura de la sección 3, **3 o más commits** de la semana con mensajes que dicen qué cambió (`agrega menú en matriz`, `corrige modo a en anexar`). | Estructura correcta y 3 commits con mensajes poco descriptivos. | 1 o 2 commits, o archivos fuera de `semana7/proyecto/`. | Repositorio nuevo, privado o sin liga. |

**Total: 80 + 20 = 100 pts.**

---

## 6. Reglas

- **Sin prórroga.** Si algo no funciona, entrega lo que tengas y explícalo en el reporte: un requerimiento a medias suma; uno ausente, no.
- El programa debe **correr** en VS Code con la carpeta del proyecto abierta. Si no arranca por un error de sintaxis, solo se califica lo que se pueda revisar en el código y el reporte.
- Proyectos idénticos o sustancialmente iguales entre alumnos valen 0.
- Puedo pedirte que expliques cualquier parte de tu código.
- La **presentación** de este proyecto es la Actividad 8 (semana 8) y **no lleva código**: aquí se evalúa el programa; allá, cómo lo presentas.

---

## 7. Checklist antes de entregar

- [ ] Pide el nombre, da la bienvenida con ese nombre y muestra la carga (máx. 5 s).
- [ ] El menú vive en una matriz y se dibuja con un `for`.
- [ ] Enter vacío → 10 "minutos" → si/no; `no` me regresa a pedir el nombre.
- [ ] La fecha está en `Fecha = dia, mes, anio` y aparece en todo archivo que creo o modifico.
- [ ] Tengo 4 o más `.txt` con datos de mi problema; puedo verlos, abrirlos, crear uno y agregarle registros.
- [ ] Probé un archivo que no existe, una fecha mal escrita y una opción inválida: nada truena.
- [ ] Cada función tiene su comentario.
- [ ] El reporte tiene las 7 secciones y mi bitácora de 2 bugs reales.
- [ ] Todo está en `semana7/` de mi mismo repositorio, con 3 commits o más.
