from django.contrib import admin
from eurodrivers_app.models import *
from myforms import TranslationForm
import os

class TranslationAdmin(admin.ModelAdmin):
    form=TranslationForm

    def save_model(self, request, obj, form, change):
    #		lang_id=Language.objects.get(id=obj.lang_id).lang_id
        lang=Language.objects.get(id=obj.lang_id_id)
        f=open("locale/%s.po"%lang.lang_id, mode='w')
    #		TODO zapisywanie do pliku .po
        f.write("msgid \"News\"\n")
        f.write("msgstr \"%s\"\n\n"%form.cleaned_data["news"])
        f.write("msgid \"Opinions\"\n")
        f.write("msgstr \"%s\"\n\n"%form.cleaned_data["opinions"])

        os.system("django-admin.py compilemessages")
        obj.save()


class NewsTransInline(admin.StackedInline):
    model=NewsTranslation
    extra=1


class NewsIdAdmin(admin.ModelAdmin):
    inlines=[NewsTransInline]


admin.site.register(News, NewsIdAdmin)
admin.site.register(Opinion)
admin.site.register(Translation, TranslationAdmin)
#admin.site.register(Language)