#  D-Fire: an image dataset for fire and smoke detection

**Authors:** Researchers from Gaia, solutions on demand ([GAIA](https://www.gaiasd.com/))

## About

D-Fire is an image dataset of fire and smoke occurrences designed for machine learning and object detection algorithms with more than 21,000 images.

<div align="center">
<table>
  <tr>
    <th>Number of images</th>
    <th>Number of bounding boxes</th>
  </tr>
 
  <tr><td>

  | Category | # Images |
  | ------------- | ------------- |
  | Only fire  | 1,164  |
  | Only smoke  | 5,867  |
  | Fire and smoke  | 4,658  |
  | None  | 9,838  |

  </td><td>

  | Class | # Bounding boxes |
  | ------------- | ------------- |
  | Fire  | 14,692 |
  | Smoke  | 11,865 |

  </td></tr> 
</table>
</div>

All images were annotated according to the YOLO format (normalized coordinates between 0 and 1). 
However, we provide the yolo2pixel function that converts coordinates in YOLO format to coordinates in pixels.

***

## Examples

<p align = "center">
<img src="https://drive.google.com/uc?export=view&id=1TfxQUZd89zU7xYG3y0enivXk3rqI6sIj" width="auto" height="180"/>
<img src="https://drive.google.com/uc?export=view&id=1mIvClp9fLnKURYrRoNab8b96FZCm3Zje" width="auto" height="180"/>
</p>

## Download

* [D-Fire dataset (only images and labels)](https://drive.google.com/drive/folders/1DWgsQLVgkkLM8m-VcugHNpD5WYDbjYp5?usp=sharing).
* [Training, validation and test sets](https://drive.google.com/drive/folders/1Np_FC3MuuFJgV-z0FmZwS9YzsTKdyRGJ?usp=sharing).
* [Some surveillance videos](https://drive.google.com/drive/folders/1P5TNDP7ZrWpIZ4v_Aav5hf3S9UII2ZKA?usp=sharing). 
* [Some models trained with the D-Fire dataset](https://github.com/pedbrgs/Fire-Detection).
* For more surveillance videos, request your registration on our environmental monitoring website ["Apaga o Fogo!" (Put out the Fire!)](https://apagaofogo.eco.br/).

## Citation

Please cite the following paper if you use our image database:

- <p align="justify">Pedro Vinícius Almeida Borges de Venâncio, Adriano Chaves Lisboa, Adriano Vilela Barbosa: <a href="https://link.springer.com/article/10.1007/s00521-022-07467-z"> An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices. </a> In: Neural Computing and Applications, 2022.</p>

If you use our surveillance videos, please cite the following paper in your publications:
- Pedro Vinícius Almeida Borges de Venâncio, Tamires Martins Rezende, Adriano Chaves Lisboa, Adriano Vilela Barbosa: <a href="https://ieeexplore.ieee.org/document/9769824"> Fire Detection based on a Two-Dimensional Convolutional Neural Network and Temporal Analysis. </a> In: IEEE Latin American Conference on Computational Intelligence (LA-CCI), 2021, Temuco, Chile.
