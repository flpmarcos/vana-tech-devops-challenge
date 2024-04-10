# Prueba Tecnica con SAM Deployment, Github Actions y AWS Lambda

El objetivo deste projecto es configurar el servicio de API en AWS utilizando AWS API Gateway, AWS Lambda Functions mientras que para el IAC vamos utilizar SAM Deployment y el pipeline Github Actions.


## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `template.yaml`: Archivo de definición de la infraestructura como código que describe la configuración de la aplicación y sus recursos en AWS.
- `lambda_api_functions/`: Directorio que contiene el código fuente de las funciones Lambda de la API.
- `README.md`: Este archivo, que proporciona información detallada sobre la solución implementada.
- `.github/workflows/`: Directorio donde queda el github workflow

## Implementación Local

Para implementar la solución, siga los siguientes pasos:

1. Clonar el Repositorio:

```
https://github.com/flpmarcos/vana-tech-devops-challenge.git
```

2. Instalar Dependencias:
```
apt-get install python3
```

3. Configurar Credenciales de AWS:
Asegúrese de tener las credenciales de AWS configuradas localmente. Puede hacerlo mediante la configuración de AWS CLI o a través de las acciones de GitHub si está utilizando CI/CD.

4. Construir la Aplicación:
```
sam build
```

5. Desplegar la Aplicación:
```
sam deploy --guided
```
Siga las instrucciones interactivas proporcionadas por sam deploy --guided para configurar la implementación.



## Implementación Github

1. Como configurar la variables
Con la cuenta creada en AWS y las credenciales en manos, crea 3 secretos en github.

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
```

2. Pipeline GitHub Actions

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


## Mantenimiento

Para el mantenimiento continuo de la aplicación, tenga en cuenta las siguientes consideraciones:

### Gestión de Dependencias

Si hay cambios en las dependencias del proyecto, asegúrese de actualizarlas y probar la aplicación localmente antes de realizar despliegues en producción.

### Seguridad

Mantenga actualizadas las políticas de seguridad y revise regularmente los permisos y configuraciones de seguridad de los recursos de AWS.

### Monitorización y Registro

Implemente la monitorización y registro adecuados para la aplicación y sus recursos en AWS. Utilice servicios como Amazon CloudWatch para monitorear métricas y registros de aplicaciones.

## Problemas - Troubleshotting
1. Error para ejecutar el pipeline 
  La mayoria de los errores son de permisos de usuario en IAM

2. Se usted intentar gravar los dados recebido en lo API Gateway y recibir este error:
  AWS CloudWatch Logs role ARN must be set error
  Use este guia:
  https://coady.tech/aws-cloudwatch-logs-arn/

  The new API Gateway UI looks a bit different. You can find the "CloudWatch log role ARN" setting in Settings, under Client Certificates in the left nav.

3. Lambda invocation failed with status: 403 on CloudWhatch Log

  