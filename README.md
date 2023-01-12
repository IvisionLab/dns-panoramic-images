# Deprecation Warning

Do not request this data set anymore. REQUESTS WILL BE IGNORED.

This data set has been deprecated in favor of a new, soon-to-be-released data set.

# A study on tooth segmentation and numbering using end-to-end deep neural networks


## Image statistics
The work used 543 panoramic images, which were split into five folds.
The first four folds contained 108 images each, and the remaining one, which was used for testing, contained 111 images.
An additional 778 images with only binary mask annotations were used for evaluation (please refer to the original article).
The table below summarizes the images according to categories.
These categories group the images according to the presence of 32 teeth, restoration, and dental appliance, revealing the high variability of the images.
Categories 5 and 6 were excluded from the experiments because they include mouths with implants and deciduous teeth.

| Category |      32 Teeth      |     Restoration    |      Appliance     | Number and Inst. Segm. | Semantic Segm. |
|:--------:|:------------------:|:------------------:|:------------------:|:----------------------:|:--------------:|
|     1    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |           23           |       57       |
|     2    | :heavy_check_mark: | :heavy_check_mark: |                    |           174          |       80       |
|     3    | :heavy_check_mark: |                    | :heavy_check_mark: |           42           |       11       |
|     4    | :heavy_check_mark: |                    |                    |           92           |       68       |
|     7    |                    | :heavy_check_mark: | :heavy_check_mark: |           36           |       87       |
|     8    |                    | :heavy_check_mark: |                    |           128          |       355      |
|     9    |                    |                    | :heavy_check_mark: |           14           |       33       |
|    10    |                    |                    |                    |           34           |       87       |
|          |                    |                    |        Total       |           543          |       778      |

## Citation

B. Silva, L. Pinheiro, L. Oliveira, and M. Pithon, “A study on tooth segmentation and numbering using end-to-end deep neural networks,” in Conference on Graphics, Patterns and Images. IEEE, 2020.

```
@inproceedings{silva2020study,
  title={A study on tooth segmentation and numbering using end-to-end deep neural networks},
  author={Silva, Bernardo and Pinheiro, Laís and Oliveira, Luciano and Pithon, Matheus}
  booktitle={Conference on Graphics, Patterns and Images (SIBGRAPI)},
  year={2020},
  organization={IEEE}
}
```

## Previous Works
Please, consider reading and citing:

- G. Jader, J. Fontineli, M. Ruiz, K. Abdalla, M. Pithon, and L. Oliveira, “Deep instance segmentation of teeth in panoramic X-ray images,” in Conference on Graphics, Patterns and Images. IEEE, 2018.
```
@inproceedings{jader2018deep,
  title={Deep instance segmentation of teeth in panoramic X-ray images},
  author={Jader, Gil and Fontineli, Jefferson and Ruiz, Marco and Abdalla, Kalyf and Pithon, Matheus and Oliveira, Luciano},
  booktitle={Conference on Graphics, Patterns and Images (SIBGRAPI)},
  pages={400--407},
  year={2018},
  organization={IEEE}
}
```

- G. Silva, L. Oliveira, and M. Pithon, “Automatic segmenting teeth in X-ray images: Trends, a novel data set, benchmarking and future perspectives,” Expert Systems with Applications, Patterns and Images. vol. 107, pp. 15-31, 2018.
```
@article{silva2018automatic,
  title={Automatic segmenting teeth in X-ray images: Trends, a novel data set, benchmarking and future perspectives},
  author={Silva, Gil and Oliveira, Luciano and Pithon, Matheus},
  journal={Expert Systems with Applications},
  volume={107},
  pages={15--31},
  year={2018},
  publisher={Elsevier}
}
```
