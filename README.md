##  D-Fire: an image dataset for fire and smoke detection

**Authors:** Researchers from Gaia, solutions on demand ([GAIA](https://www.gaiasd.com/))

### About

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

### Examples

<div align="center">
    <img src="https://lh3.googleusercontent.com/pw/AL9nZEUAI1XO1nuK0XmTSxd01nma6VZkZJ5Jrnj_qIvhqe1uxziYXmTnO5GLAFEdyric37YHGLersFbnZOZ1UQ5nOX057Kgze4d8d-fdX34O9972BnUI4n4zLt8_Lw0nm03cp8qqLX-72VRUHzMf01j-8XvtYg=s721-no" width="600"</img> 
</div>

### Download

* [D-Fire dataset (only images and labels)](https://1drv.ms/f/c/c0bd25b6b048b01d/EoGlv1-7_ZlGqvKdi1rulI0B0_Tho1F1sHzn_yU8uXFwoQ?e=G8MjXb).
* [Training, validation and test sets](https://1drv.ms/f/c/c0bd25b6b048b01d/Ema8FFze8mFIlM1Hn81BUUgBSyCe3R8DpI-tN5ZLOOGu5g?e=Vgdlo4).
* [Some surveillance videos](https://1drv.ms/f/c/c0bd25b6b048b01d/EhT2Jy6L-YlGvZv-gXH2SnYB0XJXbv5dQc1fC4ZvlM2GKg?e=aAkHmt). 
* [Some deep learning models trained with the D-Fire dataset](https://github.com/pedbrgs/Fire-Detection).
* For more surveillance videos, request your registration on our environmental monitoring platform ["Apaga o Fogo!" (Put out the Fire!)](https://apagaofogo.eco.br/).

### Citation

Please cite the following paper if you use our image database:

- <p align="justify">Pedro Vinícius Almeida Borges de Venâncio, Adriano Chaves Lisboa, Adriano Vilela Barbosa: <a href="https://link.springer.com/article/10.1007/s00521-022-07467-z"> An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices. </a> In: Neural Computing and Applications, 2022.</p>

If you use our surveillance videos, please cite the following paper:
- <p align="justify"><b>Pedro Vinícius Almeida Borges de Venâncio</b>, Roger Júnio Campos, Tamires Martins Rezende, Adriano Chaves Lisboa, Adriano Vilela Barbosa: <a href="https://link.springer.com/article/10.1007/s00521-023-08260-2"> A hybrid method for fire detection based on spatial and temporal patterns. </a> In: Neural Computing and Applications, 2023.</p>
