from django.shortcuts import render


def inicio(request):
    dados = []
    dados.append(
        {
            'titulo': 'Curso Python Basic',
            'categoria': 'Educação',
            'data': '30/08/2023',
            'descricao': 'Curso de Python já supera as expectativas para o primeiro semestre.'
        }
    )
    dados.append(
        {
            'titulo': 'Curso JavaScript Basic',
            'categoria': 'Educação',
            'data': '30/08/2023',
            'descricao': 'Curso Java script para iniciantes vem sendo muito procurado.'
        }
    )
    dados.append(
        {
            'titulo': 'Buteco do Gustavo Lima',
            'categoria': 'Show',
            'data': '15/08/2023',
            'descricao': 'Definida a data para o Show do Buteco do Gustavo Lima no interior de SC.'
        }
    )

    contexto = {
        'dados': dados
    }

    resposta = render(request, 'inicio.html', contexto)
    return resposta


def contato(request):
    contexto = {
        'telefone': '555-5525',
        'responsavel': 'John Doe'
    }
    resposta = render(request, 'contato.html', contexto)
    return resposta
