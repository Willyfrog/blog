Nuevo mini-proyecto: tuitorrent
###############################

:date: 2012-04-10 09:49
:author: Willyfrog
:category: [proyecto, python]
:tags: [github, programación, proyectos, python, twitter]
:slug: nuevo-mini-proyecto-tuitorrent

En estos días, he intentado sacar algo de tiempo para un mini-proyecto
que tenía en mente desde hace mucho y que recordé hace poco gracias a un
artículo: `"Como crear un bot de Twitter en Python"`_ (titulo traducido
libremente).

La idea es la de un bot de twitter al que mandarle torrents y que este
se encargue de gestionarlos. Por ahora solo descarga el torrent y lo
coloca en una carpeta, la cual está vigilada por utorrent que al
detectar el nuevo archivo lo pone a la cola. Como efecto extra, también
descarga archivos que no sean torrent, pero en este caso no se añaden a
la lista y se quedan ahí.

El `proyecto está alojado en github`_ bajo una licencia BSD de 3
clausulas (que podeis trastear con él todo lo que queráis mientras
sigáis diciendo de donde salio ;) ). Esto me recuerda que tambien tengo
que añadir la licencia al proyecto :P

Los requisitos que tiene son pocos por ahora: Python 2.X (solo he
probado con la 2.7) y python-twitter

Por ahora está en una versión muy primaria (alfa que se suele decir),
por lo que tiene varios problemas:

 - la instalación es más complicada de lo que me gustaría. Aunque he
puesto un shell script, hay que asegurarse de al menos tener python y
virtualenv, cosa no siempre disponible (para windows ni siquiera he
intentado automatizarlo). Además requiere generar un token de oauth en
twitter y darle las claves al bot, para que pueda leer y escribir de la
cuenta.

 - la ejecución requiere pasos poco necesarios fuera de un entorno de
desarrollo. Cuando desarrollo con python uso virtualenv para abstraer el
uso de librerías del resto de la máquina, esto hace que hay que activar
el entorno previamente a lanzar el cliente.

 - python-twitter tiene un problema con la codificación de caracteres
que he arrastrado y espero solucionar en algún momento, ya que justo en
mac es donde me ha sucedido, aunque espero arreglarlo esta tarde/noche.

De cara a un futuro, me gustaría por un lado facilitar el uso e
instalación del bot y por otro, montarle un pequeño sistema de plugins
de manera que pueda realizar más acciones que solo descarga de archivos
y quizás filtrar los tipos de archivos descargables o una lista blanca
de quien descargar.

.. _"Como crear un bot de Twitter en Python": http://inventwithpython.com/blog/2012/03/25/how-to-code-a-twitter-bot-in-python-on-dreamhost/
.. _proyecto está alojado en github: https://github.com/Willyfrog/tuitorrent
