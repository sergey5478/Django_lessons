from random import randint
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def text(title, result):
    return f'<h1>{title}<h1>' \
           f'<p>result for you: {result}<p>'


def coin(request):
    title = 'Go coin!'
    temp = randint(1, 2)
    if temp == 1:
        result = 'tails'
    else:
        result = 'eagle'
    logger.info(f'Result - {str(result)}')
    return HttpResponse(text(title, result))


def cube(request):
    title = 'Go cub!'
    result = randint(1, 6)
    logger.info(f'Result - {str(result)}')
    return HttpResponse(text(title, result))


def rand100(request):
    title = 'Result in 100!'
    result = randint(1, 100)
    logger.info(f'Result - {str(result)}')
    return HttpResponse(text(title, result))


def main_hw(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой сайт!</h1>
        <p>Это моя главная страница, где вы найдете разнообразные интересные материалы.</p>
    </body>
    </html>
    """
    logger.info(f'Result main_hw')
    return HttpResponse(html)


def about_me(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Привет! Меня зовут [Sergey] и я люблю изучать новые технологии.</p>
    </body>
    </html>
    """
    logger.info(f'Result about_me')
    return HttpResponse(html)
