# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )
@view_config(route_name='tasks_view', renderer='templates/tasks.mak')
def tasks_view(request):
    author_name = "Lukasz Sochanski"
    tasks = []
    main_task_elements = []
    main_task_elements.append('Widok z templatki.')
    main_task_elements.append('Przekazanie do templatki słownika.')
    main_task_elements.append('Słownik zawiera listę, której każdy element jest słownikiem')
    main_task_elements.append('Każdy element posiada klucz - literę i wartość klucza')
    main_task_elements.append('Każdy z kluczy to jedna z liter akronimu SOLID')
    main_task_elements.append('Wartość klucza to string, w którym opiszesz, jak rozumiesz pojęcie kryjące się pod daną literą')
    main_task_elements.append('Np: S - Single Reponsibility Priciple rozumiem jako...')
    main_task_elements.append('Wszystko oczywiście wyświetlone za pomocą templatki')


    task_for_all_team_members = {
        'contents': """Zadanie dla wszystkich polega na stworzeniu widoku\
            (view) tak, żeby po włączeniu serwera była dostępna strona \
            '0.0.0.0:port/twoje_imie/' a treść będzie generowana dzięki:""",
        'elements': main_task_elements,
        'summary': """Treść do widoku przekazałem za pomocą słownika, \
            żebyście mogli zobaczyć, jak działa pyramid i templatki mako.\
            Dokumentacja pyramid: http://docs.pylonsproject.org/projects/pyramid/en/latest/
            Dokumentacja mako: http://docs.makotemplates.org/en/latest/
            Dokumentacja python: https://docs.python.org/2/"""
    }
    tasks.append(task_for_all_team_members)
    return { 'tasks': tasks, 'letters': ['a','b','c'], 'default_filters':'decode.utf8'}

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'TeamProject'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_TeamProject_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

