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


## Troubleshotting
1. Error para ejecutar el pipeline 
  La mayoria de los errores son de permisos.


2. AWS CloudWatch Logs role ARN must be set error
  https://coady.tech/aws-cloudwatch-logs-arn/

  The new API Gateway UI looks a bit different. You can find the "CloudWatch log role ARN" setting in Settings, under Client Certificates in the left nav.

3. Lambda invocation failed with status: 403. Lambda request id:
  https://repost.aws/questions/QUH0wdOjJ6Re6_o5lOoNRvzw/lambda-invocation-failed-with-status-403-on-new-aws-region