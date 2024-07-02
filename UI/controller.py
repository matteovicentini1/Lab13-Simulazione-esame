import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        anni = self._model.getanni()
        for i in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(i))
        forme = self._model.getforme()
        for i in forme:
            self._view.ddshape.options.append(ft.dropdown.Option(i))

    def handle_graph(self, e):
        if self._view.ddyear.value is None:
            self._view.create_alert('inserire anno')
            return
        if self._view.ddshape.value is None:
            self._view.create_alert('inserire forma')
            return
        self._view.txt_result.controls.clear()

        self._model.creagrafo(self._view.ddshape.value,self._view.ddyear.value)
        self._view.txt_result.controls.append(ft.Text(f'Numero di vertici: {self._model.getnodi()}, numero di archi {self._model.getarchi()}'))
        lista = self._model.listastati()
        for i in lista:
            self._view.txt_result.controls.append(
                ft.Text(f'Nodo {i[0]}, somma pesi su archi {i[1]}'))

        self._view.update_page()

    def handle_path(self, e):
        pass