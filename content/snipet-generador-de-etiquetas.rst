Snipet: Generador de etiquetas
##############################

:date: 2012-03-01 23:49
:author: Willyfrog
:category: python
:tags: [generator, programación, python, snipet]
:slug: snipet-generador-de-etiquetas

Para poder generar automaticamente etiquetas para nodos (aunque valdria
para cualquier otra cosa) he hecho un generador automatico sencillo que
va dando strings de texto:

.. code-block:: python

    def generador_etiquetas(self):
        '''genera etiquetas,primero minusculas, luego mayusculas y finalmente
        digitos'''
        for a in string.lowercase:
            yield a
        for A in string.uppercase: #cuando termina con las minusculas, pasa a las
                                 #   mayusculas
            yield A
        n = 0
        while 1:
            n += 1
            yield str(n)

El while 1 en vez de while True, es porque al parecer es ligeramente más
rapido (imagino que por alguna optimización del compilador del
interprete)
