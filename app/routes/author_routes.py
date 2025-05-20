from flask import Blueprint, Response, abort, make_response, request
from app.models.author import Author
from .route_utilities import validate_model
from ..db import db

bp = Blueprint("bp", __name__, url_prefix="/authors")

@bp.post("")
def create_book():
    request_body = request.get_json()
    try:
        new_author = Author.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_author)
    db.session.commit()

    return new_author.to_dict(), 201

@bp.get("")
def get_all_authors():
    query = db.select(Author)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Author.title.ilike(f"%{name_param}%"))

    query = query.order_by(Author.id)
    authors = db.session.scalars(query)

    authors_response = []
    for author in authors:
        authors_response.append(author.to_dict())
    return authors_response