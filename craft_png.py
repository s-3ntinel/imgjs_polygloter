#!/usr/bin/python3

import struct

def craft_png_polyglot(payload):
  # PNG header
  #data = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0d\x49\x48\x44\x52'
  data = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
  
  #data += struct.pack('H', w)
  #data += struct.pack('H', h)
  
  # '/*' comment
  #data += b'\x2f\x2a'
  #data += b'\x2a\x2f'
  
  #pay = '=1;'
  #pay += 'alert(2);'
  #
  #data += pay.encode('utf-8')
  
  return data
