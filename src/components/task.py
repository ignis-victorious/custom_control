#  ___________________
#  Import LIBRARIES
import flet as ft
from flet import Text, TextField, IconButton
#  Import FILES
#  ___________________


class Task(ft.Row):
    def __init__(self, text: str) -> None:
        super().__init__(controls=[])
        self.text_view = Text(value=text)
        self.text_edit = TextField(text, visible=False)
        self.edit_button = IconButton(icon=ft.Icons.EDIT, on_click=self.edit)
        self.save_button = IconButton(
            visible=False, icon=ft.Icons.SAVE, on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]
        # Row [
        # text_view = Text
        # text_edit = TextField
        # edit_button = IconButton
        # save_button = IconButton
        # controls = Checkbox
        # ]

    def edit(self, e: ft.ControlEvent) -> None:
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e: ft.ControlEvent) -> None:
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()
