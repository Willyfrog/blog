Des/activando virtualenv automaticamente
########################################

:date: 2012-08-01 15:05
:author: Willyfrog
:category: python
:tags: [bash, gist, github, python, snipet]
:slug: desactivando-virtualenv-automaticamente

Algo que no se me habia ocurrido hasta que mi compañero me lo comentó
es la activación automática del entorno virtualenv nada más entrar en el
propio directorio, de esta manera ahorramos tiempo y problemas de no
estar en el virtualenv apropiado.

Buscando un poco por la red, encontré este `gist`_ donde hacía parte
de lo que queria, ya que no terminaba el virtualenv al abandonar el
directorio, por lo que podria dar problemas al seguir en la misma linea
de comandos y ejecutar otras cosas. De ahí que modificara el script para
que al abandonar el directorio desactivara el entorno.

Para poder utilizarlo se puede poner el entorno en .venv en el
directorio o crear un enlace simbolico (llamado igualmente .venv) si
queremos tenerlo en otro lado. El script debe incluirse en .bashrc y ya
solo falta cerrar e iniciar sesión.

El script en cuestión está en un `fork del enlazado anteriormente`_.

.. _gist: https://gist.github.com/2198913
.. _fork del enlazado anteriormente: https://gist.github.com/3226639
