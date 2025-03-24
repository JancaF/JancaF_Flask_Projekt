from flask import Blueprint, render_template, session, flash, redirect, url_for

from application.login import login_required

bp = Blueprint('shop', __name__, url_prefix='/shop', template_folder='../templates',static_folder='../static')


@bp.route('/')
@login_required
def index():
    return render_template('webshop.html')

