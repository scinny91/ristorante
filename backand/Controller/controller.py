from backand.Bo.tavolo import Tavolo, Asporto
from backand.Bo.menu import Menu

import itertools
from operator import itemgetter

class MenuController():
    def __init__(self):
        self.tavoli = Tavolo.get_tavoli()
        self.asporto = Asporto.get_tavoli()


class TavoloController():

    @staticmethod
    def load(codice):
        dati_out = {}

        if not codice:
            obj_tavolo = Asporto.crea_nuovo()
        else:
            obj_tavolo = Tavolo.get_attivo(codice)
        piatti_menu = Menu.objects.filter(stato__in=('valido','terminato'))

        menu = []
        piatti = []
        for i in piatti_menu:
            i.to_css()
            piatti.append(i.__dict__)
        grouper = itemgetter('categoria')
        for k, c in itertools.groupby(sorted(piatti, key=grouper), key=grouper):
            menu.append({
                'categoria': k.title(),
                'piatti': list(c),
            })

        dati_out['tavolo'] = obj_tavolo.__dict__
        dati_out['menu'] = menu

        #print(dati_out)
        return dati_out