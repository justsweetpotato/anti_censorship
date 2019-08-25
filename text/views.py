from django.shortcuts import render
from .data import anti_censor


def index(request):
    if request.method != 'POST':
        row = request.GET.get('row', 5)

        content = {}
        content['row'] = row

        return render(request, 'index.html', content)

    else:
        row = request.POST.get('row', 5)
        try:
            row = int(row)
        except:
            row = 5
        if row > 100:
            row = 100
        msg = request.POST.get('msg', '')

        content = anti_censor(row, msg)
        content = {'content': content, 'row': row, 'msg':msg}

        return render(request, 'index.html', content)
