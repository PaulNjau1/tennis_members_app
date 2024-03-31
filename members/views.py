
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }

    return HttpResponse(template.render(context, request))


def details(request,id):
    mymember = Member.objects.get(id=id)
    template=loader.get_template("details.html")
    context={
            'mymember':mymember,
        }

    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    mydata = Member.objects.all().order_by('-firstname').values()
    columndata = Member.objects.values_list("firstname")
    rowdata = Member.objects.filter(firstname='Emil').values()
    orrowdata= Member.objects.filter(firstname='Emil') | Member.objects.filter(firstname='Paul')
    template=loader.get_template('template.html')
    context = {
        'fruits':['Apple','Banana','Cherry'],
        'mymembers':mydata,
        "columndata":columndata,
        "rowdata":rowdata,
        "orrowdata":orrowdata,
    }

    return HttpResponse(template.render(context,request))


# Create your views here.
