interrupt.el
============

:date: 2014-05o-23, 20:26
:tags: [elisp, lisp, emacs]

Pues poco a poco he seguido aprendiendo `Emacs`_, diversos sabores de lisp (ninguno a fondo aun) y entre ellos bastante elisp. La cosa es que cada dia disfruto más con Emacs y cada vez estoy mas enredado con él. Hasta el punto que empiezo a desarrollar pequeñas utilidades para mi día a día.

Y de ahí este post, recientemente en mi trabajo tengo la necesidad de mantener un log de las interrupciones sufridas a lo largo de una jornada de trabajo. Es algo que no debería necesitar, pero la freecuencia es elevada y el equipo ha visto la necesidad de hacer algo así. Como cada cual usamos un editor distinto y es algo extraoficial, no hay un metodo común, asi que cada cual se ha buscado las castañas.

En mi caso, como queria aprender `org-mode`_, empecé con un fichero donde iba anotando las interrupciones. Una interrupcion: un elemento en la lista, añadia la fecha y marcaba mediante tags al *interruptor*. En unos dias resultaba un tanto tedioso hacer todo esto, por lo que me pareció el momento perfecto para intentar usar un poco *elisp-fu* y de ahi surgio `interrupt.el`_

Asi que ahora simplemente pulsando <F12> puedo añadir el nombre de quien me interrumpa, ir a ver qué necesita la persona y cuando vuelva tendré el cursor esperando para añadir el motivo. Como extra, puedo pulsar despues <S-F12> y además apuntará la cantidad de minutos que he estado durante la interrupcion.

Desde luego aun está en sus primeras versiones, pero ya hace mucho más de lo que pensaba poner en un principio asi que ya veremos como continua.

.. _Emacs: http://www.gnu.org/software/emacs/
.. _org-mode: http://orgmode.org/
.. _interrupt.el: https://github.com/Willyfrog/interrupt.el
