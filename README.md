# Fundamentos de Programación Orientada a Objetos en Python

Este proyecto educativo está diseñado para aprender los fundamentos de POO en Python de forma progresiva.

Incluye ejemplos guiados, ejercicios prácticos, comentarios explicativos en los módulos y pruebas automatizadas para reforzar cada concepto.

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

# Lint
ruff check .
```

## Objetivo

En este repositorio encontrarás ejemplos simples, organizados por tema, para comprender:

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
├── docs/
│   └── study_guide.md
├── examples/
│   └── run_all_examples.py
├── exercises/
│   ├── exercise_01_person.py
│   ├── exercise_02_car.py
│   ├── exercise_03_bank_account.py
│   ├── exercise_04_inheritance.py
│   └── exercise_05_product.py
├── src/
│   └── oop_python_fundamentos/
│       ├── __init__.py
│       ├── abstraccion/
│       │   ├── __init__.py
│       │   └── coffee_machine.py
│       ├── basicos/
│       │   ├── __init__.py
│       │   ├── car.py
│       │   └── person.py
│       ├── composicion/
│       │   ├── __init__.py
│       │   └── computer.py
│       ├── encapsulamiento/
│       │   ├── __init__.py
│       │   ├── bank_account.py
│       │   └── product_with_property.py
│       ├── herencia/
│       │   ├── __init__.py
│       │   ├── animals.py
│       │   └── students.py
│       ├── metodos_especiales/
│       │   ├── __init__.py
│       │   └── product.py
│       └── polimorfismo/
│       │   ├── __init__.py
│       │   └── payment_methods.py
└── tests/
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
```

## Requisitos

- Python 3.10 o superior

## Configuración del entorno

Ejecuta estos comandos desde la raíz del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Cómo ejecutar el proyecto

Ejecuta el proyecto desde la raíz con:

```bash
python -m main
```

También puedes ejecutar ejemplos específicos desde sus propios archivos para practicar cada tema por separado.

## Cómo ejecutar ejemplos individuales

```bash
python -m examples.run_all_examples
```

## Cómo ejecutar pruebas

Con el entorno virtual activo, ejecuta:

```bash
python -m pytest -q
```

## Cómo medir la cobertura

Este proyecto usa `pytest-cov` para reportar cobertura numérica por módulo.

Para ver cobertura en consola, ejecuta:

```bash
python -m pytest --cov=oop_python_fundamentos --cov-report=term-missing -q
```

Si quieres un informe HTML navegable, ejecuta:

```bash
python -m pytest --cov=oop_python_fundamentos --cov-report=html -q
```

El informe se genera en la carpeta `htmlcov/`.

Actualmente, el conjunto de pruebas cubre:

- Básicos (`Car`, `Person`)
- Encapsulamiento (`BankAccount`, `ProductWithProperty`)
- Herencia (`Animal`, `Dog`, `Cat`, `Student`)
- Polimorfismo (`PaymentMethod` y subclases)
- Abstracción (`CoffeeMachine`)
- Composición (`Computer`, `Processor`, `Memory`)
- Métodos especiales (`Product`)

## Recomendación para estudiantes

Para estudiar el contenido de forma progresiva, revisa los archivos en este orden:

1. `src/oop_python_fundamentos/basicos/car.py`
2. `src/oop_python_fundamentos/basicos/person.py`
3. `src/oop_python_fundamentos/encapsulamiento/bank_account.py`
4. `src/oop_python_fundamentos/herencia/animals.py`
5. `src/oop_python_fundamentos/polimorfismo/payment_methods.py`
6. `src/oop_python_fundamentos/abstraccion/coffee_machine.py`
7. `src/oop_python_fundamentos/composicion/computer.py`
8. `src/oop_python_fundamentos/metodos_especiales/product.py`

Después, resuelve los ejercicios de la carpeta `exercises/`.
