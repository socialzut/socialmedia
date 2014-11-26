# -*- coding: utf-8 -*-
from PyPDF2.pdf import PdfFileReader
from StringIO import StringIO


import os
import shutil
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from .models import (
    DBSession,
    MyModel,
    )

def getDataUsingPyPdf2(file):
    pdf = PdfFileReader(file)
    content = ""

    for i in range(0, pdf.getNumPages()):
        print str(i)
        extractedText = pdf.getPage(i).extractText()
        content +=  extractedText + "\n"

    content = " ".join(content.replace("\xa0", " ").strip().split())
    return content.encode("ascii", "ignore")

@view_config(route_name='zadanie_view', renderer='templates/zadanie.mak')
def zadanie_view(request):


        
    zadanie = []
    zadanie_elements = []
    submit = request.POST.get('submit', '0') 
    if submit == 'submit':
        filename = request.POST['pdf'].filename

        input_file = request.POST['pdf'].file
        zadanie_elements.append("Zaladowales plik")
        zadanie_elements.append(filename)
        content = getDataUsingPyPdf2(input_file)
        zadanie_elements.append(content)


            

    else:
        zadanie_elements.append("Nie zaladowano piku")
    
    zadanie_members = {
          'contents': """""",
          'elements': zadanie_elements,
          'summary': """"""
    }

    zadanie.append(zadanie_members)
    return { 'zadanie': zadanie }

@view_config(route_name='tasks_view', renderer='templates/tasks.mak')
def tasks_view(request):
    
    author_name = "Lukasz Sochanski"
    tasks = []
    main_task_elements = []
    main_task_elements.append('Stworzenie widoku(view) gdzie będzie formularz umożliwiający\
        podanie pliku pdf z listą studentów.')
    main_task_elements.append('Wykorzystanie jednego z dostępnych w internecie input_filełów\
     pythonowych, który umożliwia wydobycie tekstu z pdfa.')
    main_task_elements.append("Stworzenie modułu, którego jedna z metod będzie miała\
        na wyjściu listę studentów - listę, czyli pythonową strukturę danych - '[]'")
    main_task_elements.append('Stworzenie modułu, który filtruje tą listę i na wyjściu ma listę kobiet.')
    main_task_elements.append('Stworznie modułu, a raczej fragmentu kodu,\
     który będzie przyjmował listę i zapisywał ją do bazy danych.')
    main_task_elements.append('Stworznie widoku, który wyświetli tą listę w formie tabeli')


    task_for_all_team_members = {
        'contents': """Zadanie dla wszystkich polega na stworzeniu parsera\
        o znanej nam tematyce. Całość zadania to:""",
        'elements': main_task_elements,
        'summary': """Wykorzytajcie do zadania wiedzę z zadania 2. Treść do widoku przekazałem za pomocą słownika, \
            żebyście mogli zobaczyć, jak działa pyramid i templatki mako.\
            Zapoznajcie się z formatem json.
            Dokumentacja pyramid: http://docs.pylonsproject.org/projects/pyramid/en/latest/
            Dokumentacja mako: http://docs.makotemplates.org/en/latest/
            Dokumentacja python: https://docs.python.org/2/"""
    }
    tasks.append(task_for_all_team_members)
    knowledge_task = {
        'contents': """ By poznać zasady i dobre praktyki programowania, \
            zapoznajcie się z materiałami: """,
        'elements': [
            "http://legacy.python.org/dev/peps/pep-0008/ - zasady pisania kodu w pythonie",
            "https://speakerdeck.com/guasek/test-driven-development-the-right-way  - TDD autorstwa kolegi z red-sky",
            "https://docs.python.org/2/library/unittest.html#organizing-test-code   - z dokumentacji unittesty",
            "!!! https://www.youtube.com/watch?v=WpkDN78P884&index=5&list=PLLbmAYY8SeFXCQ0Lrc6lzfNu_Ix6Q_H5b - architektura warstwowa",
            "http://williamdurand.fr/2013/07/30/from-stupid-to-solid-code/",
            "!!! http://blog.8thlight.com/uncle-bob/2012/08/13/the-clean-architecture.html",
            "PL !!! https://www.youtube.com/watch?v=znRByMgnFSM- testy",

        ],
        'summary': "Zwróćcie uwagi na wykrzykniki, przejrzyjcie arch. \
            warstwową nawet kilka razy. Na początek to powinno wystarczyć."

    }
    tasks.append(knowledge_task)
    return { 'tasks': tasks }

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

