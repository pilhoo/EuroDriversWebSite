from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from reportlab.pdfgen import canvas
from django.http import HttpResponse,HttpResponseRedirect
from models import *
from myforms import UserAddOpinionForm
import datetime
from django.core.context_processors import csrf
from django.utils.translation import ugettext as _

def main(request):
    if not 'lang_id' in request.session:
        request.session['lang_id']=1
    t=loader.get_template("main_page.html")
    trans_lang_ids=([trans.lang_id_id for trans in Translation.objects.all()])
    # TODO session
    news_site=1 # TODO delete
    news_from=(news_site-1)*5
    act_lang=request.session['lang_id']
    c=Context({
        'page_lang': act_lang,
        'transl_langs': Language.objects.filter(id__in=trans_lang_ids),
        'all_langs': Language.objects.all(),
        'news': NewsTranslation.objects.filter(lang_id=act_lang)[news_from:news_from+5],
        'opinions': Opinion.objects.all(), # TODO lang filter
    })
    return HttpResponse(t.render(c))


def addOpinion(request):
    if request.POST:
        form=UserAddOpinionForm(request.POST)

        if form.is_valid():
            opinion=Opinion(author=form.cleaned_data['author'],
                            text=form.cleaned_data['text'],
                            lang_id=form.cleaned_data['lang_id'],
                            pub_date=datetime.date.today())
            opinion.save()
            return HttpResponseRedirect('../')
    else:
        form=UserAddOpinionForm()

    if not 'lang_id' in request.session:
        request.session['lang_id']=1
    trans_lang_ids=([trans.lang_id_id for trans in Translation.objects.all()])
    act_lang=request.session['lang_id']

    c=locals()
    c.update(csrf(request))
    return render_to_response('add_opinion.html', c)


def setlang(request, lang_id):
    request.session["lang_id"]=lang_id
    return HttpResponseRedirect('../')


def comments_to_pdf(request):
    response=HttpResponse(mimetype='application/pdf')
    response['Content-Disposition']='attachment; filename=comments.pdf'

    comments=Opinion.objects.all()

    p=canvas.Canvas(response)
    i=0
    for c in comments:
        p.drawString(30,800-i*30, c.pub_date.__str__())
        p.drawString(100,800-i*30, c.author)
        p.drawString(30,790-i*30, c.text)
        i+=1
    p.showPage()
    p.save()

    return response