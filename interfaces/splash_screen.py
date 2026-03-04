import flet as ft
import asyncio


def main_splash(page: ft.Page):


    bar = ft.ProgressBar(width=500, value=0, opacity=0)

    text = ft.Text(
        "MINICLINIQUE",
        size=60,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_800,
        opacity=0
    )

    logo = ft.Image(
        src="images/logo1.jpeg",
        width=380,
        height=380,
        scale=0.5,
    )

    splash_content = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.Container(
                            expand=True,
                            alignment=ft.Alignment(0.0, 0.0),
                            content=logo,
                        ),
                        ft.Row(
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[text],
                            margin=ft.margin.only(bottom=50),
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[bar],
                        ),
                    ],
                )
            ),
        ],
    )
    if not hasattr(page, 'splash_done'):
        async def animate():
        
            for i in range(101):
                logo.scale = i / 100
                page.update()
                await asyncio.sleep(0.01)
    
            for i in range(101):
                text.opacity = i / 100
                page.update()
                await asyncio.sleep(0.02)
    
            bar.opacity = 1
    
            for i in range(101):
                bar.value = i / 100
                page.update()
                await asyncio.sleep(0.06)
                
            page.go("/choice_user")
    
        page.run_task(animate)
        page.splash_done = True

    
    
    return ft.View(
        route="/",
        bgcolor = ft.Colors.WHITE,
        controls=[splash_content],
    )


# ft.app(target=main_splash)