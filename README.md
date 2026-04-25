# Fundamentos de Programación Orientada a Objetos en Python

Proyecto educativo para estudiar los fundamentos de POO en Python.

## Objetivo

Este repositorio contiene ejemplos simples, ordenados por tema, para comprender:

- Clases
- Objetos
- Atributos
- Métodos
- Constructor `__init__`
- `self`
- Encapsulamiento
- Herencia
- Polimorfismo
- Abstracción
- Composición
- Métodos especiales o dunder methods

## Estructura del proyecto

```text
oop-python-fundamentos/
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── oop_python_fundamentals/
│       ├── basics/
│       ├── encapsulation/
│       ├── inheritance/
│       ├── polymorphism/
│       ├── abstraction/
│       ├── composition/
│       └── dunder_methods/
├── examples/
├── exercises/
├── tests/
└── docs/
```

## Cómo ejecutar el proyecto

Desde la raíz del proyecto:

```bash
python main.py
```

También puedes ejecutar ejemplos específicos desde sus propios archivos.

## Cómo ejecutar ejemplos individuales

```bash
python examples/run_all_examples.py
```

## Cómo ejecutar tests

Instala dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta los tests:

```bash
pytest
```

## Recomendación para estudiantes

Estudia los archivos en este orden:

1. `basics/car.py`
2. `basics/person.py`
3. `encapsulation/bank_account.py`
4. `inheritance/animals.py`
5. `polymorphism/payment_methods.py`
6. `abstraction/coffee_machine.py`
7. `composition/computer.py`
8. `dunder_methods/product.py`

Luego resuelve los ejercicios de la carpeta `exercises/`.
