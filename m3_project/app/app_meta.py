from django.conf.urls import url

from objectpack import desktop

from .controller import controller
from .actions import action_packs


def register_urlpatterns() -> list:
	"""
	Регистрация конфигурации урлов для приложения
	"""
	return [url(*controller.urlpattern)]


def register_actions() -> list:
	"""
	Регистрация экшен-паков
	"""
	return controller.packs.extend(action_packs)

def register_desktop_menu() -> None:
	"""
	регистрация элементов рабочего стола
	"""
	desktop.uificate_the_controller(
    	    controller,
    	    menu_root=desktop.MainMenu.SubMenu('Demo')
	)
