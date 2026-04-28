# Fundamentos de Programación Orientada a Objetos en Python

Proyecto educativo para estudiar los fundamentos de POO en Python.

Incluye ejemplos guiados, ejercicios prácticos y pruebas automatizadas para reforzar cada concepto.

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
│   ├── test_animals.py
│   ├── test_bank_account.py
│   ├── test_car.py
│   ├── test_coffee_machine.py
│   ├── test_payment_methods.py
│   ├── test_person.py
│   └── test_product.py
└── docs/
```

## Requisitos

- Python 3.10 o superior

## Configuración del entorno

Desde la raíz del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
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

Con el entorno virtual activo:

```bash
python -m pytest -q
```

Actualmente la suite incluye pruebas para:

- Básicos (`Car`, `Person`)
- Encapsulamiento (`BankAccount`)
- Herencia (`Animal`, `Dog`, `Cat`)
- Polimorfismo (`PaymentMethod` y subclases)
- Abstracción (`CoffeeMachine`)
- Métodos especiales (`Product`)

## Recomendación para estudiantes

Estudia los archivos en este orden:

1. `src/oop_python_fundamentals/basics/car.py`
2. `src/oop_python_fundamentals/basics/person.py`
3. `src/oop_python_fundamentals/encapsulation/bank_account.py`
4. `src/oop_python_fundamentals/inheritance/animals.py`
5. `src/oop_python_fundamentals/polymorphism/payment_methods.py`
6. `src/oop_python_fundamentals/abstraction/coffee_machine.py`
7. `src/oop_python_fundamentals/composition/computer.py`
8. `src/oop_python_fundamentals/dunder_methods/product.py`

Luego resuelve los ejercicios de la carpeta `exercises/`.
