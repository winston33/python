# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    yield fixture
    fixture.destroy()


def test_delete_first_group(app):
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.delete_first()
    app.group.open_group_page()
    app.session.logout()

