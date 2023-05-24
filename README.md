# Introducción

MVC en construcción para una hamburguesería. Se usa las siguientes herramientas:

- [Flask](https://flask.palletsprojects.com/en/2.3.x/http:// "Flask")
- SGBD MySQL

# Instalación

Una vez clonamos el repositorio:

1. Creamos el entorno virtual:
<p>Linux:</p>

```bash
python3 -m venv .venv
```

<p>Windows:</p>

```bash
py -3 -m venv .venv
```

2. Activamos el entorno virtual:
<p>Linux:</p>

```bash
. .venv/bin/activate
```

<p>Windows:</p>

```bash
.venv\Scripts\activate
```

3. Instalamos las dependencias:
<p>Flask:</p>

```bash
pip install Flask
```

<p>MySQL:</p>

```bash
pip install pymysql
```

<p>Cryptograph:</p>

```bash
pip install cryptography
```

4. Creamos un archivo de configuracion (cfg.py) para la conexión a la base de datos, agregando las siguientes variables:

```
host = 'host'
port = 1111
db = 'nombre_bd'
username = 'user'
password = 'password'
```

**DESDE EL ARCHIVO APP.PY CORREMOS EL PROYECTO**
