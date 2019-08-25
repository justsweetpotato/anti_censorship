from django.shortcuts import render
from .data import print_in_line, print_in_line_reverse


def index(request):
    if request.method != 'POST':
        row = request.GET.get('row', 5)

        content = {}
        content['row'] = row
        content['style'] = ' '
        content['reverse'] = '0'

        return render(request, 'index.html', content)

    else:
        row = request.POST.get('row', 5)
        try:
            row = int(row)
        except:
            row = 5
        if row > 10:
            row = 10
        msg = request.POST.get('msg', '')
        style = request.POST.get('style', ' ')
        reverse = request.POST.get('reverse', '0')

        if reverse == '0':
            content = print_in_line(row, msg, style)
        else:
            content = print_in_line_reverse(row, msg, style)

        content = {
            'content': content,
            'row': row,
            'msg': msg,
            'style': style,
            'reverse': reverse
        }
        return render(request, 'index.html', content)
