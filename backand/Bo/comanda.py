from django.db import models
from backand.Bo.menu import Menu

class Comanda(models.Model):
    id_comanda = models.AutoField(max_length=11, primary_key=True)
    id_tavolo = models.IntegerField(max_length=11)
    id_piatto = models.IntegerField(max_length=11)

    portata = models.Field(max_length=11, default=1)
    stato = models.Field(max_length=11, default='inserito')

    ins_ts = models.DateTimeField(auto_now=True)
    upd_ts = models.DateTimeField(auto_now=True)
    upd_user = models.Field(max_length=11)


    class Meta:
        db_table = 'comande'
        app_label = 'ristorante'


    @staticmethod
    def get_comande_tavolo(id_tavolo):
        lista_comande = Comanda.objects.filter(id_tavolo=id_tavolo).order_by('portata')

        count = 0
        for com in lista_comande:
            com.piatto = Menu.get(com.id_piatto)
            count += 1
            com.count = count

        return lista_comande