from django.db import models

class Language(models.Model):
    lang_id=models.CharField(max_length=8)
    name=models.CharField(max_length=50)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.lang_id)


class Translation(models.Model):
    lang_id=models.ForeignKey(Language)
    i18n_file=models.URLField(max_length=64)

    def sentence1(self):
        return "cokolwiek"

    def __unicode__(self):
        return Language.objects.get(id=self.lang_id_id).__unicode__()


class Opinion(models.Model):
    lang_id=models.ForeignKey(Language)
    text=models.TextField()
    author=models.CharField(max_length=50)
    pub_date=models.DateField()

    def __unicode__(self):
        return "(%s) [%s] %s - %s" % (Language.objects.get(id=self.lang_id_id).name, self.pub_date.__str__(), self.author, self.text)


class News(models.Model):
    pub_date=models.DateField()

    class Meta:
        verbose_name_plural="News" # TODO gettext

    def countTranslations(self):
        return NewsTranslation.objects.filter(news_id=self.id).count()

    def translations(self):
        return [Language.objects.get(id=news.lang_id_id).lang_id for news in NewsTranslation.objects.filter(news_id=self.id)]

    def firstTitle(self):
        return NewsTranslation.objects.filter(news_id=self.id)[0]

    def __unicode__(self):
        trans_str=','.join([trans for trans in self.translations()])
        return "[%s] %s (%s)" % (self.pub_date.__str__(), self.firstTitle(),trans_str)


class NewsTranslation(models.Model):
    lang_id=models.ForeignKey(Language)
    title=models.CharField(max_length=100)
    text=models.TextField()
    news_id=models.ForeignKey(News)

    def pub_date(self):
        return News.objects.get(id=self.news_id_id).pub_date

    def __unicode__(self):
        return "(%s) %s" % (self.lang_id.lang_id, self.title)