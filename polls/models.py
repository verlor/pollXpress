from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
from django.core.validators import MinValueValidator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CodigoPostal(models.Model):
    codigo = models.CharField(max_length=10)
    municipio = models.CharField(max_length=50)

    def __str__(self):
        return (self.codigo+' - '+self.municipio)

class Article(models.Model):
    pub_date = models.DateTimeField()

    P1 = models.IntegerField(
        null=True,
        blank=True,

        choices=(
            (1, 'Femenino'),
            (2, 'Masculino'),
            (3, 'Otro'),
        ),

        verbose_name="¿Con qué género te identificas?:",
    )

    P2 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, '18-19'),
            (2, '20-21'),
            (3, '22-24'),
            (4, '25-27'),
            (5, '29-30'),
            (6, '31-35'),
            (7, '36-40'),
            (8, '41-45'),
            (9, '46-50'),
            (10, '51-60'),
            (11, '61 y más')
        ),
        verbose_name="¿En qué rango de edad (en años) te encuentras?:",
    )

    P3 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Estudiante de Licenciatura'),
            (2, 'Estudiante de Maestría'),
            (3, 'Estudiante de Doctorado o Postdoctorado'),
            (4, 'Profesor/a'),
            (5, 'Trabajador/a')
        ),
        verbose_name="Formas parte de la Comunidad Universitaria como:",
    )

    P3_1 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'CBI'),
            (2, 'CBS'),
            (3, 'CSH'),
        ),
        verbose_name="Si eres estudiante o profesor, ¿Cuál es tu división?:",
    )

    #preguntaa 4 pendiente
    P4 = models.ForeignKey(CodigoPostal, on_delete=models.CASCADE,
         verbose_name="El código postal del lugar donde vives es:  ",
         null=True,
         blank=True,
    )

    P5 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de personas. Si vives sola/o, ingresa 0 (cero).',
        verbose_name="La cantidad de personas con las que vives actualmente es: ",

    )

    P6 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de personas. Si no vivies con familiares ingresa 0 (cero).',
        verbose_name="De las personas que viven contigo: \n ¿Cuántas son tus familiares?",
    # Filtro: Si P5=0, esta no se debe ver
    )

    P6_1 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de personas',
        verbose_name="¿Cuántas no son tus familiares?",
    # Filtro: Si P5=0, esta no se debe ver
    )


# Se puede poner esto como un título de sección o algo por el estilo:
# 'Preguntas sobre Teléfonos Móviles'

    P7_1 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
            verbose_name="¿Tienes un télefono móvil?",
    )

    P7_2 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
        verbose_name="¿Tu teléfono móvil es un smartphone?",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_3 = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="¿Qué teléfono móvil usas actualmente?: \n Marca",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_3_o = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Modelo',
    # Filtro: Si P7_1=2 ocultar
    )

    P7_4 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Hablar'),
            (2, 'Comunicarte por internet (Redes sociales)'),
            (3, 'Entretenimiento (videos música, juegos, etc.)'),
            (4, 'Informarte (búsquedas, noticias, etc.)'),
            (5, 'Compras online'),
            (6, 'Operaciones bancarias (consultas, transferencias, etc.)'),
            (7, 'Trabajar'),
        ),
        help_text='Marca sólo la actividad que realizas con mayor frecuencia',
        verbose_name="Usas principalmente tu teléfono móvil para:",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_4_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otra, ¿cuál?',
    # Filtro: Si P7_1=2 ocultar
    )

    P7_5 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, '1 hora o menos'),
            (2, '2 a 3 horas'),
            (3, '4 a 5 horas'),
            (4, '6 a 10 horas'),
            (5, 'Más de 10 horas'),
        ),
        verbose_name="¿Cuánto tiempo usas tu teléfono móvil al día?",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_6 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de meses',
        verbose_name="¿Hace cuánto tiempo cambiaste de teléfono móvil por última vez?",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_7 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de veces',
        verbose_name="¿Cuántas veces cambiaste de teléfono móvil en los últimos 5 años?",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_8 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
        verbose_name="¿Piensas cambiar de teléfono móvil en los próximos 6 meses?",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_9 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Nuevo'),
            (2, 'Usado'),
        ),
        verbose_name="La próxima vez que vayas a cambiar de teléfono móvil, ¿Piensas comprar un equipo nuevo o uno usado?",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_10 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Lo tires'),
            (2, 'Lo regales'),
            (3, 'Lo vendas'),
            (4, 'Se quede en tu casa (sin usar)'),
            (5, 'Sigas usando el equipo viejo'),
        ),
        verbose_name="Al cambiar de teléfono móvil, lo habitual es que el equipo viejo:",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_10_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otra, ¿cuál?',
    # Filtro: Si P7_1=2 ocultar
    )

    P7_11 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Actualizar el equipo'),
            (2, 'Se rompió / descompuso el equipo'),
            (3, 'Robo del equipo'),
        ),
        verbose_name="El principal motivo por el que cambias de teléfono móvil es:",
    # Filtro: Si P7_1=2 ocultar
    )

    P7_11_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otro, ¿cuál?',
    # Filtro: Si P7_1=2 ocultar
    )

    P7_12 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa la cantidad de personas que tiene este tipo de equipo',
        verbose_name="¿Cuántas de las personas que viven contigo tienen teléfonos móviles?",
    # Filtro: Si P5=0 ocultar
    )


