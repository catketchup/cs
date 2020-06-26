(+ 3 4)
;; http://ergoemacs.org/emacs/elisp_basics.html
;; printing
(message "hi")
(message "Her age is: %d" 16) ;;%d is for number
(message "Her names is: %s" "Vicky") ;;%s if for string
(message "My list is: %S" (list 8 2 3)) ;;(message "My list is: %S" (list 8 2 3))

;; Variables
(setq x 1)
(setq a 3 b 2 c 7) ; multiple assignment
(progn (message "One") (message "Two"))

(require 'function_test)
