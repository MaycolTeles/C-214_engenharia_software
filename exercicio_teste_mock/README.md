# Executando

## Summary

* [Requirements](#requirements)
* [Setup and Installation](#setup-installation)
* [How to Use](#how-to-use)

*********************
## Requirements <a name="requirements"></a>

* [Python 3.6+](https://www.python.org/)
* Pip 20.0+ (comes with Python 3)

*********************
## Setup and Installation <a name="setup-installation"></a>

### Creating the Virtual Environment and Installing Dependencies

It is recommended to install the dependencies inside a [virtualenv](https://docs.python.org/3/tutorial/venv.html). You have to create a virtual environment, then activate it, and finally install all the dependencies.

If you don't know how to do that, <b>no worries!</b> Just follow [this guide](docs/set_up_virtual_environment.md) and you'll be fine!

*********************

## How To Use <a name="how-to-use"></a>

If you want to run all the tests, you can do this using the `Makefile` by running:

```
make tests
```

Or if you can't run a `Makefile`, you can type either of the following commands from whithin the same directory this file is (i.e.: $<YOUR_PATH>/C-214_engenharia_software/exercicio_test_mock)

```
python -m pytest
```

or even

```
python3 -m pytest
```

and it should work.

### Note
In case the commands above doesn't work, make sure that you are running them from whithin your virtual environment!