# Se puede poner esto como un título de sección o algo por el estilo:
# 'Preguntas sobre Tablets'

    P8_1 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
            verbose_name="¿Tienes o usas algún tipo de tablet (tablet / ipad / kindle / etc.)?",
    )

    P8_2 = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="¿Qué tablet usas actualmente?: \n Marca",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_2_o = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Modelo',
    # Filtro: Si P8_1=2 ocultar
    )


    P8_3 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Informarte (búsquedas, noticias, etc.)'),
            (2, 'Entretenimiento (videos música, juegos, etc.)'),
            (3, 'Estudiar'),
            (4, 'Leer libros'),
            (5, 'Trabajar'),
            (6, 'Comunicarte por internet (Redes sociales)'),
            (7, 'Compras online'),
            (8, 'Operaciones bancarias (consultas, transferencias, etc.)'),
        ),
        help_text='Marca sólo la actividad que realizas con mayor frecuencia',
        verbose_name="Usas principalmente tu tablet para:",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_3_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otra, ¿cuál?',
    # Filtro: Si P8_1=2 ocultar
    )

    P8_4 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, '1 hora o menos'),
            (2, '2 a 3 horas'),
            (3, '4 a 5 horas'),
            (4, '6 a 10 horas'),
            (5, 'Más de 10 horas'),
        ),
        verbose_name="¿Cuánto tiempo usas tu tablet al día?",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_5 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de meses. Si es tu primera tablet ingresa 0 (cero)',
        verbose_name="¿Hace cuánto tiempo cambiaste de tablet por última vez?",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_6 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de veces',
        verbose_name="¿Cuántas veces cambiaste de tablet en los últimos 5 años?",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_7 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
        verbose_name="¿Piensas cambiar de tablet en los próximos 6 meses?",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_8 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Nuevo'),
            (2, 'Usado'),
        ),
        verbose_name="La próxima vez que vayas a cambiar de tablet, ¿Piensas comprar un equipo nuevo o uno usado?",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_9 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Lo tires'),
            (2, 'Lo regales'),
            (3, 'Lo vendas'),
            (4, 'Se quede en tu casa (sin usar)'),
            (5, 'Sigas usando el equipo viejo'),
        ),
        verbose_name="Al cambiar de tablet, lo habitual es que el equipo viejo:",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_9_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otra, ¿cuál?',
    # Filtro: Si P8_1=2 ocultar
    )

    P8_10 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Actualizar el equipo'),
            (2, 'Se rompió / descompuso el equipo'),
            (3, 'Robo del equipo'),
        ),
        verbose_name="El principal motivo por el que cambias de tablet es:",
    # Filtro: Si P8_1=2 ocultar
    )

    P8_10_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otro, ¿cuál?',
    # Filtro: Si P8_1=2 ocultar
    )

    P8_11 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa la cantidad de personas que tiene este tipo de equipo',
        verbose_name="¿Cuántas de las personas que viven contigo tienen tablets?",
    # Filtro: Si P5=0 ocultar
    )

    P8_12 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de personas que usa tablets de manera individual',
        verbose_name="Las personas con las que vives que usan tablets (incluyéndote), lo hacen principalmente de manera: \n Individual",
    # Filtro: Si P5=0, esta no se debe ver
    )

    P8_12_1 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de personas que comparte tablets',
        verbose_name="Compartido",
    # Filtro: Si P5=0, esta no se debe ver
    )



