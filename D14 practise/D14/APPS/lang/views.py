import pytz
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views import View
from .models import MyModel
from django.views.generic import ListView
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


class Index1(View):
    def get(self, request):
        string = _('Hello world')

        return HttpResponse(string)


class Index2(ListView):
    model = MyModel
    template_name = 'translate.html'
    context_object_name = 'name'


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('set_timezone')
    else:
        return render(request, 'time.html', {'current_time': timezone.now(), 'timezones': pytz.common_timezones})


class Index(View):
    def get(self, request):
        context = {
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
        }

        return HttpResponse(render(request, 'time2.html', context))

    #  по пост-запросу будем добавлять в сессию часовой пояс
    #  который и будет обрабатываться написанным нами ранее middleware
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('time')

# class Index(ListView):
#     model = MyModel
#     template_name = 'time2.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current_time'] = timezone.now()
#         context['timezones'] = pytz.common_timezones
#         return context
#
#     @staticmethod
#     def post(request):
#         request.session['django_timezone'] = request.POST['timezone']
#         return redirect('time')
