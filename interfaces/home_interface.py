import flet as ft

import asyncio
import sys

sys.path.append('../')
from interfaces.splash_screen import main_splash

def main_home(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    
    def route_change(route) -> None:
        print("Route : ", page.route),
        page.views.clear()
         
        page.views.append(main_splash(page))
        

        if page.route == "/choice_user":
            page.views.append(
                ft.View(
                    route="/choice_user",
                    bgcolor = ft.Colors.WHITE,
                    padding = 0,
                    controls=[ft.Text("choice_user")],
                )
            )

    
    page.update()
    
    def view_pop(e):
         if len(page.views) > 1:
             page.views.pop()
             top_view = page.views[-1]
             page.go(top_view.route)
             page.bgcolor = ft.Colors.WHITE
             


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change(None)   
    
    
ft.run(main_home)