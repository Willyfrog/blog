time, datetime, epoch y el lio de todos los tiempos
###################################################

:date: 2011-10-31 13:17
:author: Willyfrog
:category: python
:tags: [briconsejo, programación, python]
:slug: time-datetime-epoch-y-el-lio-de-todos-los-tiempos

Estoy intentando hacer la transición del código de Python de una
aplicación desde mx.DateTime a la librería estándar de Python datetime.
Las razones son 2, por un lado quitarnos una dependencia que no hace
falta realmente y por otra facilitar la transición a psycopg2 (estamos
usando el 1 ahora mismo). La mayor parte de las cosas son fácilmente
traducibles ya que en ocasiones usan la misma sintaxis o parecida.

Si bien nadie debería jugar demasiado con `epoch`_ dado que Python
ofrece múltiples opciones para jugar con la fecha tanto en mx.DateTime
como en datetime, parece que los tiempos de C no se olvidan y hay quien
lo prefiere. Esto, me ha supuesto un problema ya que para traer una
fecha de un timestamp a datetime es sencillo, pero la inversa no. En
cualquier otro caso estaría estudiando un poco el código para adaptarlo
y hacerlo sencillo, pero dado que tengo que cambiar algo más de 100
ficheros, me corre cierta prisa cambiar todo y que de primeras funcione
igual, es decir que no puedo cambiar apenas el código mas que lo
estrictamente necesario.

Por si alguien más lo necesita, el código para pasar de datetime al
número de segundos desde 'epoch' sería el siguiente:

.. code-block:: python

    time.mktime(datetime.datetime.today().timetuple())

datetime.datetime.today() puede sustituirse por cualquier otra fecha en
formato datetime, además se pierde la precisión del float debido al uso
de timetuple, por lo que si los microsegundos son importantes, esta no
es una forma válida, aunque posiblemente sería parcheable.

`Fuente`_

.. _epoch: http://en.wikipedia.org/wiki/Unix_epoch
.. _Fuente: http://bytes.com/topic/python/answers/522572-datetime-timestamp
