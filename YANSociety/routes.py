import timeago
import os
import secrets
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

def time_ago_format(post):
    return timeago.format(post.date_posted, datetime.now())

