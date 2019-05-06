from django.urls import path
from servicios import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('asignatura/', views.AsignaturaAPIListView.as_view()),

    path('tema/', views.TemaAPIListView.as_view()),

    path('tema-asignatura/<int:id>', views.TemaAsignaturaAPIView.as_view()),

    path('subtema-tema/<int:id>', views.SubtemaTemaAPIView.as_view()),

    path('subtema/', views.SubtemaAPIListView.as_view()),

    path('pregunta/<int:id>', views.PreguntaAPIView.as_view()),
    path('pregunta/', views.PreguntaAPIListView.as_view()),

    path('preguntaT/', views.PreguntaTAPIListView.as_view()),
    path('preguntaT/<int:id>', views.PreguntaTAPIListView.as_view()),

    path('preguntaR/<int:id>/<int:completado>',
         views.PreguntaRAPIListView.as_view()),

    path('respuesta/<int:id>', views.RespuestaAPIView.as_view()),
    path('respuesta/', views.RespuestaAPIListView.as_view()),

    path('usuario/<int:id>', views.UsuarioAPIView.as_view()),
    path('usuario/', views.UsuarioAPIListView.as_view()),

    path('usuarioAuth/', views.UsuarioAuthAPIListView.as_view()),

    path('usuarioAsignatura/', views.UsuarioAsignaturaAPIListView.as_view()),

    path('usuarioTema/', views.UsuarioTemaAPIListView.as_view()),

    path('completado/', views.UsuarioSubtemaCascadaAPIListView.as_view()),

    path('usuarioSubtema/', views.UsuarioSubtemaAPIListView.as_view()),

    path('articulo/', views.ArticuloAPIListView.as_view()),

    path('usuarioArticulo/', views.UsuarioArticuloAPI.as_view()),

    path('usuarioMonedas/', views.UsuarioMonedasAPI.as_view()),

    path('respuestaPregunta/', views.RespuestaPreguntaListView.as_view()),

    path('usuarioArticulos/', views.UsuarioArticuloListAPI.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
