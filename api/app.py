from aiohttp import web


def init_app() -> web.Application:
    app = web.Application()
    return app


app = init_app()
