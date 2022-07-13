from aiohttp import TCPConnector

from clients.abstract_client import AbstractInteractionClient


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector()
    REQUEST_TIMEOUT = 5 * 60
    CONNECT_TIMEOUT = 10
    SERVICE = 'CloudPayments'
    BASE_URL = 'https://api.cloudpayments.ru'
