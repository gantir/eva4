
# Image Statistics

1. __Images Details__
    - __Google Drive__ [link](https://drive.google.com/drive/folders/1GFFQp6Y-6sbVUe7X0nTiwEHXScpzdear?usp=sharing)
    - __Background Images__: 100 Images
      - __Downloaded Images__:
        - Kind: jgp images. (mostly square)
        - Path: images/bg/original
        - Size: 33MB
      - __Altered Images__:
        - Transformation: Grayscale, Scale (224*224), Crop
        - Path: images/bg/altered
        - Size: 1.1MB
    - __Foreground Images__: 100 Images
      - __Downloaded Images__:
        - Kind: png images.
        - Path: images/fg/original
        - Size: 99.8MB
        - Stats:
      - __Altered Images__:
        - Transformation: Grayscale, Scale (maxwidth 100), Crop
        - Path: images/bg/altered
        - Size: 807KB
        - Stats:
      - __Mask Images__:
        - Transformation: Python program using opencv library
        - Path: images/bg/mask
        - Size: 414KB
        - Stats:
    - __Generated Images__:
      - __Background - Foreground__: 200K Images:
        - Transformation: Pasted foreground images at 20 different positions
        - Path: images/generated/bg-fg
        - Size: 2.34GB
        - Stats:
      - __Background - Foreground Flip__: 200K Images:
        - Transformation: Pasted foreground(flipped) images at 20 different positions
        - Path: images/generated/bg-fg-flip
        - Size: 2.34GB
        - Stats:
      - __Background - Foreground Mask__: 200K Images:
        - Transformation: Pasted mask on black background images at 20 different positions
        - Path: images/generated/bg-fg-mask
        - Size: 2.34GB
        - Stats:
      - __Background - Foreground Mask Flip__: 200K Images:
        - Transformation: Pasted mask on black background(flipped) images at 20 different positions
        - Path: images/generated/bg-fg-mask-flip
        - Size: 2.34GB
        - Stats:
    - __Depth Images__:
        - Transformation:
        - Path:
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
4. Link to code to do the above steps (Not an ipynb notebook)
5. Jupyter notebook to generate Depth Images
6. Jupyter notebook to calculate stats of the images generated
