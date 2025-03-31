# SOUČÁSTÍ APLIKACE (OBCHOD) - ZOBRAZÍ SE PO PŘIHLÁŠENÍ UŽIVATELE
from flask import Blueprint, render_template, session, flash, redirect, url_for

from application import db_execute
from application.login import login_required

bp = Blueprint('shop', __name__, url_prefix='/shop', template_folder='../templates',static_folder='../static')


@bp.route('/')
@login_required
def index():
    product_command = "SELECT name, price FROM products"
    results = db_execute(product_command)
    print(results)
    return render_template('webshop.html', results=results)

