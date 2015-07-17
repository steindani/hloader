from __future__ import absolute_import

from hloader.api.v1 import app
from hloader.db.DatabaseManager import DatabaseManager
from flask import Response, json, redirect, request

@app.route('/api')
def api_index():
    # This route must be redirected to a suitable version of the HLoader API
    # In future the API may well be extended/changed, and backward
    # compatibility will guarantee that things don't break.

    # Redirect to HLoader API v1
    return redirect('/api/v1', code=302)

@app.route('/api/v1')
def api_index_default():
    return "This is the landing page for the HLoader REST API v1"


@app.route('/api/v1/HL_SERVERS')
def api_HL_SERVERS():
    s_id = request.args.get('server_id')
    address = request.args.get('server_address')
    port = request.args.get('server_port')
    name = request.args.get('server_name')

    # print(DatabaseManager.meta_connector.get_servers())

    return "Not implemented!"

    #return Response(json.dumps(connector.get_servers(server_id=s_id,
    #                                                 server_name=name,
    #                                                 server_port=port,
    #                                                 server_address=address), indent=4), mimetype='application/json')
