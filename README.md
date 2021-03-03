# dbt-denoising-dncnn
DnCNN for Reconstructed Digital Breast Tomosynthesis

![Under development](https://img.shields.io/badge/status-under%20development-yellowgreen) • [dataset](https://github.com/ghjardim/dbt-denoising-dataset) • [dataset generator script (currently empty)](https://github.com/ghjardim/dbt-openvct-script)

Currently under development. A fork of https://github.com/wbhu/DnCNN-tensorflow.

DBT dataset is avaiable at https://github.com/ghjardim/dbt-denoising-dataset.

# Repository structure
- You can use our preprocessing scripts on ```preprocessing/``` folder.
- Then you can run dncnn on ```dncnn/``` folder.
  - It has a ```data/``` folder inside of it. It follows the following structure:
    - ```data/train/original/``` --> Holds the **Ground Truth** for **training**.
    - ```data/train/noisy/``` --> Holds the **noisy** images for **training**.
    - ```data/test/original/``` --> Holds the **Ground Truth** for **testing**.
    - ```data/test/noisy/``` --> Holds the **noisy** images for **testing**.
    - ```data/denoised/``` -->  Has the result of denoising ```data/test/noisy```.
