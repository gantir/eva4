import json
import os
from typing import List
# import requests

import math
import shutil
from PIL import Image


def get_json_files():
  files = []
  interested_extension = ".json"
  for (dirpath, dirnames, filenames) in os.walk("/Users/projects/work/learning/eva4/s13/data/source"):
    dirnames[:] = [d for d in dirnames if d not in [".venv","images"]]
  return (dirpath, [f for f in filenames if f.endswith(interested_extension)])

def get_image_paths(dirpath: str, files: List) -> List:
  image_paths = []
  for i, file in enumerate(files):
    with open(os.path.join(dirpath,file)) as js:
      file_dict = json.load(js)
      for image in file_dict["images_results"].items():
        image_paths.append((i*100+int(image[1]['position']), image[1]['original']))
  return image_paths

def get_image(src_url: str, dest_file: str):
  resp = requests.get(src_url, stream=True, verify=False)
  local_file = open(dest_file, 'wb')
  resp.raw.decode_content = True
  shutil.copyfileobj(resp.raw, local_file)
  del resp
  local_file.close()

def download_images(images_src_url: List[str]):
  for index, image_url in images_src_url:
    file_path = os.path.join(os.getcwd(),"images",str(index)+".jpg")
    print(image_url, file_path)
    get_image(image_url, file_path)

def resize_image(dir_path: str, desired_width: int) -> List:
  for (dirpath, dirnames, filenames) in os.walk(dir_path):
    for f in filenames:
      print('Processing file: {}'.format(f))
      try:
        im = Image.open(os.path.join(dirpath, f))
        width, height = im.size
        new_width = desired_width
        if(im.size[0] > new_width):
          new_height = math.floor((new_width/width) * height)
          if(new_height > new_width):
            new_height = new_width
            new_width = math.floor((new_height/height) * width)
          # print(f,(width, height),(new_width, new_height))
          k = im.resize((new_width, new_height)).convert('RGB')
          k.save(os.path.join(dirpath,"../resized",f))
      except Exception as ex:
        print(ex, f)
        pass

def list_file_contents(dir_path: str):
  for (dirpath, dirnames, filenames) in os.walk(dir_path):
    for f in filenames:
      with open(os.path.join(dirpath, f)) as file:
        k = file.readlines()
        if len(k) == 0:
          print(f,k)

# list_file_contents("/Users/projects/work/learning/YoloV3_Annotation_Tool/Labels/woody")
resize_image("/Users/projects/work/learning/eva4/s13/data/customdata/images/spare",640)
# dirpath, json_files = get_json_files()
# image_paths = get_image_paths(dirpath, json_files)
# download_images(image_paths)