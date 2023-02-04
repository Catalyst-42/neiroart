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
    Универсальный сборник скриптов для генерации изображений.
</p>

### Установка

Для работы скриптов понадобятся следующие python-пакеты:

- numpy
- Pillow

Для настройки среды установите модули в соответствии с `requirements.txt`:

```
$ pip3 install -r requirements.txt
```

### Настройки

Практически в каждом скрипте доступны параметры:

- `MAX_X` = длина изображения;
- `MAX_Y` = высота изображения;
- `MAX_ITERS` = максимальное количество итераций при генерации;
- `RESIZE_TO` = кортеж для маштабирования по X и Y.

## Процедурная генерация

#### `map_simple.py`

<img src="./img/map-simple.png" width=400px alt="map_simple">

#### `map_linear.py`

<img src="./img/map-linear.png" width=400px alt="map_linear">

#### `map_squared.py`

<img src="./img/map-squared.png" width=400px alt="map_squared">

## Генерация из набора текстур и символов

#### `glyphs.py`

<img src="./img/glyphs.png" width=400px alt="glyphs">

#### `enemies.py`

<img src="./img/enemies.png" width=400px alt="enemies">

#### `zombatar.py`

<img src="./img/zombatar.png" width=400px alt="zombatar">
