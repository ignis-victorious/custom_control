#  ___________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, Column

#  Import FILES
from components.task import Task
#  ___________________


def main(page: Page) -> None:
    page.title = "https://flet.dev/docs/getting-started/custom-controls/"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    mum_text = Text(value="Hello Mum", size=50, color=ft.Colors.YELLOW_400)

    page.add(
        Column(
            controls=[
                Task(text="Do laundry"),
                mum_text,
                Task(text="Cook dinner"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )


if __name__ == "__main__":
    app(target=main)


#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________
