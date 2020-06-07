const path = require('path');

module.exports = Object.freeze({
  RTMPDUMP_PATH : path.join('.', 'rtmpdump', 'rtmpdump.exe'),
  FFMPEG_PATH : path.join('.', 'ffmpeg', 'bin', 'ffmpeg.exe'),
  DEFAULT_CONFIG_PATH : path.join('.', 'config', 'config.yml')
});
