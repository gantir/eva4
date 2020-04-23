import json
import os
from typing import List
import requests

import shutil

def get_json_files():
  files = []
  interested_extension = ".json"
  for (dirpath, dirnames, filenames) in os.walk("/Users/projects/Downloads/toystory"):
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

dirpath, json_files = get_json_files()
image_paths = get_image_paths(dirpath, json_files)
download_images(image_paths)