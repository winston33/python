# -*- coding: utf-8 -*-
from application_pytest import ApplicationPytest
from group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = ApplicationPytest()
    #request.addfinalizer(fixture.destroy())
    #return fixture
    yield fixture
    fixture.destroy()


def test_test_add_group(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_group(Group(name="study", header="good", footer="Not friends"))
    app.open_group_page()
    app.log_out()


def test_test_add_empty_group(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_group(Group(name="", header="", footer=""))
    app.open_group_page()
    app.log_out()