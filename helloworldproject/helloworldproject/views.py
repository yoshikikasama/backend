from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunc(request):
    return HttpResponse('<h1>hello world</h1>')

class HelloWorldClass(TemplateView):
    #ブラウザに表示させるhtmlを指定する
    template_name = 'hello.html'