from aiohttp import TCPConnector

from clients.abstract_client import AbstractInteractionClient


__all__ = (
    'cloudpayments_client',
)


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector()
    REQUEST_TIMEOUT = 5 * 60
    CONNECT_TIMEOUT = 10
    SERVICE = 'CloudPayments'
    BASE_URL = 'https://api.cloudpayments.ru'


cloudpayments_client = CloudPaymentsClient()
