
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
   1.