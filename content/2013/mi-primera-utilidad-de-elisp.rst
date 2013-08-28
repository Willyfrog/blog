Mi primera utilidad de elisp
============================

:date: 2013-08o-28, 11:49
:tags: [elisp, lisp, emacs]

Desde hace algún tiempo me pasé a `Emacs`_, si bien la versatilidad ya la tenía en vim (es un gran editor) con Emacs puedo además aprovechar para aprender un sabor de lisp: `emacs lisp`_ (*elisp* para abreviar). Esta es una tarea que imagino que me llevará años ya que no es un uso intensivo, sino que intentaré ir haciendo pequeñas funciones y cambios que me permitan aprovechar esa caracteristica tan genial de Emacs de ser programable.

Lo difícil es encontrar algo que hacer, por lo que lo primero que se me ha ocurrido es algo que ya he tenido que hacer varias veces: cerrar todos los buffers de un proyecto. Estoy seguro que si lo busco, encuentro que alguien ya lo ha hecho y mucho mejor que yo, pero si no voy haciendo pequeñas funciones, no creo que aprenda en la vida.

.. code-block:: elisp
    :linenos:

    (defun filter-buffers-by-file-name (partial-path)
      "return list of buffers which contains 'partial-path'"
      (remove-if (lambda (x) (or (null (buffer-file-name x))
                              (null (string-match partial-path (buffer-file-name x))))) (buffer-list)))
    
    (defun kill-project-buffers (partial-path)
      "kills all buffers which contains partial-path"
      (interactive "sPartial name:")
      (let ((kill-list (filter-buffers-by-file-name partial-path)))
        (if (null kill-list)
            (message (format "No buffers matched '%s'" partial-path))
          (if (y-or-n-p (format "killing %d buffers" (length kill-list)))
            (kill-some-buffers kill-list)
            (message ("User cancelled"))
            )
        )))

Si bien estoy seguro de que se puede hacer mejor, esta es mi segunda aproximación (la original daba mas vueltas a los datos para conseguir lo mismo) que funciona. Lo que hace es buscar entre los buffers que han sido cargados desde un fichero aquellos que contengan en su path el texto indicado, teniendo en cuenta que puede usarse expresiones regulares. De esta manera poniendo el nombre del proyecto (o parte de su path), eliminará los buffers que coincidan.

La última versión de esta funcion, podrá encontrarse siempre en `github`_

.. _github: https://github.com/Willyfrog/vimfiles/blob/master/emacs_custom.el
.. _Emacs: http://www.gnu.org/software/emacs/
.. _emacs lisp: http://en.wikipedia.org/wiki/Emacs_Lisp
