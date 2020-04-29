# filename: main.py, request handler (aiohttp) for interacting with stellar obs
import stellarobservatory as so
import json
from aiohttp import web

# define simple handler function
async def handle(request):

    nodes = so.nodes.get_nodes_from_stellarbeat()
    print(nodes)
    nodes_by_public_key = so.nodes.get_nodes_by_public_key(nodes)
    print(nodes_by_public_key)
    # dependencies_trans = nodes.get_node_dependencies(nodes_by_public_key, 'E')
    # print(dependencies_trans)
    # dependencies_intrans = nodes.get_node_dependencies(nodes_by_public_key, 'E', dependencies=set(), transitive=False)
    # print(dependencies_intrans)
    # graph = so.nodes.get_trust_graph(nodes_by_public_key)
    # print(graph)
    # strcc = scc.get_strongly_connected_components(graph)
    # print(strcc)
    response_obj = { 'status' : 'successful', 'graph' : nodes }

    return web.Response(text=json.dumps(response_obj))

# create app object
app = web.Application()
app.router.add_get('/', handle)

# run app
web.run_app(app)
