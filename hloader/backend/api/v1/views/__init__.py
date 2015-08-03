from flask import url_for
from werkzeug.utils import redirect
from hloader.backend.api import app

__author__ = 'dstein'

from hloader.backend.api.v1.views import index
from hloader.backend.api.v1.views import headers
from hloader.backend.api.v1.views import secret
from hloader.backend.api.v1.views import servers
from hloader.backend.api.v1.views import packages
from hloader.backend.api.v1.views import auth

# @app.route('/<path:path>')
# def index(path):
#     return redirect(url_for('api_v1') + "/" + path)