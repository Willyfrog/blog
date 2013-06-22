El arbol de navidad de QBert
############################

:date: 2011-12-23 11:43
:author: Willyfrog
:category: python
:tags: [aprendizaje, list comprehension, optimizacion, programación, projecto euler, python, pythonic]
:slug: el-arbol-de-navidad-de-qbert

En el `weekly python newsletter`_, enlazaban al problema de sacar la
suma máxima, dado un árbol y utilizando el movimiento del clásico
videojuego `qBert`_ (no del todo cierto porque qBert sí podía subir,
pero eso son tecnicismos). El árbol en concreto sería así:

.. code-block:: python

        chrismasTree =   [
                        [75],
                       [95,64],
                     [17,47,82],
                    [18,35,87,10],
                   [20, 4,82,47,65],
                  [19, 1,23,75, 3,34] 
                          ]

Y las reglas son que qBert siempre debe bajar por el árbol, bien hacia
un lado o el otro.

Dado el pequeño número de datos, se puede hacer una aproximación por
fuerza bruta (recorriendo todos los posibles caminos y comparándolos)
pero esta solución sería malísima si cambiamos el set de datos al
proporcionado por el `proyecto euler`_ en su `problema 67`_, que
aseguran que si pudieras comprobar 10⁷ rutas por segundo, tadarías 20
billones americanos (millardos por aquí) de años en resolverlo.

El código para generar este segundo árbol, sería:

.. code-block:: python

        tri = []
        peUrl = "http://projecteuler.net/project/triangle.txt"
        for line in urllib.urlopen(peUrl).readlines():
            tri.append([int(x) for x in line.strip().split(" ")])
        print qbertRun(tri)

Y por si quieres intentar resolverlo, no pondré mi solución hasta
después de "Leer mas".

**Solucion:**
La parte crítica de la solución está en la siguiente función:

.. code-block:: python

        def solve_line(curr, prev):
           """
           dadas 2 lineas, hacemos una nueva con cada elemento
           max(curr[i]+prev[i],curr[i]+prev[i+1])
           """
           if not prev:
               res=curr
           else:
               res=[max(prev[i],prev[i+1])+curr[i] for i in range(len(curr))]
           return res

Es decir, tomamos el árbol de navidad como un `árbol binario`_ y
sumamos a cada línea el máximo de los dos caminos posibles.

Esto en realidad, nos daría un resultado incorrecto si lo aplicaramos
de arriba a abajo, ya que se iria por el primer resultado gordo que
hubiera, pero si invertimos el arbol y empezamos por el lado ancho, lo
que hace es recortar los caminos, dejando cada vez el camino mayor. Por
ello, la funcion que tratará los datos, lo primero que hace es invertir
la lista:

.. code-block:: python

    def qbert(arbol):
       """
       dada una lista en forma de arbol (ver variable tree) resolver
       la suma maxima pudiendo solo bajar bien a izda. o dcha.
       """
       arbol.reverse() #invertimos la lista
       res = []
       for l in arbol:
           res = solve_line(l,res)
       return res

.. _weekly python newsletter: http://www.pythonweekly.com/
.. _qBert: http://en.wikipedia.org/wiki/Qbert
.. _proyecto euler: http://projecteuler.net
.. _problema 67: http://projecteuler.net/problem=67
.. _árbol binario: http://es.wikipedia.org/wiki/%C3%81rbol_binario
