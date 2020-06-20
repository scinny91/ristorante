from django.db import models

class Menu(models.Model):
    id_piatto = models.AutoField(max_length=11, primary_key=True)
    nome_piatto = models.Field(max_length=50)
    categoria = models.Field(max_length=15)
    prezzo = models.DecimalField(default=0)
    stato = models.Field(max_length=11, default=1)
    ins_ts = models.DateTimeField(auto_now=True)
    upd_user = models.Field(blank=False)
    upd_ts = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'menu'
        app_label = 'ristorante'

    def to_css(self):
        self.btn = 'success' if self.stato == 'valido' else 'danger'

    @staticmethod
    def get(id_piatto):
        return Menu.objects.get(id_piatto=id_piatto)

    @staticmethod
    def get_lista(ordinabili=False):
        ret = None
        if ordinabili:
            ret = Menu.objects.filter(stato__in=('valido', 'terminato'))
        return ret