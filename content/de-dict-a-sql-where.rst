De dict a sql where
###################

:date: 2011-10-28 12:27
:author: Willyfrog
:category: python
:tags: [list comprehension, optimizacion, programación, python, pythonic]
:slug: de-dict-a-sql-where

he decidido mejorar un poco el codigo de una de las funciones heredadas
de alguien que ni siquiera conozco (por suerte) y he decidido
convertirlo de

.. code-block:: python

    buf.write(" WHERE 1=1 ")
    for col in to.pk:
        buf.write( " AND " )
        buf.write( col )
        buf.write( " = %s" )
        par.append( getattr( obj, to.map[ col ] ) )

a esto otro

.. code-block:: python

    buf.write("WHERE %s" % " AND ".join(["%s = %s" % (col,getattr(obj,to.map[col])) for col in to.pk])

