import email.utils
import functools
import operator

import flask

from . import timeline
from ..import utils
from application import app

@app.route("/rss")
def home_rss():
    params = utils.parse_params()
    params["include_entities"] = 1
    data = timeline.timeline("Home", functools.partial(flask.g.api.getHomeTimeline, **params))
    data["results"].sort(key=operator.itemgetter("id"), reverse=True)
    data["now"] = email.utils.formatdate()
    resp = flask.make_response(flask.render_template("rss.xml", **data))
    resp.headers["Content-Type"] = "application/rss+xml"
    return resp

