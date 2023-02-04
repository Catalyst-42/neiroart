<table>
    <th><a href="./README.md">ENG</a></th>
    <th><a href="./README_ru.md">RUS</a></th>
</table>

<div align=center>
    <img src="./img/logo.png" width=128px alt="logo">
</div>

<h1 align=center>
    Neiroart
</h1>

<p align=center>
    A versatile collection of image generation scripts.
</p>

### Setup

There are some python packages required for these scripts to work:

- numpy
- Pillow

To setup the environment install modules according to `requirements.txt`:

```
$ pip3 install -r requirements.txt
```

### Settings

The following parameters can be found in almost every script file:

- `MAX_X` = the picture length;
- `MAX_Y` = the picture height;
- `MAX_ITERS` = the maximum amount of iterations during generation;
- `RESIZE_TO` = a tuple for scaling in X and Y.

## Procedural generation

#### `map_simple.py`

<img src="./img/map-simple.png" width=400px alt="map_simple">

#### `map_linear.py`

<img src="./img/map-linear.png" width=400px alt="map_linear">

#### `map_squared.py`

<img src="./img/map-squared.png" width=400px alt="map_squared">

## Generation out of texture and symbol sets

#### `glyphs.py`

<img src="./img/glyphs.png" width=400px alt="glyphs">

#### `enemies.py`

<img src="./img/enemies.png" width=400px alt="enemies">

#### `zombatar.py`

<img src="./img/zombatar.png" width=400px alt="zombatar">
