import os
import dload
import csv
import shutil
import time
from PIL import Image,ImageOps
from math import ceil
import numpy as np
import cv2
import random
import copy
import logging

logging.basicConfig(filename='logs/debug.log',
  filemode='a',
  format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
  datefmt='%H:%M:%S',
  level=logging.DEBUG
)

logger = logging.getLogger(__name__)

def download_images(img_url_file: str, img_dest: str):
  src_filepath = os.path.join(os.getcwd(), img_url_file)
  dest_filepath = os.path.join(os.getcwd(), "img_src_local_map.csv")
  with open(src_filepath) as s, open(dest_filepath,'w') as d:
    dest_file = csv.writer(d,lineterminator=os.linesep, quoting=csv.QUOTE_ALL)
    urls = sorted(set(s.readlines()))
    for i, img_url in enumerate(urls):
      img_url = img_url.strip()
      dest_image_name = "img{:04d}.jpg".format(i+1)
      dest_image_path = os.path.join(os.getcwd(), img_dest, dest_image_name)
      try:
        print("Downloading as {} image {}".format(dest_image_name, img_url))
        dest_file.writerow([dest_image_name,img_url])
        dload.save(img_url, dest_image_path)
        if "pixabay" in img_url:
          # This delay is needed as otherwise the pixabay was throwing 403 error
          time.sleep(5)
      except Exception as e:
        print("Error: Error downloading as {} image {}".format(dest_image_name, img_url))
        pass

def alter_bg_image(src_img_dir, src_img_filename, dest_img_folder):
  image_path = os.path.join(src_img_dir,src_img_filename)
  org_img = Image.open(image_path)
  gi = ImageOps.grayscale(org_img)
  altered_image = ImageOps.fit(gi,(224,224), method=Image.ANTIALIAS)
  # altered_image.show()
  altered_image.save(os.path.join(dest_img_folder,src_img_filename))

def alter_fg_image(src_img_dir, src_img_filename, dest_img_folder):
  image_path = os.path.join(src_img_dir,src_img_filename)
  MAX_SIZE = 100
  try:
    # https://pillow.readthedocs.io/en/latest/handbook/concepts.html#modes
    org_img = Image.open(image_path).convert('LA')
    width,height = org_img.size
    ratio = width/height
    new_width = MAX_SIZE
    new_height = ceil(MAX_SIZE/ratio)
    if width < height:
      new_width = ceil(MAX_SIZE*ratio)
      new_height = MAX_SIZE
    # print(ratio,src_img_filename,[width,height],[new_width,new_height])
    altered_image = ImageOps.fit(org_img,(new_width,new_height), method=Image.ANTIALIAS)
    altered_image.save(os.path.join(dest_img_folder,src_img_filename))
  except Exception as e:
    print(e)
    pass

def rename_bg_files(src_img_dir, dest_img_dir):
  img_files = sorted(os.listdir(src_img_dir))
  for i, img in enumerate(img_files):
    dest_image_name = "img{:04d}.jpg".format(i+1)
    src_img_path = os.path.join(src_img_dir, img)
    dest_image_path = os.path.join(dest_img_dir, dest_image_name)
    os.rename(src_img_path, dest_image_path)

def rename_fg_files(src_dir, dest_img_dir):
  classes = ['bird','boat','car','cat','cow','dog','person']
  img_files = []
  for cl in classes:
    for img in os.listdir(os.path.join(src_dir,cl)):
      if 'png' in img:
        img_files.append((cl,os.path.join(src_dir,cl,img)))

  class_img = []
  for i, details in enumerate(img_files):
    dest_image_name = "img{:04d}.png".format(i+1)
    dest_image_path = os.path.join(dest_img_dir, dest_image_name)
    shutil.copy2(details[1],dest_image_path)
    class_img.append((details[0],dest_image_name))

  with open('/Users/projects/Downloads/s14-15/fg_img_class_map.csv','w') as f:
    fg_map_file = csv.writer(f,lineterminator=os.linesep, quoting=csv.QUOTE_ALL)
    fg_map_file.writerows(class_img)


def generate_mask(src_img_dir, dest_img_dir):
  img_files = sorted(os.listdir(src_img_dir))
  for img in img_files:
    # https://stackoverflow.com/questions/28430904/set-numpy-array-elements-to-zero-if-they-are-above-a-specific-threshold
    image = cv2.imread(os.path.join(src_img_dir,img))
    white_indicies = image >= 1
    image[white_indicies] = 255
    dest_image_path = os.path.join(dest_img_dir, img)
    cv2.imwrite(dest_image_path, (image).astype(np.uint8))

