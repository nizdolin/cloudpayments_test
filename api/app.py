import os

from aiohttp import web
from aiohttp_basicauth import BasicAuthMiddleware

from api.handlers import charge_payment
from api.middlewares import validation_middleware


def init_app() -> web.Application:
    # https://developers.cloudpayments.ru/#autentifikatsiya-zaprosov
    auth_middleware = BasicAuthMiddleware(
        username=os.environ.get('PUBLIC_ID'),
        password=os.environ.get('API_SECRET'),
    )
    application = web.Application(middlewares=[auth_middleware, validation_middleware])
    application.router.add_post('/api/charge/', charge_payment)
    return application


app = init_app()
