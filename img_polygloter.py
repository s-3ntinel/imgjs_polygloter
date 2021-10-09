#!/usr/bin/python3

import struct, sys, argparse
from craft_jpg import *
from craft_gif import craft_gif_polyglot


def save_polyglot(data, output_file):
  with open(output_file, 'wb') as f:
    f.write(data)


def main():
  parser = argparse.ArgumentParser()

  subparsers = parser.add_subparsers(dest='img_format', help='image format')

  jpg_parser = subparsers.add_parser('jpg', help='craft jpg polyglot')
  jpg_parser.add_argument('-H', '--height', default=1024, type=int, help='jpg height', dest='height')
  jpg_parser.add_argument('-W', '--width', default=1024, type=int, help='jpg width', dest='width')
  jpg_parser.add_argument('-p', '--payload', required=True, type=str, help='js payload (separate commands with a semicolon)', dest='payload')
  jpg_parser.add_argument('-o', '--output', required=True, help='specify filename for output', dest='output_file')

  gif_parser = subparsers.add_parser('gif', help='craft gif polyglot')
  gif_parser.add_argument('-p', '--payload', required=True, type=str, help='js payload (separate commands with a semicolon)', dest='payload')
  gif_parser.add_argument('-o', '--output', required=True, help='specify filename for output', dest='output_file')

  args = parser.parse_args()

  if args.img_format == 'jpg':
    jpg_check_dims(args.height, args.width)
    data = craft_jpg_polyglot(args.height, args.width, args.payload)
    save_polyglot(data, args.output_file)

  elif args.img_format == 'gif':
    data = craft_gif_polyglot(args.payload)
    save_polyglot(data, args.output_file)

if __name__ == '__main__':
  main()

