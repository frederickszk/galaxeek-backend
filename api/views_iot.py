from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer


from api.models import *
from api.serializers import *

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkiotda.v5.region.iotda_region import IoTDARegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


@api_view(['POST'])
def positions(request):
    if request.method == 'POST':
        data_iot = request.data['notify_data']['body']['services'][0]["properties"]
        serializer = PositionSerializer(data=data_iot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def action(request):
    ak = "O675URS3YGS85V3JHROC"
    sk = "vA51D8QI0IkpadHEV5hENgFjFfRYGty7GPVfH9XI"
    credentials = BasicCredentials(ak, sk)
    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IoTDARegion.CN_NORTH_4) \
        .build()

    try:
        device_id = request.GET.get('device_id')
        device_id_iot = Device.objects.get(pk=device_id).device_id_iot
        print(device_id_iot)

        # 实例化请求对象
        request_iot = CreateCommandRequest()
        # Implement the device_id_iot fetch here
        paras = {"command_para": 1}
        # paras_json = JSONRenderer().render(paras)

        request_iot.device_id = device_id_iot
        request_iot.body = DeviceCommandRequest(
            # service_id="basic_data",
            # command_name="command",
            paras=paras
        )
        #
        response = client.create_command(request_iot)
        # request = ListProductsRequest()
        # response = client.list_products(request)

        print(response)
        return Response(response.to_json_object())
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