def generate_images(source, dest):
  logger.debug("Starting to generate Images")
  bg_images = os.listdir(source['bg'])
  fg_images = os.listdir(source['fg'])
  black_image = Image.open(source['black'])
  for bg_image_name in bg_images:
    logger.debug("Background Image : {}".format(bg_image_name))
    bg_image = Image.open(os.path.join(source['bg'], bg_image_name))
    for fg_image_name in fg_images:
      logger.debug("Foreground Image : {}".format(fg_image_name))
      # https://stackoverflow.com/questions/7911451/pil-convert-png-or-gif-with-transparency-to-jpg-without
      fg_image = Image.open(os.path.join(source['fg'], fg_image_name)).convert('RGBA')
      fg_image_flip = ImageOps.mirror(fg_image)
      fg_mask_image = Image.open(os.path.join(source['fg-mask'], fg_image_name)).convert('RGBA')
      fg_mask_image_flip = ImageOps.mirror(fg_mask_image)
      for placement in range(1,21):
        x1,y1 = random.randint(1,80), random.randint(1,80)
        bg_fg = copy.deepcopy(bg_image)
        mask = copy.deepcopy(black_image)
        bg_fg_flip = copy.deepcopy(bg_image)
        mask_flip = copy.deepcopy(black_image)

        bg_fg.paste(fg_image, (x1,y1), fg_image)
        mask.paste(fg_mask_image, (x1,y1), fg_mask_image)
        bg_fg_flip.paste(fg_image_flip, (x1,y1), fg_image_flip)
        mask_flip.paste(fg_mask_image_flip, (x1,y1), fg_mask_image_flip)

        bg_fg.save(os.path.join(dest,"bg-fg/bg-{}-fg-{}-{}.jpg".format(bg_image_name.split('.')[0],fg_image_name.split('.')[0],placement)))
        mask.save(os.path.join(dest,"bg-fg-mask/bg-{}-fg-mask-{}-{}.jpg".format(bg_image_name.split('.')[0],fg_image_name.split('.')[0],placement)))
        bg_fg_flip.save(os.path.join(dest,"bg-fg-flip/bg-{}-fg-flip-{}-{}.jpg".format(bg_image_name.split('.')[0],fg_image_name.split('.')[0],placement)))
        mask_flip.save(os.path.join(dest,"bg-fg-mask-flip/bg-{}-fg-mask-flip-{}-{}.jpg".format(bg_image_name.split('.')[0],fg_image_name.split('.')[0],placement)))

if __name__ == "__main__":
    # download_images('img_src.txt','images/bg/original')
    # rename_bg_files('/Users/projects/Downloads/s14-15/images/bg/roads','/Users/projects/Downloads/s14-15/images/bg/original')
    # rename_fg_files('/Users/projects/Downloads/s14-15/images/fg/temp/','/Users/projects/Downloads/s14-15/images/fg/original/')

    # bg_img_files = sorted(os.listdir('/Users/projects/Downloads/s14-15/images/bg/original/'))
    # for img in bg_img_files:
    #   alter_bg_image('/Users/projects/Downloads/s14-15/images/bg/original/', img,'/Users/projects/Downloads/s14-15/images/bg/altered/')

    # fg_img_files = sorted(os.listdir('/Users/projects/Downloads/s14-15/images/fg/original/'))
    # for i, img in enumerate(fg_img_files):
    #   alter_fg_image('/Users/projects/Downloads/s14-15/images/fg/original/', img,'/Users/projects/Downloads/s14-15/images/fg/altered/')

    # generate_mask('/Users/projects/Downloads/s14-15/images/fg/altered/','/Users/projects/Downloads/s14-15/images/fg/mask')
    cur_dir = os.curdir
    generate_images({
      'bg': os.path.join(os.curdir,'images/bg/altered/'),
      'fg': os.path.join(os.curdir,'images/fg/altered/'),
      'fg-mask':os.path.join(os.curdir,'images/fg/mask/'),
      'black': os.path.join(os.curdir,'images/black.jpg')
    }, dest= os.path.join(os.curdir,'images/generated')
    )