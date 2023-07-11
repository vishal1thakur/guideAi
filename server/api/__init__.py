
from flask import Blueprint

api = Blueprint('api', __name__)

# this has to be at the bottom to avoid circular imports
from . import prompts, documents
