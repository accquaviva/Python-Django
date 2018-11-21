from django.conf.urls import url
from .views import home, lista_pessoas, lista_veiculos, lista_movrotativos, lista_mensalistas, lista_movmensalitas, \
    pessoa_novo, veiculos_novo, movrotativos_novo, mensalistas_novo, movmensalitas_novo, pessoas_update, \
    veiculos_update, movrotativos_update, mensalistas_update, movmensalitas_update, pessoas_delete, veiculos_delete, \
    movrotativos_delete, mensalistas_delete,movmensalitas_delete

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoas_novo/$', pessoa_novo, name='core_pessoas_novo'),
    url(r'^pessoas_update/(?P<id>\d+)/$', pessoas_update, name='core_pessoas_update'),
    url(r'^pessoas_delete/(?P<id>\d+)/$', pessoas_delete, name='core_pessoas_delete'),

    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^veiculos_novo/$', veiculos_novo, name='core_veiculos_novo'),
    url(r'^veiculos_update/(?P<id>\d+)/$', veiculos_update, name='core_veiculos_update'),
    url(r'^veiculos_delete/(?P<id>\d+)/$', veiculos_delete, name='core_veiculos_delete'),

    url(r'^movrotativos/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^movrotativos_novo/$', movrotativos_novo, name='core_movrotativos_novo'),
    url(r'^movrotativos_update/(?P<id>\d+)/$', movrotativos_update, name='core_movrotativos_update'),
    url(r'^movrotativos_delete/(?P<id>\d+)/$', movrotativos_delete, name='core_movrotativos_delete'),

    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    url(r'^mensalistas_novo/$', mensalistas_novo, name='core_mensalistas_novo'),
    url(r'^mensalistas_update/(?P<id>\d+)$', mensalistas_update, name='core_mensalistas_update'),
    url(r'^mensalistas_delete/(?P<id>\d+)$', mensalistas_delete, name='core_mensalistas_delete'),

    url(r'^movmensalitas/$', lista_movmensalitas, name='core_lista_movmensalitas'),
    url(r'^movmensalitas_novo/$', movmensalitas_novo, name='core_movmensalitas_novo'),
    url(r'^movmensalitas_update/(?P<id>\d+)/$', movmensalitas_update, name='core_movmensalitas_update'),
    url(r'^movmensalitas_delete/(?P<id>\d+)/$', movmensalitas_delete, name='core_movmensalitas_delete'),

]
