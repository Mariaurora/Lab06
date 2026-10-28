from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        conn=get_connection()
        if conn is not None:
            cursore_dizionario = conn.cursor(dictionary=True)
            query = """SELECT *
                            FROM strumento"""
            cursore_dizionario.execute(query)
            lista_strumenti = []
            # itero nel database e ogni riga la trasformo in un oggetto di tipo strumento
            for riga in cursore_dizionario:
                strumento = Strumento(riga['codice'], riga['tipo'], riga['marca']
                                      , int(riga['anno_acquisto']), float(riga['valore']), riga['disponibile'])
                lista_strumenti.append(strumento)
            if lista_strumenti == []:
                return None
            else:
                return lista_strumenti
        else:
            return None


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        conn=get_connection()
        cursore_dizionario=conn.cursor(dictionary=True)
        query=""" SELECT *
                  FROM strumento
                  WHERE tipo = %s"""
        cursore_dizionario.execute(query, (tipo,))
        lista_strumenti_per_tipo=[]
        for riga in cursore_dizionario:
            strumento = Strumento(riga['codice'], riga['tipo'], riga['marca']
                                  , int(riga['anno_acquisto']), float(riga['valore']), riga['disponibile'])
            lista_strumenti_per_tipo.append(strumento)

        if lista_strumenti_per_tipo==[]:
            return None
        else:
            return lista_strumenti_per_tipo


