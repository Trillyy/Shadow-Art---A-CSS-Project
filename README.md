# Shadow Box Art Creation

![Banner](/banner.png)

![BadgeCSS](https://img.shields.io/badge/Language-CSS-blue) 
![BadgeWork](https://img.shields.io/badge/Work-In%20Progress-yellow)

Fun Project to automate a small CSS box-shadow trick and create wonderful art in a click

**Description:** Python module to generate a class that you can assign to a div and display an image, with no actual backgrounds shown

**WARNING:** This script may get very slow for very big images, plus it is not guaranteed to work with every image

## Project setup
1. Download ShadowBoxArtCreation.py
2. Import the module. The only function available is:
```
generate(img, pixel)
```
### img
**Description:** path to the target image (relative or absolute), only local path are working for now

**Default Value:** img.jpg

### pixel
**Description:** mapping of real image pixels with box shadow visualization

**Default Value:** 1 (same as the image)