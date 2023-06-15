from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Avg, Min, Max
from .forms import UploadForm
from .models import Place


def get_place(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            info = form.save()
            number = int(info.number)
            side = 'Нижнее' if number % 2 else 'Верхнее'
            place = 'Боковое' if 37 <= number <= 54 else 'В купе'
            info.side = side
            info.location = place
            info.save()
            return redirect('result/' + str(number), number=number)

    else:
        form = UploadForm()

    return render(request, 'AlgorithmApp/form.html', {'form': form})


def get_result(request, number):
    result = get_object_or_404(Place, number=number)
    context = {
        'number': result.number,
        'side': result.side,
        'location': result.location,

    }
    return render(request, 'AlgorithmApp/result.html', context=context)


def get_results_and_stats(request):
    results = Place.objects.filter(side__exact="Верхнее").order_by("number")
    context = {
        "results": results,
        'stats': results.all().aggregate(Max('number'), Min('number'), Avg('number'))
    }
    return render(request, 'AlgorithmApp/results.html', context=context)
