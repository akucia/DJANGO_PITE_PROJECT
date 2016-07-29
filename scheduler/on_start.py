from django.apps import AppConfig
from menu import Menu, MenuItem
from django.core.urlresolvers import reverse
class MyAppConfig(AppConfig):
	name = 'scheduler'
	verbose_name = "on_start"
	def ready(self):
		# Add two items to our main menu
		Menu.add_item("main", MenuItem("Informacje o koncie",reverse("am_userInfo"),weight=10,icon="tools"))
		Menu.add_item("main", MenuItem("zmień dane",reverse("am_changeUserdata"),weight=20,icon="report"))
		Menu.add_item("main", MenuItem("zmień hasło",reverse("am_changeUserpassword"),weight=30,icon="report"))
		Menu.add_item("main", MenuItem("twoje ankiety",reverse("am_userSurveys"),weight=40,icon="report"))
		Menu.add_item("main", MenuItem("statystyki i aktywność użytkownika",reverse("am_userActivity"),weight=50,icon="report"))
