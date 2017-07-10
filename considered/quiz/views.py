# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('quiz', __name__, url_prefix='/quiz', static_folder='../static')


@blueprint.route('/')
@login_required
def start():
    """Start a quiz"""
    return render_template('quiz/start.html')