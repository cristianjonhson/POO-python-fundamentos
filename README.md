# Fundamentos de Programación Orientada a Objetos en Python

Proyecto educativo para estudiar los fundamentos de POO en Python.

Incluye ejemplos guiados, ejercicios prácticos y pruebas automatizadas para reforzar cada concepto.

## Comandos rápidos

```bash
# Configuración
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

# Pruebas
python -m pytest -q

# Cobertura (por módulo)
python -m pytest --cov=oop_python_fundamentos --cov-report=term-missing -q
```

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
- Métodos especiales (dunder)

## Estructura del proyecto

```text
oop-python-fundamentos/
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── oop_python_fundamentos/
│       ├── basicos/
│       ├── encapsulamiento/
│       ├── herencia/
│       ├── polimorfismo/
│       ├── abstraccion/
│       ├── composicion/
│       └── metodos_especiales/
├── examples/
├── exercises/
├── tests/
│   ├── test_animals.py
│   ├── test_bank_account.py
│   ├── test_car.py
│   ├── test_coffee_machine.py
│   ├── test_computer.py
│   ├── test_payment_methods.py
│   ├── test_person.py
│   ├── test_product.py
│   ├── test_product_with_property.py
│   └── test_students.py
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

## Cómo ejecutar pruebas

Con el entorno virtual activo:

```bash
python -m pytest -q
```

## Cómo medir la cobertura

Este proyecto usa `pytest-cov` para reportar cobertura de forma numérica por módulo.

Ejecuta:

```bash
python -m pytest --cov=oop_python_fundamentos --cov-report=term-missing -q
```

Si quieres un informe HTML navegable:

```bash
python -m pytest --cov=oop_python_fundamentos --cov-report=html -q
```

El informe se genera en la carpeta `htmlcov/`.

Actualmente el conjunto de pruebas incluye:

- Básicos (`Car`, `Person`)
- Encapsulamiento (`BankAccount`, `ProductWithProperty`)
- Herencia (`Animal`, `Dog`, `Cat`, `Student`)
- Polimorfismo (`PaymentMethod` y subclases)
- Abstracción (`CoffeeMachine`)
- Composición (`Computer`, `Processor`, `Memory`)
- Métodos especiales (`Product`)

## Recomendación para estudiantes

Estudia los archivos en este orden:

1. `src/oop_python_fundamentos/basicos/car.py`
2. `src/oop_python_fundamentos/basicos/person.py`
3. `src/oop_python_fundamentos/encapsulamiento/bank_account.py`
4. `src/oop_python_fundamentos/herencia/animals.py`
5. `src/oop_python_fundamentos/polimorfismo/payment_methods.py`
6. `src/oop_python_fundamentos/abstraccion/coffee_machine.py`
7. `src/oop_python_fundamentos/composicion/computer.py`
8. `src/oop_python_fundamentos/metodos_especiales/product.py`

Luego resuelve los ejercicios de la carpeta `exercises/`.
