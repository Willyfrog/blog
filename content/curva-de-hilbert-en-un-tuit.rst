Curva de Hilbert en un 'tuit'
#############################
:date: 2012-03-14 17:33
:author: admin
:category: python
:tags: matematicas, programación, python, snipet
:slug: curva-de-hilbert-en-un-tuit

Actualmente estoy mirando implementaciones de las curvas de `Peano`_ y
`Hilbert`_ y me he encontrado en la `lista de python-argentina`_ con una
curiosa implementación de una curva de Hilbert en un tweet (es decir en
140 caracteres o menos):

.. code-block:: python
    :linenos:

    from turtle import *
    l=left
    f=forward
    def h(n,a):
        if n:n-=1;l(a*3);h(n,-a);f(4);l(a);h(n,a);f(4);h(n,a);l(a);f(4);h(n,-a);l(a*3)
    h(6,90)

Además no conocía el módulo de la tortuga

.. _Peano: http://es.wikipedia.org/wiki/Curva_de_Peano
.. _Hilbert: http://es.wikipedia.org/wiki/Curva_de_Hilbert
.. _lista de python-argentina: http://comments.gmane.org/gmane.org.user-groups.python.argentina/43309
