from django import forms
from captcha.fields import CaptchaField
from models import Opinion, Translation, Language
import os

class TranslationForm(forms.ModelForm):
    news=forms.CharField(max_length=50)
    opinions=forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(TranslationForm, self).__init__(*args, **kwargs)
        if Language.objects.filter(id=self.instance.lang_id_id).count():
            lang=Language.objects.get(id=self.instance.lang_id_id).lang_id
            eval(self.parsePoFile(lang))


    def parsePoFile(self, lang_id):
        os.system("django-admin.py make messages -l %s"%lang_id)
        f=open("locale/%s.po"%lang, mode='r')
        flines=f.readlines()
        return "self.initial.update({'news': flines[1][8:-2], 'opinions': flines[4][8:-2]})"

    class Meta:
        model=Translation
        exclude=('i18n_file',)


class UserAddOpinionForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=Opinion
        exclude=('pub_date')