import json

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps("¡Hola desde AWS Lambda! Mi nombre es Felipe, soy brasileño pero vivo en Argentina y me encanta el mate!"),
    }
    return response
