import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_strumenti(self,e):
        self._view.lista_strumenti.controls.clear()
        if self._model.get_strumenti() is None:
             self._view.alert.show_alert('Il DATABASE non contiene strumenti oppure non si è stabilita la connessione')
        for strumento in self._model.get_strumenti():
            stato = "✅" if strumento.disponibile else "⛔"
            self._view.lista_strumenti.controls.append(ft.Text(f"{stato} {strumento}"))
        self._view.update()

    def cerca_strumenti_per_tipo(self,e):
        self._view.lista_strumenti_ricerca.controls.clear()
        tipo=self._view.input_tipo_strumento.value
        if self._model.cerca_strumenti_per_tipo(tipo) is None:
            self._view.alert.show_alert(f'La ricerca per strumenti di tipo "{tipo}" non ha prodotto risultati')
        else:
           self._view.lista_strumenti_ricerca.controls.append(ft.Text(f'----STRUMENTI DI TIPO {tipo}---- '))
           for strumento in self._model.cerca_strumenti_per_tipo(tipo):
             stato = "✅" if strumento.disponibile else "⛔"
             self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"{stato} {strumento}"))

        self._view.update()

