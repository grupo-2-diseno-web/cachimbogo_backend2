from rest_framework.serializers import ModelSerializer, SerializerMethodField
from servicios.models import *


class AsignaturaSerializer(ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'


class DificultadSerializer(ModelSerializer):
    class Meta:
        model = Dificultad
        fields = '__all__'


class TemaAsignaturaSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'


class SubtemaTemaSerializer(ModelSerializer):
    class Meta:
        model = Subtema
        fields = '__all__'


class TemaOSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'


class TemaSerializer(ModelSerializer):
    asignatura = SerializerMethodField()

    def get_asignatura(self, tema):
        asignatura = AsignaturaSerializer(
            tema.id_asignatura, many=False, read_only=True)
        return asignatura.data

    class Meta:
        model = Tema
        fields = '__all__'


class SubtemaSerializer(ModelSerializer):
    tema = SerializerMethodField()

    def get_tema(self, subtema):
        tema = TemaSerializer(subtema.id_tema, many=False, read_only=True)
        return tema.data

    class Meta:
        model = Subtema
        fields = '__all__'


class TipoPreguntaSerializer(ModelSerializer):
    class Meta:
        model = TipoPregunta
        fields = '__all__'


class PreguntaTSerializer(ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'


class PreguntaSerializer(ModelSerializer):
    dificultad = SerializerMethodField()
    subtema = SerializerMethodField()
    tipo_pregunta = SerializerMethodField()

    def get_tipo_pregunta(self, pregunta):
        tipo_pregunta = TipoPreguntaSerializer(
            pregunta.id_tipopregunta, many=False, read_only=True)
        return tipo_pregunta.data

    def get_subtema(self, pregunta):
        subtema = SubtemaSerializer(
            pregunta.id_subtema, many=False, read_only=True)
        return subtema.data

    def get_dificultad(self, pregunta):
        dificultad = DificultadSerializer(
            pregunta.id_dificultad, many=False, read_only=True)
        return dificultad.data

    class Meta:
        model = Pregunta
        fields = '__all__'


class RespuestaSerializer(ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'


class RespuestaPreguntaSerializer(ModelSerializer):
    pregunta = SerializerMethodField()

    def get_pregunta(self, respuesta):
        pregunta = PreguntaSerializer(
            respuesta.id_pregunta, many=False, read_only=True)
        return pregunta.data

    class Meta:
        model = Respuesta
        fields = '__all__'


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario', 'usuario', 'nombres',
                  'apellidos', 'correo', 'monedas')


class UsuarioRegisterSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('usuario', 'password', 'nombres',
                  'apellidos', 'correo', 'monedas')


class UsuarioAsignaturaSerializer(ModelSerializer):
    asignatura = SerializerMethodField()

    def get_asignatura(self, usuario_asignatura):
        asignatura = AsignaturaSerializer(
            usuario_asignatura.id_asignatura, many=False, read_only=True)
        return asignatura.data

    class Meta:
        model = UsuarioAsignatura
        fields = '__all__'


class UsuarioTemaSerializer(ModelSerializer):
    tema = SerializerMethodField()

    def get_tema(self, usuario_tema):
        tema = TemaOSerializer(usuario_tema.id_tema,
                               many=False, read_only=True)
        return tema.data

    class Meta:
        model = UsuarioTema
        fields = '__all__'


class UsuarioSubtemaSerializer(ModelSerializer):
    subtema = SerializerMethodField()

    def get_subtema(self, usuario_subtema):
        subtema = SubtemaTemaSerializer(
            usuario_subtema.id_subtema, many=False, read_only=True)
        return subtema.data

    class Meta:
        model = UsuarioSubtema
        fields = '__all__'


class UsuarioSubtemaCascadaSerializer(ModelSerializer):
    class Meta:
        model = UsuarioSubtema
        fields = '__all__'


class UsuarioArticuloSerializer(ModelSerializer):
    class Meta:
        model = UsuarioArticulo
        fields = '__all__'


class ArticuloSerializer(ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
