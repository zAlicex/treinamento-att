from django.urls import path
from django import views
from .views import (
    IndexView,
    EquipamentoView,
    EquipamentoSelecaoView,  # Verifique se está aqui
    PlataformaView,
    InsercaoView,
    VideoIsca2GView,
    VideoIsca4GView,
    VideoQueclinkView,
    VideoIsca419View,
    VideoInsercaoView,
    VideoPlataformaView,
    LoginView,
    PilaresView,
    VideoPilaresView,
    mark_pilar_watched,
    ChatbotView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('equipamento/', EquipamentoView.as_view(), name='equipamento'),
    path('equipamentoselecao/', EquipamentoSelecaoView.as_view(), name='equipamento-selecao'),  # Aqui
    path('plataforma/', PlataformaView.as_view(), name='plataforma'),
    path('insercao/', InsercaoView.as_view(), name='insercao'),
    path('videoisca2g/', VideoIsca2GView.as_view(), name='isca2g'),
    path('videoisca4g/', VideoIsca4GView.as_view(), name='isca4g'),
    path('videoqueclink/', VideoQueclinkView.as_view(), name='gl33'),
    path('pilares/', PilaresView.as_view(), name='pilares'),
    path('mark_pilar_watched/', mark_pilar_watched, name='mark_pilar_watched'),
    path('video-pilares/', VideoPilaresView.as_view(), name='pilares'),
    path('chatbot', ChatbotView.as_view(), name='chat_view'),
    path('videoisca419/', VideoIsca419View.as_view(), name='isca419'),
    path('VideoInsercao/', VideoInsercaoView.as_view(), name='insercao'),
    path('VideoPlataforma/', VideoPlataformaView.as_view(), name='plataforma'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
