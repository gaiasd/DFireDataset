##  D-Fire: an image dataset for fire and smoke detection

**Authors:** Researchers from Gaia, solutions on demand ([GAIA](https://www.gaiasd.com/))

### About

D-Fire is an image dataset of fire and smoke occurrences designed for machine learning and object detection algorithms with more than 20,000 images.

<table>
<tr><th>Number of images</th><th>Number of bounding boxes</th></tr>
<tr><td>

| Category | # Images |
| ------------- | ------------- |
| Only fire  | 1,164  |
| Only smoke  | 5,868  |
| Fire and smoke  | 4,657  |
| None  | 9,838  |

</td><td>

| Class | # Bounding boxes |
| ------------- | ------------- |
| Fire  | 14,691 |
| Smoke  | 11,865  |

</td></tr> </table>

All images were annotated according to the YOLO format (normalized coordinates between 0 and 1).

***

### Download

* [Download D-Fire Dataset (only images and labels)](https://drive.google.com/drive/folders/1DWgsQLVgkkLM8m-VcugHNpD5WYDbjYp5?usp=sharing).
* [Download some surveillance videos](https://drive.google.com/drive/folders/1P5TNDP7ZrWpIZ4v_Aav5hf3S9UII2ZKA?usp=sharing).
* If you want more surveillance videos, please request your registration on our environmental monitoring website ["Apaga o Fogo!" (Put out the Fire!)](https://apagaofogo.eco.br/).
* Data splitting is also available [here](https://drive.google.com/drive/folders/1Np_FC3MuuFJgV-z0FmZwS9YzsTKdyRGJ?usp=sharing).

### Citation

Please cite our paper in your publications if you use this dataset.

```
@inproceedings{Venancio2021,
title = {{Fire Detection based on a Two-Dimensional Convolutional Neural Network and Temporal Analysis}},
author = {Pedro Vinícius A. B. de Venâncio and Tamires M. Rezende and Adriano C. Lisboa and Adriano V. Barbosa},
year = {2021},
booktitle = {IEEE Latin American Conference on Computational Intelligence (LA-CCI)},
pages = {1-6},
}
```
