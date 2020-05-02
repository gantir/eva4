
# Image Statistics

1. Google Drive [link]()
2. Background Images: 100 Images
    - Downloaded Images:
      - Kind: jgp images. (mostly square)
      - Path: images/bg/original
      - Size: 33MB
    - Altered Images:
      - Transformation: Grayscale, Scale (224*224), Crop
      - Path: images/bg/altered
      - Size: 1.1MB
    - Foreground Images: 100 Images
      - Downloaded Images:
        - Kind: png images.
        - Path: images/fg/original
        - Size: 99.8MB
        - Stats:
      - Altered Images:
        - Transformation: Grayscale, Scale (maxwidth 100), Crop
        - Path: images/bg/altered
        - Size: 807KB
        - Stats:
      - Mask Images:
        - Transformation: Python program using opencv library
        - Path: images/bg/mask
        - Size: 414KB
        - Stats:
    - Generated Images:
      - Background - Foreground: 200K Images:
        - Transformation: Pasted foreground images at 20 different positions
        - Path: images/generated/bg-fg
        - Size: 2.34GB
        - Stats:
      - Background - Foreground Flip: 200K Images:
        - Transformation: Pasted foreground(flipped) images at 20 different positions
        - Path: images/generated/bg-fg-flip
        - Size: 2.34GB
        - Stats:
      - Background - Foreground Mask: 200K Images:
        - Transformation: Pasted mask on black background images at 20 different positions
        - Path: images/generated/bg-fg-mask
        - Size: 2.34GB
        - Stats:
      - Background - Foreground Mask Flip: 200K Images:
        - Transformation: Pasted mask on black background(flipped) images at 20 different positions
        - Path: images/generated/bg-fg-mask-flip
        - Size: 2.34GB
        - Stats:
    - Depth Images:
        - Transformation:
        - Path:
        - Size:
        - Stats:
3. Images of the dataset
    - Background Images
    - Foreground Images
    - Foreground Images masks
    - Overlay of Foreground Image or Background Images
    - Equivalent Masks
    - Depth Images
4. Dataset Creation Process. Code used for various transformations can be found [here]().
   1. download_images: method was used to download background images
   2. rename_bg_files: method was used to give bg images a proper naming following convention img:04d format.
   3. Foreground images in png format were downloaded manually/using browser plugin.
   4. rename_fg_files; method was used to give fg images a proper naming following convention img:04d format. Also a map file was created to map class and the file
   5. alter_bg_image: Used to transform the background images. Converted to grayscale and also fit the image to 224*224.
   6. alter_fg_image: Used to transform the foreground images. Converted to grayscale, scaled to Max 100 pix (width/height depending on aspect ratio)
   7. generate_mask: Used to generate mask for the foreground images. It takes the foreground png image and generates a black(transparent area) and white(actual object past). The logic used is to take the pixels which were not transparent and make them white. The rest of the image was made black
   8. generate_images: This loops through all the background and foreground images and generates images with overlay of foreground over background, foreground mask over black background etc.
   9. Depth Images
5. Link to code to do the above steps (Not an ipynb notebook)
6. Jupyter notebook to generate Depth Images
7. Jupyter notebook to calculate stats of the images generated