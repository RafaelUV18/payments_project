# Payments Project

Este proyecto se utiliza para procesar los pagos que recibe una empresa en archivos de tipo Excel. 
El propósito de este proyecto es demostrativo y tiene muchas oportunidades de mejora.

## Instalación

Para correr este proyecto y que funcione adecuadamente, se necesita realizar lo siguiente:

1. Clona este repositorio.
2. Instalar las dependencias que se encuentran en el archivo requirements.txt (Se recomienda usar un entorno virtual)
```
pip install -r requirements.txt
```
3. Levantar el servidor desde la carpeta raíz del proyecto con:
```
uvicorn main:app --reload
```

## Uso del proyecto

Para probar los endpoints del proyecto se recomienda hacer uso de la documentación auto generada con swagger:
    http://127.0.0.1:8000/docs


## Aspectos considerados para la implementación de la solución
Una vez comprendida la problematica, se tomó en consideración los siguientes puntos a desarrollar:

1. En este caso se observa que los 3 archivos de Excel que se reciben poseen las mismas cabeceras en el mismo orden. Se asumirá que el orden de las cabeceras podría cambiar, pero no los nombres de las mismas. Por ello al momento de scrapear la información se hará con base en los nombres de las cabeceras. 
2. Ya que se guardará información bancaria, la cual (haremos la suposición) no puede ser incorrecta o nula, al momento de subir los archivos se buscarán errores y se regresarán al usuario, no permitiendo subir la información en la base de datos hasta que esté bien, ya que no se considera que subir información incompleta o errónea en este contexto sea lo ideal. 
3. Creación de endpoints que devuelvan toda la información en general, tanto en formato json por la facilidad de pintar los datos en una página que consuma este endpoint, como descargando un archivo excel con los mismos.
4. Creación de endpoint que devuelta el monto total de los pagos realizados.
5. Creación de endpoint solo para verificar que el servicio esté activo.

## Tecnologías utilizadas

1. El programa fué desarrollado con Python 3.9.
2. Para el desarrollo del API se utilizó FastAPI, este framework encajaba muy bien con los requerimientos del proyecto
3. Para el scrapeo de los Excel se utilizó Pandas.
4. Ya que la problemática era sencilla a nivel de relaciones en base de datos se optó por usar SQLite para una rápida configuración.

## Flujo del sistema

El flujo para utilizar el sistema planteado para el uso del sistema sería el siguiente:
1. Acceder a la URL con la documentación de los endpoint, esto después de haber de haber levantado el servidor con los pasos
previstos en el apartado de instalación: http://127.0.0.1:8000/docs
2. Utilizar el endpoint: /payments/upload para subir los archivos a scrapear, en caso de que un archivo tenga algún error,
no se cargarán. Se recomienda corregir el dato incorrecto con lo que devuelva el endpoint y volver a intentar subir los archivos.
3. Una vez cargados los archivos los demás endpoints ya podrán devolver información.


## Propuestas de mejora

1. Se utilizó SQLite por su facilidad y rápida configuración, pero con un proyecto a gran escala sin duda se tendría que optar por una base de datos más robusta y un diseño más complejo.
2. Se dejaron de fuera elementos de seguridad que no se deberían de omitir en este tipo de servicios con este tipo información.
3. El almacenamiento de la base de datos está limitado, al cargar la tabla de los pagos se eliminan los registros anteriores. Esto supone que, si se quieren ver los pagos de los 3 archivos de Excel, se deberían de cargar todos en el array de string ítems en una sola llamada al endpoint.
4. Dependiendo de las exigencias del proyecto sería beneficioso considerar el utilizar bases de datos NoSQL.
5. Es importante definir un estándar en los archivos que procesará el programa, ya que si el usuario manda archivos con columnas incorrectas se tendrán problemas al hacer uso del mismo.
6. Podría ser muy conveniente implementar un filtro de búsqueda de la información almacenada en base de datos, esto suponiendo que cada vez se tendrá más información y será más difícil para el usuario recuperarla. Se sugeriría hacer un filtrado, por cada una de las columnas que poseen los archivos.
7. Seria conveniente correr este programa haciendo uso de Docker, con ello se evitarán posibles problemas de versiones o compatibilidad.

## Autor

* **Rafael Vázquez Castillo** - *Desarrollo* - [Rafael](https://github.com/RafaelUV18)




