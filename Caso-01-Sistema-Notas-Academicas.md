# 📘 Caso de Estudio 01: Sistema de Notas Académicas

## Información General

| Campo | Detalle |
|------|---------|
| Asignatura | Programación Orientada a Objetos |
| Duración | 20 minutos |
| Nivel | Básico |
| Herramientas | Python 3.10+, editor de texto/IDE |

## Contexto
La Secretaría Académica de la universidad necesita un sistema para llevar las notas de los estudiantes de manera ordenada. Las notas se registran por estudiante y por asignatura, y se debe poder calcular el promedio de cada estudiante.

## Objetivo
Diseñar un modelo de clases que permita guardar estudiantes, asignaturas y notas, y luego implementar ese modelo en Python.

## Estructura de directorios sugerida
- `modelo/`
  - `estudiante.py`
  - `asignatura.py`
  - `nota.py`
  - `registro_notas.py`
- `uml/`
  - `caso_04_notas.puml`
- `main.py`

## 1. Análisis / Abstracción

### Narrativa
- El sistema debe registrar estudiantes con su matrícula y nombre.
- Debe registrar asignaturas con código y nombre.
- Cada nota une a un estudiante con una asignatura y una calificación numérica.
- Se solicita obtener el promedio de notas de un estudiante.

### Tareas de análisis
- Identifica las entidades principales.
- Para cada entidad, lista sus atributos.
- Escribe los comportamientos que necesita cada entidad.

### Entidades sugeridas
- `Estudiante` → matrícula, nombre
- `Asignatura` → código, nombre
- `Nota` → estudiante, asignatura, calificación
- `RegistroNotas` → lista de estudiantes, lista de asignaturas, lista de notas

## 2. Diseño / Modelado de clases

### Relaciones esperadas
- `Nota` referencia a `Estudiante` y a `Asignatura`.
- `RegistroNotas` administra los objetos `Estudiante`, `Asignatura` y `Nota`.

### Modelo mínimo
- `Estudiante`
- `Asignatura`
- `Nota`
- `RegistroNotas`

### Métodos propuestos
- `RegistroNotas.agregar_estudiante(matricula, nombre)`
- `RegistroNotas.agregar_asignatura(codigo, nombre)`
- `RegistroNotas.registrar_nota(matricula, codigo_asignatura, calificacion)`
- `RegistroNotas.promedio_estudiante(matricula)`
- `RegistroNotas.obtener_notas_estudiante(matricula)`

## 3. Implementación en Python

### Requisitos mínimos
- Usa atributos privados (`self._...`) y propiedades.
- Implementa las clases con los métodos propuestos.
- Modela las clases UML en PlanTUML antes de codificar.
- Crea un `main.py` que:
  1. registre 2 estudiantes,
  2. registre 2 asignaturas,
  3. agregue 3 notas,
  4. muestre el promedio de un estudiante.

### Preguntas de comprobación
- ¿Qué entidad representa una calificación?
- ¿Por qué `Nota` no es solo un número?
- ¿Qué clase se encarga de buscar estudiantes y asignaturas?

---

## Resultado esperado
Un programa Python que guarda estudiantes, asignaturas y notas, y calcula el promedio de un estudiante mediante un modelo orientado a objetos.
