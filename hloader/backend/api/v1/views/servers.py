import json
from flask import request, Response

from hloader.backend.api import app
from hloader.db.DatabaseManager import DatabaseManager




@app.route('/api/v1/servers')
def api_v1_servers():
    """

    :return: Server list
    """
    kwargs = {k: request.args[k] for k in
              ('server_id', 'server_address', 'server_port', 'server_name', 'limit', 'offset') if k in request.args}
    session = DatabaseManager.meta_connector.create_session()
    servers = DatabaseManager.meta_connector.get_servers(_session=session, **kwargs)

    result = map_(servers)

    return Response(json.dumps(result, indent=4), mimetype="application/json")


def filter_(servers):
    """

    :param servers:
    :return: Filtered server list
    """
    return servers


def map_(servers):
    """

    :param servers:
    :return:
    """
    result = {"servers": []}
    for server in servers:
        s = {
            "server_id": server.server_id,
            "server_address": server.server_address,
            "server_port": server.server_port,
            "server_name": server.server_name
        }

        result["servers"].append(s)

    return result
