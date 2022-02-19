// Auto-generated. Do not edit!

// (in-package drone_system.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Status {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pos_n = null;
      this.pos_e = null;
      this.pos_d = null;
      this.vel_n = null;
      this.vel_e = null;
      this.vel_d = null;
      this.yaw_ang = null;
      this.yaw_ang_vel = null;
      this.connection = null;
    }
    else {
      if (initObj.hasOwnProperty('pos_n')) {
        this.pos_n = initObj.pos_n
      }
      else {
        this.pos_n = 0.0;
      }
      if (initObj.hasOwnProperty('pos_e')) {
        this.pos_e = initObj.pos_e
      }
      else {
        this.pos_e = 0.0;
      }
      if (initObj.hasOwnProperty('pos_d')) {
        this.pos_d = initObj.pos_d
      }
      else {
        this.pos_d = 0.0;
      }
      if (initObj.hasOwnProperty('vel_n')) {
        this.vel_n = initObj.vel_n
      }
      else {
        this.vel_n = 0.0;
      }
      if (initObj.hasOwnProperty('vel_e')) {
        this.vel_e = initObj.vel_e
      }
      else {
        this.vel_e = 0.0;
      }
      if (initObj.hasOwnProperty('vel_d')) {
        this.vel_d = initObj.vel_d
      }
      else {
        this.vel_d = 0.0;
      }
      if (initObj.hasOwnProperty('yaw_ang')) {
        this.yaw_ang = initObj.yaw_ang
      }
      else {
        this.yaw_ang = 0.0;
      }
      if (initObj.hasOwnProperty('yaw_ang_vel')) {
        this.yaw_ang_vel = initObj.yaw_ang_vel
      }
      else {
        this.yaw_ang_vel = 0.0;
      }
      if (initObj.hasOwnProperty('connection')) {
        this.connection = initObj.connection
      }
      else {
        this.connection = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Status
    // Serialize message field [pos_n]
    bufferOffset = _serializer.float64(obj.pos_n, buffer, bufferOffset);
    // Serialize message field [pos_e]
    bufferOffset = _serializer.float64(obj.pos_e, buffer, bufferOffset);
    // Serialize message field [pos_d]
    bufferOffset = _serializer.float64(obj.pos_d, buffer, bufferOffset);
    // Serialize message field [vel_n]
    bufferOffset = _serializer.float64(obj.vel_n, buffer, bufferOffset);
    // Serialize message field [vel_e]
    bufferOffset = _serializer.float64(obj.vel_e, buffer, bufferOffset);
    // Serialize message field [vel_d]
    bufferOffset = _serializer.float64(obj.vel_d, buffer, bufferOffset);
    // Serialize message field [yaw_ang]
    bufferOffset = _serializer.float64(obj.yaw_ang, buffer, bufferOffset);
    // Serialize message field [yaw_ang_vel]
    bufferOffset = _serializer.float64(obj.yaw_ang_vel, buffer, bufferOffset);
    // Serialize message field [connection]
    bufferOffset = _serializer.bool(obj.connection, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Status
    let len;
    let data = new Status(null);
    // Deserialize message field [pos_n]
    data.pos_n = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pos_e]
    data.pos_e = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pos_d]
    data.pos_d = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [vel_n]
    data.vel_n = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [vel_e]
    data.vel_e = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [vel_d]
    data.vel_d = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw_ang]
    data.yaw_ang = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw_ang_vel]
    data.yaw_ang_vel = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [connection]
    data.connection = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 65;
  }

  static datatype() {
    // Returns string type for a message object
    return 'drone_system/Status';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8e5d164adbff825645eb62cf6f3d00a8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 pos_n
    float64 pos_e
    float64 pos_d
    float64 vel_n
    float64 vel_e
    float64 vel_d
    float64 yaw_ang
    float64 yaw_ang_vel
    bool connection
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Status(null);
    if (msg.pos_n !== undefined) {
      resolved.pos_n = msg.pos_n;
    }
    else {
      resolved.pos_n = 0.0
    }

    if (msg.pos_e !== undefined) {
      resolved.pos_e = msg.pos_e;
    }
    else {
      resolved.pos_e = 0.0
    }

    if (msg.pos_d !== undefined) {
      resolved.pos_d = msg.pos_d;
    }
    else {
      resolved.pos_d = 0.0
    }

    if (msg.vel_n !== undefined) {
      resolved.vel_n = msg.vel_n;
    }
    else {
      resolved.vel_n = 0.0
    }

    if (msg.vel_e !== undefined) {
      resolved.vel_e = msg.vel_e;
    }
    else {
      resolved.vel_e = 0.0
    }

    if (msg.vel_d !== undefined) {
      resolved.vel_d = msg.vel_d;
    }
    else {
      resolved.vel_d = 0.0
    }

    if (msg.yaw_ang !== undefined) {
      resolved.yaw_ang = msg.yaw_ang;
    }
    else {
      resolved.yaw_ang = 0.0
    }

    if (msg.yaw_ang_vel !== undefined) {
      resolved.yaw_ang_vel = msg.yaw_ang_vel;
    }
    else {
      resolved.yaw_ang_vel = 0.0
    }

    if (msg.connection !== undefined) {
      resolved.connection = msg.connection;
    }
    else {
      resolved.connection = false
    }

    return resolved;
    }
};

module.exports = Status;
