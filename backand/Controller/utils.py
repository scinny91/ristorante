from django.http import JsonResponse

class GenericException(Exception):
    pass

def JSON_to_JS(func):
    def wrapper(*args, **kwargs):
        try:
            message = func(*args, **kwargs)
            ret = {
                'status': 200,
                'message': message
            }
        except GenericException as err:
            ret = {
                'status': 400,
                'message': str(err)
            }
        print(ret)
        return JsonResponse(ret)

    return wrapper