# Se puede poner esto como un título de sección o algo por el estilo:
# 'Preguntas sobre Computadoras Portátiles (Notebooks, Netbooks, etc.)'

    P9_1 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
            verbose_name="¿Tienes una computadora portátil (notebook, netbook, etc)?",
    )

    P9_2 = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="¿Qué computadora portátil usas actualmente?: \n Marca",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_2_o = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Modelo',
    # Filtro: Si P9_1=2 ocultar
    )

    P9_3 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Informarte (búsquedas, noticias, etc.)'),
            (2, 'Comunicarte por internet (Redes sociales)'),
            (3, 'Estudiar'),
            (4, 'Entretenimiento (videos música, juegos, etc.)'),
            (5, 'Trabajar'),
            (6, 'Compras online'),
            (7, 'Operaciones bancarias (consultas, transferencias, etc.)'),
        ),
        help_text='Marca sólo la actividad que realizas con mayor frecuencia',
        verbose_name="Usas principalmente tu computadora portátil para:",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_3_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otra, ¿cuál?',
    # Filtro: Si P9_1=2 ocultar
    )

    P9_4 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, '1 hora o menos'),
            (2, '2 a 3 horas'),
            (3, '4 a 5 horas'),
            (4, '6 a 10 horas'),
            (5, 'Más de 10 horas'),
        ),
        verbose_name="¿Cuánto tiempo usas tu computadora portátil al día?",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_5 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de meses. Si es tu primera computadora portátil ingresa 0 (cero)',
        verbose_name="¿Hace cuánto tiempo cambiaste de computadora portátil por última vez?",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_6 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de veces',
        verbose_name="¿Cuántas veces cambiaste de computadora portátil en los últimos 5 años?",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_7 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
        verbose_name="¿Piensas cambiar de computadora portátil en los próximos 6 meses?",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_8 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Nuevo'),
            (2, 'Usado'),
        ),
        verbose_name="La próxima vez que vayas a cambiar computadora portátil, ¿Piensas comprar un equipo nuevo o uno usado?",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_9 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Lo tires'),
            (2, 'Lo regales'),
            (3, 'Lo vendas'),
            (4, 'Se quede en tu casa (sin usar)'),
            (5, 'Sigas usando el equipo viejo'),
        ),
        verbose_name="Al cambiar de computadora portátil, lo habitual es que el equipo viejo:",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_9_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otra, ¿cuál?',
    # Filtro: Si P9_1=2 ocultar
    )

    P9_10 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Actualizar el equipo'),
            (2, 'Se rompió / descompuso el equipo'),
            (3, 'Robo del equipo'),
        ),
        verbose_name="El principal motivo por el que cambias de computadora portátil es:",
    # Filtro: Si P9_1=2 ocultar
    )

    P9_10_o = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otro, ¿cuál?',
    # Filtro: Si P9_1=2 ocultar
    )

    P9_11 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa la cantidad de personas que tiene este tipo de equipo',
        verbose_name="¿Cuántas de las personas que viven contigo tienen computadoras portátiles?",
    # Filtro: Si P5=0 ocultar
    )

# Se puede poner esto como un título de sección o algo por el estilo:
# 'Preguntas Finales'

    P10 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
        verbose_name="¿En el lugar donde vives tienen computadoras de escritorio (fijas)?",
    )

    P11 = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ingresa el número de computadoras de escritorio',
        verbose_name="¿Cuántas computadoras de escritorio (fijas) tienen en el lugar en que vives?",
    # Filtro: Si P10=2 ocultar
    )

    P12 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
        ),
        verbose_name="¿En el lugar donde vives tienes conexión a internet?",
    )

    P13 = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (2, 'No'),
            (3, 'No sé'),
        ),
        verbose_name="Además de los dispositivos ya señalados, ¿Usas algún otro aparato que tenga baterías de Ion-Litio?",
    )

    P14_o_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Si tu respuesta a la pregunta anterior fue sí, ¿Qué otro(s) aparato(s) usas?:  \n Aparato 1',
   # Filtro: Si P13=2 o P13=3 ocultar /O si sale más fácil, Si P13=1 mostrar
    )

    P14_o_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Aparato 2',
   # Filtro: Si P13=2 o P13=3 ocultar /O si sale más fácil, Si P13=1 mostrar
    )

    P14_o_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Aparato 3',
   # Filtro: Si P13=2 o P13=3 ocultar /O si sale más fácil, Si P13=1 mostrar
    )


# Agregar texto de despedida y agradecimiento
# 'Agradecemos tu cooperación en esta investigación'


    def __str__(self):
        return str(self.pub_date)

    class Meta:
        ordering = ('pub_date',)

class ArticleForm(ModelForm):
    #birth_country = forms.ModelChoiceField(
    #    queryset=Country.objects.all(),
    #    widget=autocomplete.ModelSelect2(url='country-autocomplete')
    #)

    class Meta:
        model = Article
        exclude = ('pub_date',)
