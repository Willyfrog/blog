Receta para introspeccion en python
###################################

:date: 2012-06-15 10:43
:author: Willyfrog
:category: python
:tags: [aprendizaje, programación, python, snipet]
:slug: receta-para-introspeccion-en-python

Al final no me ha servido ya que hay varias propiedades que no son
legibles en el codigo legacy que estoy mirando, pero por si a alguien le
sirviera copio una receta vista en `SO`_ para ver los contenidos de un
objeto:

:Original: `diveintopython`_  
:Author:   Mark Pilgrim (mark@diveintopython.org)

.. code-block:: python

   def info(object, spacing=10, collapse=1):
      """
      Print methods and doc strings.
      Takes module, class, list, dictionary, or string.
      """
   
       methodList = [e for e in dir(object) if callable(getattr(object, e))]
       processFunc = collapse and (lambda s: " ".join(s.split())) or (lambdas: s)
       print "\\n".join(["%s %s" %
           (method.ljust(spacing),
            processFunc(str(getattr(object, method).\_\_doc\_\_)))
            for method in methodList])
   
       if name == "main":
           print help.doc

En parte no lo uso por como está estructurado el codigo este que
tenemos, de hecho finalmente una variación más sencilla y peor
formateada me sirvió para lo que queria:

.. code-block:: python

    lista_negra = ['atributos problematicos aqui'] 
    logWARN("%s" % ["%s: %s" % (val, getattr(self, val, "No legible")) for val in dir(self) if val not in lista_negra])``

la lista negra es porque en este trozo de codigo concreto hay muchos
'alias' de funcion y al solicitar su valor ejecuta la funcion la cual ni
siquiera esta en el contexto apropiado. Supongo que es lo que tiene que
el objeto contenga unos 600 valores entre atributos, métodos y alias
T\_T

.. _SO: http://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object
.. _diveintopython: http://diveintopython.net/
