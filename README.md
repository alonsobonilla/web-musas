# Introducción 
MVC en construcción para una hamburguesería. Se usa las siguientes herramientas:
- [Flask](https://flask.palletsprojects.com/en/2.3.x/http:// "Flask")
- SGBD MySQL 
# Instalación
Una vez clonamos el repositorio:
1) Creamos el entorno virtual:
<p>Linux:</p>

 ```bash
python3 -m venv .venv
```
<p>Windows:</p>

```bash
py -3 -m venv .venv
```
2) Activamos el entorno virtual:
<p>Linux:</p>

```bash
. .venv/bin/activate
```
<p>Windows:</p>

```bash
.venv\Scripts\activate
```
3) Instalamos las dependencias:
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
pip install cryptograph
```
4) Creamos un archivo de configuracion (config.ini) para la conexión a la base de datos, siguiendo el siguiente modelo :
```
[database]
host = localhost
port = numero_del_puerto
database_name = nombre_de_la_base_de_datos
username = usuario 
password = contraseña
```
**DESDE EL ARCHIVO APP.PY CORREMOS EL PROYECTO**
