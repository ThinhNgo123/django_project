import jwt
from django.http import JsonResponse
from datetime import datetime
import random

blacklist = []

def token_destroy(request):
    blacklist.append(request.headers['Authorization'])

def check_exp(exp: datetime):
    # print("now:", datetime.now())
    # print("exp:", exp)
    return datetime.now() < exp

def authenticate_token(api_callback):
    def inner_func(request, *args, **kwargs):
        # print(request.headers['Authorization'])
        token = request.headers['Authorization']
        if token in blacklist:
            raise jwt.InvalidTokenError("loi gia tri token")
        else:
            pass
        try:
            # print(request.user)
            pay_load = jwt.decode(token, 'secret_key', algorithms=['HS256'])
            if pay_load["username"] != request.user:
                raise jwt.InvalidTokenError("khong hop le")
            # print(type(pay_load["username"]))
            if not pay_load.get("exp", None):
                raise jwt.InvalidTokenError("khong hop le")
            # if not check_exp(datetime.fromtimestamp(pay_load["exp"])):
            #     raise jwt.ExpiredSignatureError
            return api_callback(request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return JsonResponse("token het han", safe=False)
        except jwt.InvalidTokenError as e:
            return JsonResponse(e.args[0], safe=False)
    return inner_func

def get_security():
    security = ""
    for _ in range(5):
        security += str(random.randint(10000, 10000000))
    print("security:", security)
    return security