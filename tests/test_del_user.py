# # -*- coding: utf-8 -*-
from model.user import User

def test_del_user(app):
    # app.session.login(username="admin", password="secret")
    app.user.delete_first_user()
    app.session.logout()

