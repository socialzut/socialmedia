from pyramid.config import Configurator
from sqlalchemy import engine_from_config

try:
    # for python 2
    from urlparse import urlparse
except ImportError:
    # for python 3
    from urllib.parse import urlparse

from gridfs import GridFS
import pymongo

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.Connection(
       host=db_url.hostname,
       port=db_url.port,
    )
    def add_db(request):
       db = config.registry.db[db_url.path[1:]]
       if db_url.username and db_url.password:
           db.authenticate(db_url.username, db_url.password)
       return db

    def add_fs(request):
       return GridFS(request.db)

    config.add_request_method(add_db, 'db', reify=True)
    config.add_request_method(add_fs, 'fs', reify=True)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('tasks_view', 'tasks')
    config.add_route('tasks_view2', 'lol')
    config.add_route('tasks_view3', 'test')
    config.scan()
    return config.make_wsgi_app()
