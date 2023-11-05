from django.shortcuts import render, redirect, get_object_or_404

from .forms import UploadForm
from .models import Algo


def get_place(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            info = form.save()
            a = float(info.number_A)
            b = float(info.number_B)
            c = float(info.number_C)
            res = 'Оба условия не выполняются'
            if a > b > c:
                res = 'A > B > C'
            elif a < b < c:
                res = 'A < B < C'
            info.res = res
            uid = int(info.uid)
            print(res)
            print(uid)
            info.save()
            return redirect('result/' + str(uid), uid=uid)

    else:
        form = UploadForm()

    return render(request, 'AlgorithmApp/form.html', {'form': form})


def get_result(request, uid):
    result = get_object_or_404(Algo, uid=uid)
    context = {
        'result': result.res,
        'A': result.number_A,
        'B': result.number_B,
        'C': result.number_C,
    }
    return render(request, 'AlgorithmApp/result.html', context=context)
