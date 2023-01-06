# Desafío Backend

Trabajo desarrollado por Valentín Giorgetti. Funcionalidades implementadas:

- Se implementó una serie de endpoints para consultar información.

- Se lleva un registro de todas las queries ejecutadas en el archivo `queries.log` (dentro del directorio "FriendsLessonsSystem").

- Se implementó un middleware para añadir un header a cada request recibido.

- Se implementó un middleware para registrar cada request recibido en una colección de MongoDB.

- Se implementó envío de emails asincrónicos.

- Se integró una API externa para consultar las condiciones climáticas actuales de la ciudad de La Plata.

## Pasos para ejecutar el proyecto

1. Clonar el repositorio y ubicarse dentro del directorio "FriendsLessonsSystem".

2. Crear un archivo `.env`, y definir las siguientes variables de entorno:

 > En el email de la entrega se encuentra adjuntado este archivo con las credenciales necesarias.

 - Conexión a la base de datos PostgreSQL: 
 
    - **DB_NAME**
    - **DB_USER**
    - **DB_PASSWORD**
    - **DB_HOST** 
    - **DB_PORT**
 
 - Conexión a la base de datos MongoDB:
 
    - **MONGODB_URI**
    - **MONGODB_NAME**
    - **MONGODB_REQUESTS_LOG_COLLECTION_NAME**
 
 - Configuración para envío de emails asincrónicos: 
 
    - **EMAIL_HOST_USER** 
    - **EMAIL_HOST_PASSWORD**
    
 - API key para integración con API externa:
 
    - **ACCUWEATHER_API_KEY**

3. Iniciar un entorno virtual de Python e instalar las dependencias del proyecto.

 - Para iniciar un entorno virtual de Python usando `venv`, primero descargarlo con el comando `pip install venv`, luego crear el entorno con el comando `python venv mi_entorno` y finalmente activarlo con el comando `mi_entorno_virtual\Scripts\activate.bat` (en Windows) o `source mi_entorno_virtual/bin/activate` (en sistemas basados en Unix).
 
 - Para instalar las dependencias del proyecto utilizar el comando `pip install -r requirements.txt`.
 
4. Iniciar los servicios de PostgreSQL y MongoDB.

5. Ejecutar el comando `python manage.py test` para correr los tests y verificar que funcionen correctamente.

6. Ejecutar el comando `python init_db.py` para inicializar la base de datos PostgreSQL con algunos datos de ejemplo.

7. Ejecutar el comando `python manage.py runserver` para iniciar el servidor.

### Envío de emails asincrónicos

Se configuró el sistema para que cada 2 minutos envíe un email a la dirección ejemplobackend@mail.com. 

> Las instrucciones y credenciales necesarias necesarias para acceder al correo se encuentran adjuntadas en el email de la entrega.

Para comenzar a enviar los emails, ubicarse en el directorio "FriendsLessonsSystem" y seguir los siguientes pasos:

1. Iniciar un servidor RabbitMQ.

1. Abrir una consola y ejecutar el comando `celery -A FriendsLessonsSystem worker --pool=solo -l info`.

2. Abrir otra consola ejecutar el comando `celery -A FriendsLessonsSystem beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`.

Para dejar de enviar emails cerrar ambas consolas.

Ejemplo de email recibido:

