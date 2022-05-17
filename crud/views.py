from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.handlers.wsgi import WSGIRequest
from .models import IdeaModel
from .forms import IdeaForm
from django.http import HttpResponse

# Create your views here.


"""
1. table as a homepage
2. create/add ideas to the table
3. update individual ideas from the table
4. delete individual ideas from the table
"""


# 1
def table(request: WSGIRequest) -> HttpResponse:
    """
    Renders the table of ideas
    :param request: WSGI representing the incoming http request
    :return: HttpResponse representing the ideas table
    """
    context = {'dataset': IdeaModel.objects.all()}
    return render(request, 'crud/table.html', context)


# 2
def create(request: WSGIRequest) -> HttpResponse:
    """
    Renders the creation form for new ideas
    :param request: WSGI representing the incoming http request
    :return: HttpResponse representing the creation form
    """
    context = {}
    form = IdeaForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'crud/create.html', context)


# 3
def update_idea(request: WSGIRequest, pk) -> HttpResponse:
    """
    Updates an idea from the existing table idea
    :param request: request WSGI representing the incoming https request
    :param pk: represents the id of the idea
    :return: HttpResponse representing the updating of an individual
    """
    context = {}
    model = get_object_or_404(IdeaModel, pk=pk)
    form = IdeaForm(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'crud/update.html', context)


#4
def delete_idea(request: WSGIRequest, pk) -> HttpResponse:
    """
    Deletes an idea from the idea table
    :param request: WSGI representing the incoming http response
    :param pk: represents the id of the idea
    :return: HttpResponse representing the deletion of an individual idea from the table
    """
    context = {}
    model = get_object_or_404(IdeaModel, pk)
    if request.method == 'POST':
        model.delete()
    return render(request, 'crud/delete.html', context)
