# <img src="img/logo.png" style="width: 1ch; image-rendering: pixelated"> Neiroart
A collection of scripts that generate images. Generative art.

### Installation
Code written on [Python](https://www.python.org). Scripts uses `PIL` and `numpy` libraries to generate images.

```sh
pip3 install -r requirements.txt
```

### Settings
Each script has their own settings. You can show it with `-help` flag. Each script had default settings, which can be viewd and updated in `settings.toml` file.

You can also pass different `:aliases` in parameters. Aliases can be found via additional help commands:

```sh
# Glyphs
--show-glyphsets

# Colors
--show-colors
--show-colorsets

# Zombatar colors
--show-bright-colors
--show-common-colors
--show-skin-colors
```

You can add your own aliases in `aliases.py` file. All image samples for generators can be found in `src/img/` folder. 

### Examples
`zombatars.py`
| ![](img/zombatars1.png) | ![](img/zombatars2.png) | ![](img/zombatars3.png) |
|-|-|-|

`enemies.py`
| ![](img/enemies1.png) | ![](img/enemies2.png) | ![](img/enemies3.png) |
|-|-|-|

`glyphs.py`
<table width="100%">
  <tr>
    <td width="33.333%"><img src="img/glyphs1.png"></td>
    <td width="33.333%"><img src="img/glyphs2.png"></td>
    <td width="33.333%"><img src="img/glyphs3.png"></td>
  </tr>
</table>

`mapper.py`
| ![](img/mapper1.png) | ![](img/mapper2.png) | ![](img/mapper3.png) |
|-|-|-|

`worm.py`
| ![](img/worm1.png) | ![](img/worm2.png) | ![](img/worm3.png) |
|-|-|-|

`puzzles.py`
<table width="100%">
  <tr>
    <td width="33.333%"><img src="img/puzzles1.png"></td>
    <td width="33.333%"><img src="img/puzzles2.png"></td>
    <td width="33.333%"><img src="img/puzzles3.png"></td>
  </tr>
</table>

`coprimes.py`
| ![](img/coprimes1.png) | ![](img/coprimes2.png) | ![](img/coprimes3.png) |
|-|-|-|
