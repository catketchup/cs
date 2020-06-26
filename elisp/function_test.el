;; define a function
;; (defun function_name (param1 param2 …) "doc_string" body)
(defun myFunction1 ()
  "testing"
  (interactive)
  (message "Hello, world!"))

(myFunction1) ;;call the function
;; For 'interactive' function, M-x and type the function name

(defun myFunction2 ()
  "testing requiring a function"
  (message "I am not happy"))
(myFunction2)

;; progn, progn returns the last expression in its body.
(defun progn_test ()
  "testing progn"
  (progn
    (message "One")
    (message "Two")
    )
  )

(progn_test)

(provide 'test_function)

;; pass arguments in functions
(defun arg_fun_test (arg1 arg2)
  "passing arguments to a function"
  (+ arg1 arg2)
  )
(arg_fun_test 1 1)

;; if, (if test true_body false_body)
(if (< 1 2) 7 8)

;; if and progn
(defun compare (arg1 arg2)
  "compare two numbers"
  (interactive)
  (if (< arg1 arg2)
      (progn "<")
    (progn ">")
    )
  )
(compare 2 1)

;; let, (let (var1 var2 …) body) or (let ((var1 val1) (var2 val2) …) body)
(let (a b)
  ;; the a and b defined below only work in 'let' block
  (setq a 1)
  (setq b 2)
  (+ a b)
  (print a)
  )
(print a)

;; setq is for global variables
(setq a 2)
(print a)

(save-excursion)

;; elisp data structure
;; list
(setq mylist1 (list 1 "b" 3))
                                        ; prints a list
(message "%S" mylist1)

(setq mylist2 '(1 "b" 3))
(message "%s" mylist2)
(print mylist2)

;; use cons to build new list structure, cons object1 object2, the new element will be place in the front
(cons 1 '(2))
;; (1 2)
(cons 1 '())
;; (1)
(cons 1 2)
;; (1 . 2)

;; use push for list, equivalent to (setq listname (cons element listname))
(setq l '(a b))
(push 'c l)

;; loop with 'while', usually it's better to use dolist or dotimes(they are faster)

;; dolist macro, dolist (var list [result])
;; a good example for dolist and loops https://www.gnu.org/software/emacs/manual/html_node/eintr/dolist.html#dolist

(setq animals '(gazelle giraffe lion tiger))

(defun reverse-list-with-dolist (list)
  "Using dolist, reverse the order of LIST."
  (let (value)  ; make sure list starts empty
    (dolist (element list value)
      (setq value (cons element value)))))

(reverse-list-with-dolist animals)

;; declare, Macro: declare-function function file &optional arglist fileonly
(declare-function declare-test "testing declare" ())

;; eval-when-compile: eval-when-compile body

;; defvar and defconst: https://www.gnu.org/software/emacs/manual/html_node/elisp/Defining-Variables.html
;; defvar, for Defining Global Variables, Special Form: defvar symbol [value [doc-string]]
(defvar foo) ; not initialize it

(defvar bar 23
  "The normal weight of a bar.")
(message "%s" bar) ;initialize it

(defvar foo 32)
bar ; this doesn't change foo's value

(setq foo 32)
foo ; this changes foo's value

;; defconst, for Defining Global Variables, Special Form: defconst symbol value [doc-string]
(defconst pi 3.1415 "Pi to five places.")
pi
(setq pi 3) ; this changes pi's value
pi

;; defgroup
(defgroup defgroup-test nil
  "testing defgroup"
  :group 'defgroup-test)
;; defcustom
(defcustom defcustom-test 1
  "testing defcustom"
  :type 'integer
  :group 'defgroup-test)
;; add-to-list
;; auto-load
(provide 'function_test)
