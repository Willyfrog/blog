Calculo de numeros primos
#########################

:date: 2012-01-10 09:55
:author: Willyfrog
:category: python
:tags: [optimizacion, programación, projecto euler, python, snipet]
:slug: calculo-de-numeros-primos

En un problema que resolvi recientemente en el proyecto euler, descubrí
un algoritmo sencillo para calcular numeros primos: la `criba de
eratóstenes`_ El cual inicialmente traduje a python como:

.. code-block:: python
    :linenos:

    def eratostenes(m):
        primos = set(range(2,m+1))
        for i in xrange(2,int(sqrt(m))+1):
            if i in primos:
                for j in xrange(2,m/i+1):
                    primos.discard(i*j)

        return primos

No comento el código por ser una transcripción directa del algoritmo
enlazado, asi que si no entiendes como funciona, mejor leer el articulo
de la `wikipedia`_.

El problema de esta solución es que para números grandes, el conjunto
inicial es muy grande y se crea nada mas empezar, por lo que en caso de
no tener memoria suficiente pasará lo que tiene que pasar cuando el 99%
de las aplicaciones están en la `partición de swap`_.

Por ello, cree una modificación del algoritmo de eratóstenes, para
continuar un set de primos dado:

.. code-block:: python

    def erato_follow(m,primes):
        '''
        m   - nuevo numero tope
        primes - antiguo set de numeros primos
        '''
        if not primes: #si se ha llamado sin pasar un set antiguo
                       # se trabaja como siempre
            pl = eratostenes(m)
        else:
            pl = primes
            np = set(range(max(pl),m)) #nuevos primos
            for i in xrange(2,int(sqrt(m))+1):
                if i < max(pl): #aprovechamos lo aprendido
                    for j in xrange(2,m/i+1):
                        np.discard(i*j)
                else: #sacamos los que quedan
                    for j in xrange(2,m/i+1):
                        np.discard(i*j)
            return pl | np # union de ambos

mediante esta funcion, podemos seguir aumentando el numero de primos en
incrementos manejables, si bien habrá que tener cuidado con el set
completo ya que al final acabará creciendo por encima de la memoria
disponible.

.. _criba de eratóstenes: http://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes
.. _wikipedia: http://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes
.. _partición de swap: http://es.wikipedia.org/wiki/Espacio_de_intercambio
