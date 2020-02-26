# filename: main.py, basic request handler using aiohttp

from aiohttp import web                
import json

async def handle(request):           # we define handler function
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))

app = web.Application()              # we create app object
app.router.add_get('/', handle)

web.run_app(app)

