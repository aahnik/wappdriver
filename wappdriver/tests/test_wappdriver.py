'''
Tests the core features of WappDriver
'''
import pytest


@pytest.fixture
def bot():
    from .. import WappDriver
    bot = WappDriver()
    return bot


def test_text(bot):
    assert bot.send_message(to='aahnik', msg='success')


def test_media():
    pass


def test_url():
    pass


def test_contact():
    pass
