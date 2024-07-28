from heic2png import HEIC2PNG
import fnmatch
import os
from tqdm import tqdm


mylist = list()

for file_name in os.listdir('input'):
    if fnmatch.fnmatch(file_name, '*.heic'):
        mylist.append(file_name)


for file_name in tqdm(mylist):
        heic_img = HEIC2PNG(image_file_path=f'input/{file_name}', quality=100) 
        heic_img.save(output_image_file_path = f'output/{file_name[:-5]}.png')