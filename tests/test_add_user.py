# # -*- coding: utf-8 -*-
from model.user import User

def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(User(value='Ratata'))
    app.session.logout()

