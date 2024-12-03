# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:44:12 2024

@author: El Ayatola
"""

from manim import *

# Configuración personalizada de la escena para mayor calidad
config.pixel_height = 540  # Altura en píxeles (1080 para Full HD)
config.pixel_width = 960   # Ancho en píxeles (1920 para Full HD)
config.frame_rate = 20     # Tasa de cuadros por segundo 


class ImportImages(Scene):  # Definimos la 
    def scene1_content(self):
        
        self.camera.background_color =WHITE
        #Cargar Imagen
        image = ImageMobject('C:/Users/El Ayatola/Documents/1.PNG')
        
        # Opcional: Ajusta el tamaño y la posición de la imagen
        image.scale(0.5)  # Escala la imagen para hacerla más grande o más pequeña
        image.to_edge(UP)  # Mueve la imagen a la parte superior de la pantalla

        # Agrega la imagen a la escena
        self.add(image)

        # Agrega un texto opcional debajo de la imagen
        text = Text("Esta es una imagen importada con MANIM")
        text.next_to(image, DOWN)

        # Muestra la imagen y el texto
        self.play(FadeIn(image), Write(text))
        self.wait(2)




class ExponentialCurve(Scene):  # Definimos la segunda animación como clase, dentro va "Scene" 
    def scene2_content(self):        # Definimos el constructor incluyendo "self" 
        
        # Configuración de la escena
        self.camera.background_color = WHITE  # Definimos el color de fondo de la escena       
        axes = Axes(    #
            x_range=[0, 0.5],   # Creo que es una escala de la futura función a dibujar
            y_range=[0, 0.5],   # Creo que es una escala de la futura función a dibujar
            x_length=4,  # Longitud del eje x
            y_length=4,  # Longitud del eje y
            axis_config={  # Configuración de los ejes
                "color": BLACK,  # Definimos el color de los ejes a negro
                "include_tip": True,
                "tip_shape": ArrowSquareTip,  # Cambia la forma de la punta de la flecha a un estilo cuadrado
                "tip_length": 100,  # Ajusta el tamaño de la flecha
                },
            x_axis_config={
                "include_ticks": False,  # Quita las divisiones pequeñas
            },
            y_axis_config={
                "include_ticks": False,  # Quita las divisiones pequeñas
            }
        )
        
        
        self.wait(2)
    
        # Crear la etiqueta de los ejes
        label_deterministic = Tex(r"\textbf{Determinista}", color=BLACK)
        # Ajustar el tamaño de la etiqueta con .scale()
        label_deterministic.scale(1.25)  # Escalar a 1.5 veces su tamaño original
        # Posicionar la etiqueta debajo de los ejes
        label_deterministic.next_to(axes, UP)  # `DOWN` indica que va debajo
        # Posicionar la etiqueta debajo de los ejes con un espacio extra
        label_deterministic.next_to(axes, UP, buff=1.0)  # `buff` ajusta la distancia
   
        
        # Etiquetas de los ejes
        labels = axes.get_axis_labels(x_label="Tiempo", y_label="Predicciones")
        # Ajustar el tamaño de la etiqueta con .scale()
        labels.scale(0.75)  # Escalar a 1.5 veces su tamaño original
        
        # Cambiar el color de las etiquetas
        labels.set_color(BLACK)  # Cambia el color a negro
        
        # Definición de la curva exponencial
        exponential_curve = (axes.plot(lambda x: (x**2)*(7/5), color="#8B0000"))

        # Título de la curva
        curve_label = MathTex("Etiqueta \; de \; la \; curva", color=RED).next_to(exponential_curve, UP)
        # Ajustar el tamaño de la etiqueta con .scale()
        curve_label.scale(0.75)  # Escalar a 1.5 veces su tamaño original

        # Cambiar la tipografía del texto MathTex
        curve_label.set_font("Times New Roman")  # Tipografía moderna
        
   

        # Añadir objetos a la escena
        self.play(Write(label_deterministic))
        self.play(Create(axes), Write(labels))
        self.play(Create(exponential_curve), Write(curve_label))
        
        self.wait(2)
        group_1 = VGroup(label_deterministic, axes, labels, exponential_curve, curve_label)
        
        self.play(group_1.animate.shift(LEFT * 3.65))
        self.wait(2)


# Para ejecutar esta escena, guarda el código en un archivo Python y ejecuta:
# manim -pql nombre_del_archivo.py ExponentialCurve     ESTO PARA BAJA CALIDAD
# manim -pqh nombre_del_archivo.py ExponentialCurve     ESTO PARA ALTA CALIDAD
# manim -p4k nombre_del_archivo.py ExponentialCurve     ESTO PARA ULTRA ALTA CALIDAD



""" COMBINAR ESCENAS
class CombinedScene(ImportImages, ExponentialCurve):
    def construct(self):
        # Llamar el contenido de la primera escena
        self.scene1_content()

        # Llamar el contenido de la segunda escena
        self.scene2_content()
        
"""




