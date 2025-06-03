
#  ___________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, SafeArea, Container
#  Import FILES
#  ___________________


def main(page: Page):
    text = Text("Hello Mum", size=50)

    
    page.add(
        SafeArea(
            Container(
                text,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


if __name__ == "__main__":
    app(main)


#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________
