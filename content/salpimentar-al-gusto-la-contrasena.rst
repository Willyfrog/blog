Salpimentar al gusto la contraseña
##################################

:date: 2011-12-09 13:14
:author: Willyfrog
:category: python
:tags: [aprendizaje, programación, python, snipet]
:slug: salpimentar-al-gusto-la-contrasena

Actualmente estoy trabajando en un prototipo de aplicación bastante
sencillo, pero que requiere que aprenda bastantes cosas (y por lo tanto
voy algo lento). Uno de los pequeños problemas con los que me enfrenté
fue la creación de un sistema de usuarios y no quería dejar el
*password* en abierto en la base de datos aun cuando solo fuera a
utilizarlo yo.

Echando un ojo al módulo `crypt`_ de *Python*, requería un poco de
`sal`_, por lo que me vi de repente con que no quería meter la sal ni en
un fichero de configuración ni obviamente en el código fuente. Por lo
que finalmente decidí que la sal iba a ser parte del login y de ahí
sacar todo. Así para comprobar la clave únicamente hago:

.. code-block:: python

    from crypt import crypt
    def auth(self, clave):     
        '''Comprueba si la clave suministrada es la del usuario'''
        return self.password == crypt(clave,self.username[:2])

El motivo de usar 2 caracteres es únicamente debido a los ejemplos que
vi de uso de *crypt*, imagino que se podrían más caracteres, pero no me
pareció necesario.

Si acaso, mi mayor problema con esta implementación es que la sal se
vuelve conocida con solo leer el código y no se si a partir de ahí y con
la clave encriptada se podría sacar la clave en plano. Por ahora y para
la demo, esto me sirve y más adelante estudiaré mejores sistemas de
encriptación y almacenado.

Mientras tanto, lo publico por si a alguien le viene bien.

Ah, decir además que esto lo uso mezclado con el decorator que
sugieren en un `snippet`_ de `Flask`_, pero obviamente cambiando la
manera de acceso.

.. _crypt: http://docs.python.org/library/crypt.html
.. _sal: http://en.wikipedia.org/wiki/Salt_%28cryptography%29
.. _snippet: http://flask.pocoo.org/snippets/8/
.. _Flask: http://flask.pocoo.org
