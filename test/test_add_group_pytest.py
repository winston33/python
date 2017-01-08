# -*- coding: utf-8 -*-
import pytest

from fixture.application_pytest import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    #request.addfinalizer(fixture.destroy())
    #return fixture
    yield fixture
    fixture.destroy()


def test_add_group(app):
    app.session.login("admin", "secret")
    app.open_group_page()
    app.group.create(Group(name="study", header="good", footer="Not friends"))
    app.open_group_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.open_group_page()
    app.geoup.create(Group(name="", header="", footer=""))
    app.open_group_page()
    app.session.logout()
