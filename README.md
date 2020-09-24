# A study on tooth segmentation and numbering using end-to-end deep neural networks
In this repo, you will find instructions on how to [request the data set](#Request-the-Data-Set) used to perform the experiments of the paper mentioned above.
The used data set modifies the [UFBA-UESC Dental Images Deep data set](https://github.com/IvisionLab/deep-dental-image), which contains 1500 panoramic dental X-ray images, adding more instance annotations and including numbering information.
Therefore we refer to this new data set as the **DNS Panoramic Images**, where DNS stands for Detection, Numbering, and Segmentation.
To be notified of code releases, new data sets, and errata, please watch this repo.

## Data set statistics
The data set contains 543 panoramic images, which were split into five folds.
The first four folds contain 108 images each, and the remaining one, which was used for testing, contains 111 images.
Therefore, we strongly recommend using fold number 5 (fold5) as the test data set, so your results can be compared to ours.
An additional 778 images with only binary mask annotations were used for evaluation (please refer to the original article).
The table below summarizes the data used according to categories.
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
If you use this data set, please cite:

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
This data set and its corresponding paper give continuity to other works of ours.
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

## Demonstration
Follow the jupyter notebook file ([demo.ipynb](https://github.com/IvisionLab/deep-tooth-segmentation-and-numbering/blob/master/demo.ipynb)) that we provide to get a quick sense of the data set structure.
Notice the two annotation options: a JSON file in the [COCO format](https://cocodataset.org/#format-data) and .png images, where each color encodes an instance and a tooth number.
The conversions.py file defines useful conversion functions.

## Request the Data Set
Please send an e-mail to lrebouca@ufba.br to receive a link to download the **DNS Panoramic Images** along with their annotations.
The e-mail must be sent from a professor's valid institutional account, and must include the following text (copy and paste the text below, filling the required fields, and send it with the professor's signature, in PDF attached in the e-mail):

Subject: Request to download the DNS Panoramic Images.

"Name: [your first and last name]

Affiliation: [university where you work]

Department: [your department]

Current position: [your job title]

E-mail: [must be the e-mail at the above-mentioned institution]

I have read and agreed to follow the terms and conditions below: The following conditions define the use of the DNS Panoramic Images:

This data set is provided "AS IS" without any express or implied warranty. Although every effort has been made to ensure accuracy, IvisionLab does not take any responsibility for errors or omissions;

Without the expressed permission of IvisionLab, any of the following will be considered illegal: redistribution, modification, and commercial usage of this data set in any way or form, either partially or in its entirety;

All images in this data set are only allowed for demonstration in academic publications and presentations;

This data set will only be used for research purposes. I will not make any part of this data set available to a third party. I'll not sell any part of this data set or make any profit from its use.

[your signature]"  

**P.S. A link to the data set file will be sent as soon as possible.**
