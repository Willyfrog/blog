Cargando modulos dinámicamente en la botella
############################################

:date: 2012-11-04 11:42
:author: Willyfrog
:category: [proyecto, python]
:tags: [api, bottle, programación, python, pythonic, snipet]
:slug: cargando-modulos-dinamicamente-en-la-botella

Estoy algo liado montando una api para un pequeño proyecto mio, buscando
que sea lo más cercano a RESTFUL por motivos laborales y por aprender
cosas nuevas (entremedias estoy probando Emacs, que me esta costando un
rato el cambio desde Vim).

Como framework estoy usando `bottle`_, ya que siempre estoy usando
Flask y quería probar otro distinto a ver qué tal. Y más adelante
intentaré montarlo de manera asíncrona, pero eso para más adelante.

Como digo, es una primera aproximación, imagino que el código final
tendrá una pinta muy diferente, pero para alguien que quiera cargar
dinámicamente los módulos y tratar de ejecutar las funciones es un buen
punto de partida.

.. code-block:: python
    :linenos:

    @route('/:module/:action')  # las rutas dinámicas están compuestas de la forma modulo/función
    def run_action(module,action):
        try:
            m = import_module(module)
        except ImportError:
            redirect('/404')
        action_call = module + '_' + action 
    # para evitar que cualquier función del modulo pueda ser llamada, solo aquellos que comienzan por el nombre del modulo pueden ser invocados
        try:
            a = getattr(m, action_call)
        except AttributeError, e:  # diferencia entre fallo por modulo o accion
            print "ERROR: module %s doesn't have a %s function" % (module, action_call)
            print "ERROR: %s" % e
            redirect('/400')
        return a()

A este código habría que añadir el paso de parámetros, así como si hay
diferenciación por método (get, post, put o delete)

.. _bottle: http://bottlepy.org/
