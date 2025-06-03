#  ___________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, Column
#  Import FILES
#  ___________________


class MyButton(ft.ElevatedButton):
    def __init__(self, text: str, on_click: ft.OptionalControlEventCallable) -> None:
        super().__init__(
            text=text,
            on_click=on_click,
            bgcolor=ft.Colors.ORANGE_300,
            color=ft.Colors.GREEN_800,
        )


def main(page: Page) -> None:
    page.title = "https://flet.dev/docs/getting-started/custom-controls/"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    mum_text = Text(value="Hello Mum", size=50)

    def ok_clicked(e: ft.ControlEvent) -> None:
        print("OK clicked")

    def cancel_clicked(e: ft.ControlEvent) -> None:
        print("Cancel clicked")

    page.add(
        Column(
            controls=[
                MyButton(text="OK", on_click=ok_clicked),
                mum_text,
                MyButton(text="Cancel", on_click=cancel_clicked),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    app(main)


#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________
