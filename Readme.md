# Prueba de concepto de Health Checks en Docker

El objetivo de esta prueba de concepto es mostrar como se puede configurar el health check en Docker y como se puede hacer para que un contenedor se reinicie automaticamente una vez detecta que no esta "saludable".

## Construcción de la imagen

```shell
docker build -t docker-health-check .
```

## Ejecución de la imagen creada anteriormente
A esta imagen se le comprueba la "salud" con el health check
```shell
docker run -d --rm --name docker-health-check --label autoheal=true -p 5000:5000 docker-health-check
```

Es necesario especificar el label ```--label autoheal=true``` para que la imagen autoheal lo encuentre


## Ejecución de la imagen autoheal
Esta imagen es usada para reiniciar los contenedores "no saludables"
```shell
docker run -d --rm --name autoheal -e AUTOHEAL_CONTAINER_LABEL=all -v /var/run/docker.sock:/var/run/docker.sock willfarrell/autoheal
```

## Comprobar la salud de la imagen
```shell
docker inspect --format='{{json .State.Health}}' docker-health-check 
```

```shell
docker ps
```

## Como se usa?

La aplicación cuanta con diferentes URL's que permiten interactuar con la misma

```/``` Retorna el estado HTTP de la aplicación. 200 saludable, 500 no saludable

```/down``` Permite cambiar el estado de la aplicación de 200 a 500.

```/up``` Permite cambiar el estado de la aplicación de 500 a 200.

Una vez estén corriendo los dos contenedores es necesario hacer un llamado a ```/down``` para ponerlo "no saludable"

```shell
curl localhost:5000/down -v
```

Esto cambiará el estado de la aplicación y una vez el health check de Docker tenga tres intentos fallidos de verificar la salud, el contenedor sera reiniciado automaticamente.

## Mayor información

```shell
https://github.com/willfarrell/docker-autoheal
```