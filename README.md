# Prueba Tecnica con SAM Deployment, Github Actions y AWS Lambda

El objetivo deste projecto es configurar el servicio de API en AWS utilizando AWS API Gateway, AWS Lambda Functions mientras que para el IAC vamos utilizar SAM Deployment y el pipeline Github Actions.

## IAC - AWS SAM
Utilizando SAM para el IAC


## Como configurar la variables
Con la cuenta creada en AWS y las credenciales en manos, crea 3 secretos en github.

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
```


## Pipeline GitHub Actions

Para el pipeline tenemos dos workflows y dos branch (Develop y Production), Cuando la branch develop sufre cambio el workflow abajo es activado.

`.github/workflows/pre-build.yml` file:
```
on:
  push:
    branches:
      - develop
```

Este workflow hace el test pero no hace el deploy, para hacer el deploy es necesario hacer un pull request para lá branch production.

Mientra echo el pull request el trigger es activado llamando el workflow abajo

`.github/workflows/build.yml` file:
```
on:
  push:
    branches:
      - production
```

### En que tener dos workflows ayuda ?
Tener dos workflows ayuda en que antes que se a hecho el deploy tenga un estagio para el test. 

