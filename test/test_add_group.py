from fixture.application import Application
from model.group import Group
import pytest


@pytest.fixture
def app():
    fixture = Application()
    #request.addfinalizer(fixture.destroy())
    #return fixture
    yield fixture
    fixture.destroy()


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group(name="study", header="good", footer="Not friends"))
    app.group.open_group_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.open_group_page()
    app.session.logout()


