from flask import Blueprint, Response, abort, make_response, request
from app.models.author import Author
from .route_utilities import validate_model
from ..db import db

bp = Blueprint("bp", __name__, url_prefix="/authors")