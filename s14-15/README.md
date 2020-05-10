
# Image Statistics

1. __Images Details__
    - __Google Drive__ [link](https://drive.google.com/drive/folders/1GFFQp6Y-6sbVUe7X0nTiwEHXScpzdear?usp=sharing)
    - __Background Images__: 100 Images
      - __Downloaded Images__:[link](https://drive.google.com/drive/u/0/folders/1acl9qqiut6JkRKThWtqIEmWEaipXfgVq)
        - Kind: jgp images. (mostly square)
        - Path: data/bg/original
        - Size: 33MB
      - __Altered Images__:[link](https://drive.google.com/drive/u/0/folders/1S9syiGBus-q1LwSaO_cCSLvb9GSyhd8e)
        - Transformation: RGB(224*224*3), Crop
        - Path: data/bg/altered
        - Size: 1.1MB
    - __Foreground Images__: 100 Images
      - __Downloaded Images__:[link](https://drive.google.com/drive/u/0/folders/16W5OL6HTgWf7MEytaQGG6t9pvETQEtd8)
        - Kind: png images.
        - Path: data/fg/original
        - Size: 99.8MB
        - Stats:
      - __Altered Images__:[link](https://drive.google.com/drive/u/0/folders/1CihnYUE2rhz111IKBkxhPGCe56yyVUuT)
        - Transformation: RGB+Alpha, Scale (maxwidth 100), Crop
        - Path: data/fg/altered
        - Size: 807KB
        - Stats:
      - __Mask Images__:[link](https://drive.google.com/drive/u/0/folders/1FUKPwQSyWMN78pJO1-bpNx4yoqOXZV-V)
        - Transformation: Python program using opencv library
        - Path: data/fg/mask
        - Size: 414KB
        - Stats:
    - __Generated Images__: These files were generated using a program where the files are divided among different folders and zipped in memory. Then these files are copied to google drive
      - Colab Notebook - [link](https://github.com/gantir/eva4/blob/develop/s14-15/src/ds_gen.ipynb)
      - __Background - Foreground + Flip__: 400K Images:
        - Transformation: Pasted foreground images, foreground(flipped) images at 20 different positions
        - Path: data/generated/bg-fg
        - Size: 2.34GB
        - Stats:
      - __Background - Foreground Mask__: 400K Images:
        - Transformation: Pasted mask on black background images and the foreground mask flipped at 20 different positions
        - Path: data/generated/bg-fg-mask
        - Size: 2.34GB
        - Stats:
    - __Depth Images__: The way this is accomplished is the whole foreground on background dataset is downloaded as a zip from google drive. This is then looped through one bacground image at a time (ie. 4000 images) to generate the depth images.
        - Colab Notebook - [link](https://github.com/gantir/eva4/blob/develop/s14-15/src/depth_image_gen.ipynb)
        - Transformation: Called the [DenseDepth](https://github.com/gantir/DenseDepth) model. A few changes were made to make it compatible with TF2.0. Also to be able to save individual depth images.
        - Path: data/generated/bg-fg-depth
        - Size:
        - Stats:
2. Images of the dataset
    - __Background Images__
    - __Foreground Images__
    - __Foreground Images masks__
    - __Overlay of Foreground Image or Background Images__
    - __Equivalent Masks__
    - __Depth Images__
3. __Dataset Creation Process__. Code used for various transformations can be found [here]().
   1. __download_images__: method was used to download background images
   2. __rename_bg_files__: method was used to give bg images a proper naming following convention img:04d format.
   3. Foreground images in png format were downloaded manually/using browser plugin.
   4. __rename_fg_files__: method was used to give fg images a proper naming following convention img:04d format. Also a map file was created to map class and the file
   5. __alter_bg_image__: Used to transform the background images. Converted to grayscale and also fit the image to 224*224.
   6. __alter_fg_image__: Used to transform the foreground images. Converted to grayscale, scaled to Max 100 pix (width/height depending on aspect ratio)
   7. __generate_mask__: Used to generate mask for the foreground images. It takes the foreground png image and generates a black(transparent area) and white(actual object past). The logic used is to take the pixels which were not transparent and make them white. The rest of the image was made black
   8. __generate_images__: This loops through all the background and foreground images and generates images with overlay of foreground over background, foreground mask over black background etc.
   9. Depth Images
4. [Jupyter notebook to dataset generation steps](https://github.com/gantir/eva4/blob/develop/s14-15/src/ds_gen.ipynb)
5. [Jupyter notebook to generate Depth Images](https://github.com/gantir/eva4/blob/develop/s14-15/src/ds_gen.ipynb)
6. [Jupyter notebook to calculate stats of the images generated](https://github.com/gantir/eva4/blob/develop/s14-15/src/stats_gen.ipynb)
