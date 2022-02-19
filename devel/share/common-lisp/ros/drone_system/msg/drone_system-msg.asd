
(cl:in-package :asdf)

(defsystem "drone_system-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Status" :depends-on ("_package_Status"))
    (:file "_package_Status" :depends-on ("_package"))
    (:file "Status" :depends-on ("_package_Status"))
    (:file "_package_Status" :depends-on ("_package"))
  ))