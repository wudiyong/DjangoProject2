from django.shortcuts import render
from django.db.models import Q
from models import Publisher
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (Q(name__icontains=query)|Q(city__icontains=query))
        results = Publisher.objects.filter(qset).distinct()
    else:
        results = []
    return render(request, 'App1/search.html', {'results':results,'query':query})
