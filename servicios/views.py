from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from servicios.serializers import *
from servicios.models import *
import random


class AsignaturaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        # Excluye el curso que estan en la tienda
        items = Asignatura.objects.exclude(id_asignatura__in=[19, 8])
        serializer = AsignaturaSerializer(items, many=True)
        return Response(serializer.data, status=201)


class SubtemaTemaAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            # Subtemas de un tema
            item = Subtema.objects.filter(id_tema__pk=id)
            serializer = SubtemaTemaSerializer(item, many=True)
            return Response(serializer.data)
        except Tema.DoesNotExist:
            return Response(status=404)


class TemaAsignaturaAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            # Temas de un asignatura
            item = Tema.objects.filter(id_asignatura__pk=id)
            serializer = TemaAsignaturaSerializer(item, many=True)
            return Response(serializer.data)
        except Tema.DoesNotExist:
            return Response(status=404)


class TemaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        # Todos los temas
        items = Tema.objects.all()
        serializer = TemaSerializer(items, many=True)
        return Response(serializer.data, status=201)


class SubtemaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        # Todos los subtemas
        items = Subtema.objects.all()
        serializer = SubtemaSerializer(items, many=True)
        return Response(serializer.data, status=201)


class PreguntaAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Pregunta.objects.get(pk=id)
            serializer = PreguntaSerializer(item)
            return Response(serializer.data)
        except Pregunta.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Pregunta.objects.get(pk=id)
        except Pregunta.DoesNotExist:
            return Response(status=404)
        serializer = PreguntaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Pregunta.objects.get(pk=id)
        except Pregunta.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PreguntaTAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        # Pregutas de un subtema
        items = Pregunta.objects.filter(id_subtema__id_subtema=id)
        serializer = PreguntaTSerializer(items, many=True)
        return Response(serializer.data, status=201)

    def post(self, request, format=None):
        serializer = PreguntaTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PreguntaRAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    # Preguntas Random

    def get(self, request, id, completado, format=None):
        items = Pregunta.objects.filter(id_subtema=id)
        lists = []
        response = []
        if completado == 0:
            cantidad = 7
        elif completado == 1:
            cantidad = 10
        else:
            return Response(response)
        i = 1
        while i <= cantidad:
            # Random de las preguntas del subtema
            rand = random.choice(items).id_pregunta
            if not lists or (rand not in lists):
                lists.append(rand)
                response.append(self.get_answer(rand))
                i = i + 1

        return Response(response, status=201)

    def get_answer(self, rand):
        pregunta = Pregunta.objects.get(pk=rand)
        serializer = PreguntaTSerializer(pregunta, many=False)
        return serializer.data


class PreguntaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Pregunta.objects.all()
        serializer = PreguntaSerializer(items, many=True)
        return Response(serializer.data, status=201)

    def post(self, request, format=None):
        serializer = PreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RespuestaAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Respuesta.objects.get(pk=id)
            serializer = RespuestaSerializer(item)
            return Response(serializer.data)
        except Respuesta.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Respuesta.objects.get(pk=id)
        except Respuesta.DoesNotExist:
            return Response(status=404)
        serializer = RespuestaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Respuesta.objects.get(pk=id)
        except Respuesta.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RespuestaPreguntaListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        items = Respuesta.objects.filter(id_pregunta__id_subtema=request.data['id_subtema'],
                                         id_usuario=request.data['id_usuario'])
        serializer = RespuestaPreguntaSerializer(items, many=True)
        return Response(serializer.data, status=201)


class RespuestaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Respuesta.objects.all()
        serializer = RespuestaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        for requests in request.data:
            try:
                Respuesta.objects.get(
                    id_usuario=requests['id_usuario'], id_pregunta=requests['id_pregunta'])
                respuesta = Respuesta.objects.get(id_usuario__pk=requests['id_usuario'],
                                                  id_pregunta__pk=requests['id_pregunta'])
                respuesta.acertada = requests['acertada']
                # Actualizacion de pregunta bien contestada
                respuesta.save(update_fields=['acertada'])
            # Si la respuesta no existe, se inserta
            except Respuesta.DoesNotExist:
                usuario = Usuario.objects.get(
                    id_usuario=requests['id_usuario'])
                pregunta = Pregunta.objects.get(
                    id_pregunta=requests['id_pregunta'])
                respuesta = Respuesta(id_usuario=usuario, id_pregunta=pregunta,
                                      acertada=requests['acertada'])
                # Insercion forzosa
                respuesta.save(force_insert=True)
        return Response(status=201)


class UsuarioAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def put(self, request, id, format=None):
        try:
            item = Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            return Response(status=404)
        serializer = UsuarioSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UsuarioAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        if request.data['usuario'] != "" and request.data['password'] != "":
            serializer = UsuarioRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                items = Asignatura.objects.exclude(id_asignatura__in=[19, 8])
                id_usuario = Usuario.objects.get(
                    usuario=request.data['usuario'])
                asignaturas = []
                for item in items:
                    asignaturas.append(UsuarioAsignatura(
                        id_usuario=id_usuario, id_asignatura=item, porcentaje=0.0))
                UsuarioAsignatura.objects.bulk_create(asignaturas)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response(status=400)


class UsuarioAuthAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    # Verificacion del login

    def post(self, request, format=None):
        try:
            items = Usuario.objects.get(
                usuario=request.data['usuario'], password=request.data['password'])
            serializer = UsuarioSerializer(items)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({"auth": False})

        return Response(status=400)


class UsuarioAsignaturaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        items = UsuarioAsignatura.objects.filter(
            id_usuario=request.data['id_usuario'])
        serializer = UsuarioAsignaturaSerializer(items, many=True)
        return Response(serializer.data, status=201)


class UsuarioTemaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        items = UsuarioTema.objects.filter(
            id_usuario=request.data['id_usuario'], id_tema__id_asignatura=request.data['id_asignatura'])
        serializer = UsuarioTemaSerializer(items, many=True)
        return Response(serializer.data, status=201)


class UsuarioMonedasAPI(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        usuario = Usuario.objects.get(id_usuario=request.data['id_usuario'])
        usuario.monedas = request.data['monedas']
        usuario.save(update_fields=['monedas'])
        return Response(status=201)


class UsuarioArticuloAPI(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        id_usuario = Usuario.objects.get(id_usuario=request.data['id_usuario'])
        id_articulo = Articulo.objects.get(
            id_articulo=request.data['id_articulo'])
        id_asignatura = Asignatura.objects.get(
            id_asignatura=request.data['id_articulo'])
        usuario_articulo = UsuarioArticulo(id_usuario=id_usuario,
                                           id_articulo=id_articulo)
        usuario_articulo.save(force_insert=True)
        usuario_asignatura = UsuarioAsignatura(
            id_usuario=id_usuario, id_asignatura=id_asignatura, porcentaje=0.0)
        usuario_asignatura.save(force_insert=True)
        usuario = Usuario.objects.get(id_usuario=request.data['id_usuario'])
        usuario.monedas = request.data['monedas']
        usuario.save(update_fields=['monedas'])
        return Response(status=201)


class UsuarioArticuloListAPI(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        items = UsuarioArticulo.objects.filter(
            id_usuario_id=request.data['id_usuario'])
        serializer = UsuarioArticuloSerializer(items, many=True)
        return Response(serializer.data, status=201)


class ArticuloAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        usuario_articulo = UsuarioArticulo.objects.filter(
            id_usuario=request.data['id_usuario'])
        articulos_comprados = [
            articulo.id_articulo.id_articulo for articulo in usuario_articulo]
        items = Articulo.objects.exclude(id_articulo__in=articulos_comprados)
        if items:
            serializer = ArticuloSerializer(items, many=True)
            return Response(serializer.data, status=201)
        else:
            return Response([], status=201)


class UsuarioSubtemaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        items = UsuarioSubtema.objects.filter(
            id_usuario=request.data['id_usuario'], id_subtema__id_tema=request.data['id_tema'])
        serializer = UsuarioSubtemaSerializer(items, many=True)
        return Response(serializer.data, status=201)


class UsuarioSubtemaCascadaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        serializer = UsuarioSubtemaCascadaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                subtema = Subtema.objects.get(pk=request.data['id_subtema'])
                u_tema = UsuarioTema.objects.get(
                    id_tema=subtema.id_tema.id_tema, id_usuario=request.data['id_usuario'])
                subtemas = Subtema.objects.filter(
                    id_tema=subtema.id_tema.id_tema)
                id_subtemas = [
                    id_subtema.id_subtema for id_subtema in subtemas]
                u_subtema = UsuarioSubtema.objects.filter(
                    id_subtema__in=id_subtemas, id_usuario=request.data['id_usuario'], completado=1)
                # Porcentaje de subtema completo
                porcentaje = (u_subtema.count() / subtemas.count()) * 100
                u_tema.porcentaje = porcentaje
                # Actualizacion del porcentaje
                u_tema.save(update_fields=['porcentaje'])
                # Si llega a 100% un subtema
                if porcentaje == 100.00:
                    tema = Tema.objects.get(pk=u_tema.id_tema.id_tema)
                    temas = Tema.objects.filter(
                        id_asignatura=tema.id_asignatura.id_asignatura)
                    id_temas = [id_tema.id_tema for id_tema in temas]
                    u_tema = UsuarioTema.objects.filter(
                        id_tema__in=id_temas, id_usuario=request.data['id_usuario'], porcentaje=100.00)
                    # Porcentaje de tema completo
                    porcentaje = (u_tema.count() / temas.count()) * 100
                    u_asignatura = UsuarioAsignatura.objects.get(id_asignatura=tema.id_asignatura.id_asignatura,
                                                                 id_usuario=request.data['id_usuario'])
                    u_asignatura.porcentaje = porcentaje
                    # Actualizacion del porcentaje
                    u_asignatura.save(update_fields=['porcentaje'])
                return Response(serializer.data, status=201)
            # Primera vez que desarrolla un subtema
            except UsuarioTema.DoesNotExist:
                # Un subtema completo
                porcentaje = (1 / subtemas.count()) * 100
                u_tema = UsuarioTema(
                    id_usuario_id=request.data['id_usuario'], id_temas_id=subtema.id_tema.id_tema, porcentaje=porcentaje)
                # Inserta un usuario-tema
                u_tema.save()
                tema = Tema.objects.get(pk=u_tema.id_tema.id_tema)
                try:
                    UsuarioAsignatura.objects.get(
                        id_asignatura=tema.id_asignatura.id_asignatura, id_usuario_id=request.data['id_usuario'])
                # Si usuario asignatura no existe
                except Asignatura.DoesNotExist:
                    # Un tema completo
                    porcentaje = (1 / temas.count()) * 100
                    u_asignatura = UsuarioAsignatura(id_usuario_id=request.data['id_usuario'],
                                                     id_asignatura_id=tema.id_asignatura.id_asignatura,
                                                     porcentaje=porcentaje)
                    # Inserta usuario-asignatura
                    u_asignatura.save()
                    return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