![Ejemplo de email recibido](https://i.imgur.com/xz6bYRx.png "Ejemplo de email recibido")

### Listado de endpoints

- `GET /api/users/`: retorna un listado con todos los usuarios. Ejemplo:

```json
[
  {
    "id": 1,
    "first_name": "Joe",
    "last_name": "Smith",
    "username": "joe123",
    "birth_date": "2000-01-01"
  },
  {
    "id": 2,
    "first_name": "Mark",
    "last_name": "Johnson",
    "username": "mark456",
    "birth_date": "1999-12-31"
  },
  {
    "id": 3,
    "first_name": "Jody",
    "last_name": "Williams",
    "username": "jody789",
    "birth_date": "1998-12-30"
  },
  {
    "id": 4,
    "first_name": "Rachel",
    "last_name": "Smith",
    "username": "rachel246",
    "birth_date": "1997-12-29"
  }
]
```

- `GET /api/users-friends-list/`: retorna un listado con todos los usuarios y su lista de amigos. Ejemplo:

```json
[
  {
    "id": 1,
    "friends": [
      {
        "id": 2,
        "first_name": "Mark",
        "last_name": "Johnson",
        "username": "mark456",
        "birth_date": "1999-12-31"
      },
      {
        "id": 3,
        "first_name": "Jody",
        "last_name": "Williams",
        "username": "jody789",
        "birth_date": "1998-12-30"
      },
      {
        "id": 4,
        "first_name": "Rachel",
        "last_name": "Smith",
        "username": "rachel246",
        "birth_date": "1997-12-29"
      }
    ],
    "first_name": "Joe",
    "last_name": "Smith",
    "username": "joe123",
    "birth_date": "2000-01-01"
  },
  {
    "id": 2,
    "friends": [
      {
        "id": 1,
        "first_name": "Joe",
        "last_name": "Smith",
        "username": "joe123",
        "birth_date": "2000-01-01"
      }
    ],
    "first_name": "Mark",
    "last_name": "Johnson",
    "username": "mark456",
    "birth_date": "1999-12-31"
  },
  ...
]
```

- `GET /api/user-friends/<int:pk>/`: retorna al usuario identificado por el ID ingresado y su lista de amigos. Ejemplo:

```json
{
  "id": 1,
  "friends": [
    {
      "id": 2,
      "first_name": "Mark",
      "last_name": "Johnson",
      "username": "mark456",
      "birth_date": "1999-12-31"
    },
    {
      "id": 3,
      "first_name": "Jody",
      "last_name": "Williams",
      "username": "jody789",
      "birth_date": "1998-12-30"
    },
    {
      "id": 4,
      "first_name": "Rachel",
      "last_name": "Smith",
      "username": "rachel246",
      "birth_date": "1997-12-29"
    }
  ],
  "first_name": "Joe",
  "last_name": "Smith",
  "username": "joe123",
  "birth_date": "2000-01-01"
}
```

- `GET /api/user-lessons-taken/<int:pk>/`: retorna al usuario identificado por el ID ingresado y una lista que indica los cursos en los que ha tomado una o más lecciones. Ejemplo:

```json
{
  "id": 4,
  "courses": [
    {
      "course": {
        "id": 1,
        "name": "Math",
        "description": "Math course"
      },
      "lessons_taken": 3
    },
    {
      "course": {
        "id": 2,
        "name": "Spanish",
        "description": "Spanish course"
      },
      "lessons_taken": 2
    }
  ],
  "first_name": "Rachel",
  "last_name": "Smith",
  "username": "rachel246",
  "birth_date": "1997-12-29"
}
```

- `GET /api/courses/`: retorna un listado con todos los cursos. Ejemplo:

```json
[
  {
    "id": 1,
    "name": "Math",
    "description": "Math course"
  },
  {
    "id": 2,
    "name": "Spanish",
    "description": "Spanish course"
  }
]
```

- `GET /api/courses/<int:pk>/`: retorna al curso identificado por el ID ingresado. Ejemplo:

```json
{
  "id": 1,
  "name": "Math",
  "description": "Math course"
}
```

- `GET /api/get-current-weather-conditions/`: retorna las condiciones climáticas actuales de la ciudad de La Plata, utilizando la API pública de AccuWeather. Ejemplo:

```json
{
  "LocalObservationDateTime": "2023-01-04T20:35:00-03:00",
  "WeatherText": "Clear",
  "HasPrecipitation": false,
  "PrecipitationType": null,
  "Temperature": {
    "Metric": {
      "Value": 22.0,
      "Unit": "C",
      "UnitType": 17
    },
    "Imperial": {
      "Value": 72.0,
      "Unit": "F",
      "UnitType": 18
    }
  }
}
```

### Ejemplo de registro de requests recibidos y registrados en MongoDB

```json
{ 
    "_id" : "ObjectId('63b5fb916b8890e518ce8ca5')", 
    "method" : "GET", 
    "path" : "/api/users/", 
    "headers" : {
        "Content-Length" : "", 
        "Content-Type" : "text/plain", 
        "Accept-Encoding" : "gzip, deflate, br", 
        "Accept" : "*/*", 
        "User-Agent" : "Thunder Client (https://www.thunderclient.com)", 
        "Host" : "127.0.0.1:8000", 
        "Connection" : "close", 
        "My-Header" : "Hello"
    }, 
    "body" : {

    }
}
{ 
    "_id" : "ObjectId('63b5fbfd6b8890e518ce8ca7')", 
    "method" : "GET", 
    "path" : "/api/user-lessons-taken/4/", 
    "headers" : {
        "Content-Length" : "", 
        "Content-Type" : "text/plain", 
        "Accept-Encoding" : "gzip, deflate, br", 
        "Accept" : "*/*", 
        "User-Agent" : "Thunder Client (https://www.thunderclient.com)", 
        "Host" : "127.0.0.1:8000", 
        "Connection" : "close", 
        "My-Header" : "Hello"
    }, 
    "body" : {

    }
}
```