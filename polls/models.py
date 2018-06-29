from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
from django.core.validators import MinValueValidator
# Create your models here.

class Article(models.Model):
    pub_date = models.DateTimeField()

    genero = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Femenino'),
            (2, 'Masculino'),
            (3, 'Otro'),
        ),
        verbose_name="1. Género con el que te identificas:",
    )

    rango_edad = models.IntegerField(
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
        verbose_name="2. ¿En qué rango de edad (en años) te encuentras?:",
    )

    comunidad = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Estudiante de Licenciatura'),
            (2, 'Estudiante de Maestría'),
            (3, 'Estudiante de Doctorado o Postdoctorado'),
            (4, 'Profesor/a'),
            (5, 'Trabajador/a')
        ),
        verbose_name="3. Formas parte de la Comunidad Universitaria como:",
    )

    division = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'CBI'),
            (2, 'CBS'),
            (3, 'CSH'),
        ),
        verbose_name="3.1 Si eres estudiante o profesor, ¿Cuál es tu división? :",
    )
    #preguntaa 4 pendiente

    personas_viviendo = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="5. La cantidad de personas con las que vives actualmente es: ",
    )

    familiares = models.IntegerField(
        null=True,
        blank=True,
        help_text='Ingresar número',
        verbose_name="6. La relación de parentesco que tienes con las personas con quienes vives es: \n Familiares   ",
    )

    no_familiares = models.IntegerField(
        null=True,
        blank=True,
        help_text='Ingresar número',
        verbose_name="No Familiares   ",
        validators=[MinValueValidator(0)],
    )

    tiene_movil = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (0, 'No'),
        ),
        help_text='Si la respuesta es No pasar a 7.10 ',
        verbose_name="7. Preguntas sobre Teléfono Móvil: \n \n 7.1 ¿Tienes un télefono móvil? ",
    )

    tiene_movil_intel = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (0, 'No'),
        ),
        verbose_name="7.2 ¿Tu teléfono móvil es un Smartphone? ",
    )

    uso_movil = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Hablar'),
            (2, 'Comunicarte por internet (Redes sociales)'),
            (3, 'Entretenimiento (videos música, juegos, etc.)'),
            (4, 'Fuente de Información (búsquedas, noticias, etc.)'),
            (5, 'Trabajar'),
        ),
        help_text='Marca sólo la actividad que realizas con mayor frecuencia)',
        verbose_name="7.3 Usas principalmente tu teléfono para:",
    )

    uso_movil_otro = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otro, ¿cuál?',
    )

    hrs_uso_movil = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, '1 hora o menos'),
            (2, '2 a 3 horas'),
            (3, '4 a 5 horas'),
            (4, '6 a 10 horas'),
            (5, 'Más de 10 horas'),
        ),
        verbose_name="7.4  ¿Cuánto tiempo usas el teléfono móvil por día?",
    )

    ult_cambio_movil = models.IntegerField(
        null=True,
        blank=True,
        help_text='(número de meses)',
        verbose_name="7.5 ¿Hace cuánto tiempo cambiaste de teléfono móvil por última vez?  ",
    )

    freq_cambio_movil = models.IntegerField(
        null=True,
        blank=True,
        help_text='(ingresar número)',
        verbose_name="7.6 ¿Cuántas veces cambiaste de teléfono móvil en los últimos 5 años?",
    )

    cambio_movil = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Sí'),
            (0, 'No'),
        ),
        verbose_name="7.7 ¿Piensas cambiar de teléfono móvil en los próximos 6 meses?",
    )

    uso_viejo_movil = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Lo tires'),
            (2, 'Lo regales'),
            (3, 'Lo vendas'),
            (4, 'Sigas usando el equipo viejo'),
            (5, 'Trabajar'),
        ),
        verbose_name="7.8 Al cambiar de teléfono móvil, lo habitual es que el equipo viejo:",
    )

    otro_uso_viejo_movil = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otro, ¿cuál?',
    )

    motivo_cambio_movil = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            (1, 'Actualizar el equipo'),
            (2, 'Se descompuso el equipo'),
            (3, 'Robo del equipo'),
            (4, 'Sigas usando el equipo viejo'),
            (5, 'Trabajar'),
        ),
        verbose_name="7.9 El principal motivo por el que cambias de teléfono móvil es:",
    )

    otro_motivo_cambio_movil = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Otro, ¿cuál?',
    )

    personas_con_movil = models.IntegerField(
        null=True,
        blank=True,
        help_text='(ingresar cantidad)',
        verbose_name="7.10 ¿Cuántas de las personas que viven contigo tienen teléfonos móviles?",
    )


    def __str__(self):
        return str(self.pub_date)

    class Meta:
        ordering = ('pub_date',)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ('pub_date',)
