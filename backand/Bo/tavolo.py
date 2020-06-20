from django.db import models

class Tavolo(models.Model):

    id_tavolo = models.AutoField(max_length=11, primary_key=True)
    coperti = models.IntegerField(max_length=11, default=1)
    data_ora_arrivo = models.DateTimeField()
    codice = models.Field(max_length=11, default=1)
    stato = models.Field(max_length=11, default=1)
    flag_asporto = models.Field(max_length=1, default='')


    upd_user = models.Field(blank=False)
    upd_ts = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tavoli'
        app_label = 'ristorante'

    @staticmethod
    def get_attivo(codice):
        return Tavolo.objects.get(codice=codice, stato__in=['attivo', 'vuoto'])

    @staticmethod
    def get_tavoli():
        return Tavolo.objects.filter(stato__in=['attivo', 'vuoto'], flag_asporto='').order_by('codice')



class Asporto(Tavolo):
    @staticmethod
    def get_tavoli():
        return Tavolo.objects.filter(stato__in=['attivo'], flag_asporto='S').order_by('codice')

    @staticmethod
    def crea_nuovo():
        tavolo = Tavolo()
        tavolo.flag_asporto = 'S'
        tavolo.codice = 'asporto'
        tavolo.save()
        tavolo.codice = 'A{id_tavolo}'.format(**tavolo.__dict__)
        tavolo.save()
        return tavolo

    class Meta:
        db_table = 'tavoli'
        app_label = 'ristorante'