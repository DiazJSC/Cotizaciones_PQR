# Cambios y mejoras realizados al código inicial de la empresa PQR

# Cambios: 
1. Se crean dos funciones "calcular_valor_vidrio" y "calcular_valor_aluminio" con el objetivo de hacer los cálculos de dimensiones y costos según la entrevista de requerimientos realizados, esto permite tener un código más limpio y sin funciones sobrantes. (ventana.py)
2. Se organizan los 'return's' de las 5 funciones para que unicamente retornen valores y no texto o elementos estaticos. (ventana.py)
3. Se implementan líneas de código para la lectura del archivo JSON y la obtención de los datos de los diccionarios que hay dentro de este. 
4. Se implementa la biblioteca "Rich" para que su ejecución por consola sea más legible y visualmente atractiva. 
5. Se modifica la función "calular_total" para que dentro de esta se haga directamente el cálculo de la cotización total, según la cantidad de ventanas y un descuento si se superan las 100 ventanas. (cotizacion.py)
6. Se implementan línes de código para una transformación de los valores ingresados por el usuario con el objetivo no afectar su búsqueda dentro de los diccionarios que se encuentran en el archivo JSON (main.py)

# Mejoras
1. Se implementa un archivo JSON para el almacenamiento de los precios, medidas o estilos, esto con el objetivo de que la empresa pueda cambiar o implementar valores sin necesidad de manipular el código fuente y evitando errores humanos. (datos.json)
2. Se crea la función "mostrar_cotizacion" para generar de una manera más estructurada la cotización que solicita el cliente, basandose en lo solicitado inicialmente. (cotización.py)
3. Se crea una nueva opción para el usuario 'Ver tarifas' esto con el objetivo de que el usuario pueda visualizar los precios de la empresa y así realizar una cotización basada en sus posibilidades financieras. 