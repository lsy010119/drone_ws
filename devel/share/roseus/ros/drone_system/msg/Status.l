;; Auto-generated. Do not edit!


(when (boundp 'drone_system::Status)
  (if (not (find-package "DRONE_SYSTEM"))
    (make-package "DRONE_SYSTEM"))
  (shadow 'Status (find-package "DRONE_SYSTEM")))
(unless (find-package "DRONE_SYSTEM::STATUS")
  (make-package "DRONE_SYSTEM::STATUS"))

(in-package "ROS")
;;//! \htmlinclude Status.msg.html


(defclass drone_system::Status
  :super ros::object
  :slots (_pos_n _pos_e _pos_d _vel_n _vel_e _vel_d _yaw_ang _yaw_ang_vel _connection ))

(defmethod drone_system::Status
  (:init
   (&key
    ((:pos_n __pos_n) 0.0)
    ((:pos_e __pos_e) 0.0)
    ((:pos_d __pos_d) 0.0)
    ((:vel_n __vel_n) 0.0)
    ((:vel_e __vel_e) 0.0)
    ((:vel_d __vel_d) 0.0)
    ((:yaw_ang __yaw_ang) 0.0)
    ((:yaw_ang_vel __yaw_ang_vel) 0.0)
    ((:connection __connection) nil)
    )
   (send-super :init)
   (setq _pos_n (float __pos_n))
   (setq _pos_e (float __pos_e))
   (setq _pos_d (float __pos_d))
   (setq _vel_n (float __vel_n))
   (setq _vel_e (float __vel_e))
   (setq _vel_d (float __vel_d))
   (setq _yaw_ang (float __yaw_ang))
   (setq _yaw_ang_vel (float __yaw_ang_vel))
   (setq _connection __connection)
   self)
  (:pos_n
   (&optional __pos_n)
   (if __pos_n (setq _pos_n __pos_n)) _pos_n)
  (:pos_e
   (&optional __pos_e)
   (if __pos_e (setq _pos_e __pos_e)) _pos_e)
  (:pos_d
   (&optional __pos_d)
   (if __pos_d (setq _pos_d __pos_d)) _pos_d)
  (:vel_n
   (&optional __vel_n)
   (if __vel_n (setq _vel_n __vel_n)) _vel_n)
  (:vel_e
   (&optional __vel_e)
   (if __vel_e (setq _vel_e __vel_e)) _vel_e)
  (:vel_d
   (&optional __vel_d)
   (if __vel_d (setq _vel_d __vel_d)) _vel_d)
  (:yaw_ang
   (&optional __yaw_ang)
   (if __yaw_ang (setq _yaw_ang __yaw_ang)) _yaw_ang)
  (:yaw_ang_vel
   (&optional __yaw_ang_vel)
   (if __yaw_ang_vel (setq _yaw_ang_vel __yaw_ang_vel)) _yaw_ang_vel)
  (:connection
   (&optional __connection)
   (if __connection (setq _connection __connection)) _connection)
  (:serialization-length
   ()
   (+
    ;; float64 _pos_n
    8
    ;; float64 _pos_e
    8
    ;; float64 _pos_d
    8
    ;; float64 _vel_n
    8
    ;; float64 _vel_e
    8
    ;; float64 _vel_d
    8
    ;; float64 _yaw_ang
    8
    ;; float64 _yaw_ang_vel
    8
    ;; bool _connection
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _pos_n
       (sys::poke _pos_n (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pos_e
       (sys::poke _pos_e (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pos_d
       (sys::poke _pos_d (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_n
       (sys::poke _vel_n (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_e
       (sys::poke _vel_e (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_d
       (sys::poke _vel_d (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw_ang
       (sys::poke _yaw_ang (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw_ang_vel
       (sys::poke _yaw_ang_vel (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _connection
       (if _connection (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _pos_n
     (setq _pos_n (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pos_e
     (setq _pos_e (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pos_d
     (setq _pos_d (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_n
     (setq _vel_n (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_e
     (setq _vel_e (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_d
     (setq _vel_d (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw_ang
     (setq _yaw_ang (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw_ang_vel
     (setq _yaw_ang_vel (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _connection
     (setq _connection (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get drone_system::Status :md5sum-) "8e5d164adbff825645eb62cf6f3d00a8")
(setf (get drone_system::Status :datatype-) "drone_system/Status")
(setf (get drone_system::Status :definition-)
      "float64 pos_n
float64 pos_e
float64 pos_d
float64 vel_n
float64 vel_e
float64 vel_d
float64 yaw_ang
float64 yaw_ang_vel
bool connection


")



(provide :drone_system/Status "8e5d164adbff825645eb62cf6f3d00a8")


