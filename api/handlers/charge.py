import base64

from aiohttp.web import json_response

from api.schemas import ChargeSchema
from clients.abstract_client import InteractionResponseError
from clients.clients import cloudpayments_client


async def charge_payment(request):
    charge_schema = ChargeSchema()
    data = await request.json()
    charge_schema.validate(data)

    # Yandex Pay Token передается в формате Base64, поэтому его нужно декодировать
    data['CardCryptogramPacket'] = str(base64.b64decode(data.pop('Token')))
    url = cloudpayments_client.endpoint_url('payments/cards/charge')

    try:
        headers = {'Authorization': request.headers['Authorization']}
        response_data = await cloudpayments_client.post('charge', url, json=data, headers=headers)
    except InteractionResponseError as e:
        return json_response(dict(success=False, error=dict(message=e.message)), status=400)

    return json_response(response_data)
