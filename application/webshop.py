from flask import Blueprint, render_template

bp = Blueprint('shop', __name__, url_prefix='/shop', template_folder='../templates',static_folder='../static')

@bp.route('/')
def index():
    return render_template('webshop.html')

