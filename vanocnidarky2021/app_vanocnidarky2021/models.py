from django.db import models

# Create your models here.
class Uzivatel(models.Model):
    id_uzivatel = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    heslo = models.CharField(max_length=50)
    fb_id = models.CharField(max_length=80)
    google_id = models.CharField(max_length=80)
    aktivni = models.BooleanField(default=False)
    aktivovany = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Uzivatel'


class Instituce(models.Model):
    id_instituce = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=100)
    kontaktni_osoba = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    heslo = models.CharField(max_length=50)
    telefon = models.CharField(max_length=20)
    web = models.CharField(max_length=80)
    fb_stranka = models.CharField(max_length=80)
    ulice = models.CharField(max_length=60) 
    cislo = models.IntegerField()
    psc = models.IntegerField()
    mesto = models.CharField(max_length=50)
    ic = models.CharField(max_length=15)
    dic = models.CharField(max_length=20)
    popis_instituce = models.CharField(max_length=200)
    email_instrukce = models.CharField(max_length=200)
    email_podekovani = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Instituce'

class Obdarovany(models.Model):
    id_obdarovani = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    vek = models.IntegerField()
    medailonek = models.CharField(max_length=150)
    prani = models.CharField(max_length=100)
    prani_url = models.URLField(max_length=200)
    instituce = models.ForeignKey(Instituce, on_delete=models.SET_NULL, null=True)
    darce = models.ForeignKey(Uzivatel, on_delete=models.SET_NULL, null=True)
    prani_splneno = models.BooleanField(default=None)

    class Meta:
        verbose_name_plural = 'Obdarovany'
