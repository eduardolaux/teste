from django.shortcuts import render

# Create your views here.
# Cria uma função (def) chamada post_list que leva a solicitação e irá 
# retornar o valor que recebe ao chamar outra função render que irá renderizar 
# (montar) nosso modelo blog/post_list.html.
def post_list(request):
    return render(request, 'blog/post_list.html', {})