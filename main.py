# filename: main.py, request handler (aiohttp) for interacting with stellar obs
import stellarobservatory as so
import json
from aiohttp import web

# define simple handler function
async def handle(request):

    nodes = so.nodes.get_nodes_from_stellarbeat()
    nodes_by_public_key = so.nodes.get_nodes_by_public_key(nodes)
    # graph = so.nodes.get_trust_graph(nodes_by_public_key)
    # strcc = so.utils.scc.get_strongly_connected_components(graph)
    response_obj = { 'status' : 'successful', 'nodes_by_pubkey' : nodes_by_public_key }

    return web.Response(text=json.dumps(response_obj))

# create app object
app = web.Application()
app.router.add_get('/', handle)

# run app
web.run_app(app)
