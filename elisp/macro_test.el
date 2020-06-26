;; Macro: defmacro name args [doc] [declare] body...
(defvar x 2)
(defmacro inc (var)
  (list 'setq var (list '1+ var)))
(inc x)
