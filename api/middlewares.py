from aiohttp.web import json_response
from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
from marshmallow.exceptions import ValidationError


@middleware
async def validation_middleware(request: Request, handler):
    try:
        return await handler(request)
    except ValidationError as e:
        return json_response(dict(success=False, error=e.messages), status=400)
