Música en una línea de codigo, versión Python
#############################################

:date: 2011-11-15 17:25
:author: Willyfrog
:category: python
:tags: [aprendizaje, música, programación, proyectos, python, pythonic, snipet]
:slug: musica-en-una-linea-de-codigo-version-python

El otro día vi en reddit `algunos`_ `temas`_ en los cuales se creaba
música a partir de una línea de código (en realidad algo mas, pero la
parte importante estaba solo en una) y como curiosidad personal, decidí
hacer una versión serpentina de dicho programa, una vez conseguido
(fácil, rápido y feo) quise poner un poco mas interés y utilizar
funciones lambda y generadores. El resultado es el siguiente:

.. code-block:: python

    #redirigir el output a /dev/audio o instalar sox y redirigir a 
    # "play -u -b 8 -t raw -r 8000 -" sin las comillas

    #modificar la parte interna de la funcion int() para variar la "melodia"
    func = lambda t: int((t<<6|t|(t<<16)) * 10 + ((t<<11) & 7))

    #generador de secuencia
    def inc(t):
        '''generador para incrementar t'''
        c=t
        while True:
            yield c
            c=c+1

    if __name__=='__main__':
        for t in inc(0):
            print("%X" % func(t))

Espero que alguien lo encuentre interesante y genere nuevas
"melodías". Quizás decir que el generador es lo que menos me ha gustado
ya que queda poco "pitónico", si bien el programa final queda bastante
legible ya que añadí algo de codigo por variar la funcionalidad inicial
y dar mas opciones con el fichero.

Para ver el resultado final recomiendo `el video`_ de los enlaces

.. _algunos: http://www.reddit.com/r/programming/comments/mbakl/experimental_oneline_algorithmic_music/
.. _temas: http://xiatek.org/?p=296
.. _el video: http://www.youtube.com/watch?feature=player_detailpage&v=qlrs2Vorw2Y#t=16s
