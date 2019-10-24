import json
from datetime import datetime

from flask import request, jsonify, make_response
from werkzeug.exceptions import BadRequest, Unauthorized

from Prefix2_App import app, db
from Prefix2_App.models import PrefixClassDefaults, Prefix


@app.route("/prefix", methods=["GET"])
def get_prefix():
    prefix_class = request.args.get("class")

    if prefix_class and len(prefix_class) == 1:
        next_available_prefix = Prefix.query.filter_by(prefix=prefix_class.upper()).one()
        max_prefix = PrefixClassDefaults.query.with_entities(PrefixClassDefaults.end)\
            .filter_by(prefix=prefix_class.upper()).scalar()

        if next_available_prefix and next_available_prefix.next < max_prefix:
            next_prefix = next_available_prefix.next
            next_available_prefix.next += 1
            db.session.commit()
            print("LALALALAL")
            return make_response(json.dumps({"prefix": next_prefix, "generated_at": str(datetime.utcnow())}))
        else:
            raise Unauthorized("Prefix for this class has been exausted")

    else:
        raise BadRequest("Invalid or No class provided in the request")
