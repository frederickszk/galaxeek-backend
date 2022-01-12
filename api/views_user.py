from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import api.models
from api.models import *
from api.serializers import *


@api_view(['POST'])
def login(request):
    try:
        login_name = request.data['user']
        login_password = request.data['password']
        print(login_name, login_password)
        user = User.objects.get(name=login_name)
        if login_password == user.password:
            return Response({"status": "ok", "msg": "Log in successfully.", "user_id": user.id},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "msg": "Wrong password."},
                            status=status.HTTP_400_BAD_REQUEST)
    except api.models.User.DoesNotExist:
        return Response({"status": "error", "msg": "The user does not exist"},
                        status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response({"status": "error", "msg": "Please check the request body format."},
                        status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({"status": "error", "msg": "Unknown exception."},
                        status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['POST'])
# def login(request):
#     # try:
#     # print(request.data)
#     login_name = request.data['user']
#     login_password = request.data['password']
#     print(login_name, login_password)
#     user = User.objects.get(name=login_name)
#     if login_password == user.password:
#         return Response({"status": "ok", "msg": "Log in successfully.", "user_id": user.id},
#                         status=status.HTTP_200_OK)
#     else:
#         return Response({"status": "error", "msg": "Wrong password."},
#                         status=status.HTTP_400_BAD_REQUEST)
#     # except api.models.User.DoesNotExist:
#     #     return Response({"status": "error", "msg": "The user does not exist"},
#     #                     status=status.HTTP_400_BAD_REQUEST)
#     # except KeyError:
#     #     return Response({"status": "error", "msg": "Please check the request body format."},
#     #                     status=status.HTTP_400_BAD_REQUEST)
#     # except Exception:
#     #     return Response({"status": "error", "msg": "Unknown exception."},
#     #                     status=status.HTTP_400_BAD_REQUEST)
