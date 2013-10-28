Configuracion encriptada en Emacs
=================================

:date: 2013-10o-28, 17:52
:tags: [emacs, elisp]

En mi aprendizaje de Emacs he descubierto el módulo `jabber.el`_ que te permite
mantener las conversaciones de Google Talk dentro del propio editor. Pero 
hay que pasarle las contraseñas o guardarlas en modo plano, lo cual es algo 
incomodo desde el punto de vista de la seguridad. Si bien para la cuenta del 
trabajo me daria igual ya que no usa la autenticación de dos factores y por lo
tanto me se de memoria mi contraseña, en la personal si lo tengo habilitado y
la desconozco y aunque la conociera, seria poco afortunado guardarla como texto
plano.

Por ello, buscando un poco he encontrado como cifrar un fichero *.el* y la 
verdad es que es tremendamente sencillo. Para empezar hay que habilitar la 
extensión *.el.gpg* por lo que incluimos en nuestro .emacs:

.. code:: elisp

    (add-to-list 'load-suffixes ".el.gpg")

A partir de aqui, solo hay que crear un fichero con dicha extensión y Emacs 
sabrá que hacer ;) Cada vez que guardes, te pedirá la contraseña con la que 
debe cifrar el contenido.

Y ya se puede incluir el fichero con 

.. code:: elisp

   (require 'fichero-cifrado)

con lo que puedes usar lo que haya dentro en el resto del editor.

.. _jabber.el: http://sf.net/p/emacs-jabber
