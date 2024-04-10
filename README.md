# Prueba Tecnica con SAM Deployment, Github Actions y AWS Lambda

El objetivo deste projecto es configurar el servicio de API en AWS utilizando AWS API Gateway, AWS Lambda Functions mientras que para el IAC vamos utilizar SAM Deployment y el pipeline Github Actions.


## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `template.yaml`: Archivo de definición de la infraestructura como código que describe la configuración de la aplicación y sus recursos en AWS.
- `lambda_api_functions/`: Directorio que contiene el código fuente de las funciones Lambda de la API.
- `README.md`: Este archivo, que proporciona información detallada sobre la solución implementada.
- `.github/workflows/`: Directorio donde queda el github workflow

## Implementación Local - WSL Debian Linux

Para implementar la solución, siga los siguientes pasos:

1. Clonar el Repositorio:

```
https://github.com/flpmarcos/vana-tech-devops-challenge.git
```

2. Cómo instalar Python 3 y herramientas de AWS en Linux Debian

## 2.1 Instalar Python 3:

```bash
sudo apt update
sudo apt install python3
```

## 2.2 Verificar la instalación de Python 3:

```bash
python3 --version
```

## 2.3 Instalar el gestor de paquetes pip para Python 3:

```bash
sudo apt install python3-pip
```

## 2.4 Instalar AWS CLI:

```bash
pip3 install awscli --upgrade --user
```

## 2.5 Verificar la instalación de AWS CLI:

```bash
aws --version
```

## 2.6 Instalar Docker:

```bash
sudo apt install docker.io
```

## 2.7 Agregar su usuario al grupo Docker (opcional):

```bash
sudo usermod -aG docker $USER
```

## 2.8. Cerrar sesión y volver a iniciar sesión:

Esto es necesario para que los cambios en el grupo surtan efecto.

## 2.9. Instalar AWS SAM CLI:

```bash
sudo apt install curl
curl -L "https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip" -o sam.zip
sudo apt install unzip
sudo unzip sam.zip -d /usr/local/bin/
```

## 2.10. Verificar la instalación de AWS SAM CLI:

```bash
sam --version
```

Con estos pasos, tendrás Python 3, AWS CLI y AWS SAM CLI instalados en tu sistema Linux Debian. Asegúrate de configurar tus credenciales de AWS usando el comando `aws configure` después de instalar AWS CLI, y estarás listo.


3. Configurar Credenciales de AWS:
Asegúrese de tener las credenciales de AWS configuradas localmente. Puede hacerlo mediante la configuración de AWS CLI con variables de entorno en linux.

4. Construir la Aplicación:
```
cd vana-tech-devops-challenge
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

  