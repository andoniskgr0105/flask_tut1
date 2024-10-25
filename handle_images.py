import os
from PIL import Image


def get_all_photos():   
    all_photos=[]
    path_folder_photos='./static/photos/wd/'
    scan_path=os.scandir(path=path_folder_photos)
    for dir_photos in scan_path:
        if dir_photos.is_dir():
            for photo in os.scandir(dir_photos):
                all_photos.append(photo.name)
    return all_photos

def create_thumbnail_photos(path_folder_photos,folder,photo):
    folder=folder.name+'/'
    if '_FF_' in photo.name:   
        image=Image.open(str(path_folder_photos+folder+photo.name))
        MAX_SIZE=(200,200)
        image.thumbnail(MAX_SIZE)
        if not(os.path.exists('./static/photos/thumb/'+folder)):
            print("folder NOT exist") 
            os.mkdir('./static/photos/thumb/'+folder)
        image.save('./static/photos/thumb/'+folder+photo.name)
        
def get_thumbnail_photos():
    all_photos=[]
    path_folder_photos='./static/photos/thumb/'
    scan_path=os.scandir(path=path_folder_photos)
    for dir_photos in scan_path:
        if dir_photos.is_dir():
            for photo in os.scandir(dir_photos):
                all_photos.append(dir_photos.name+'/'+photo.name)
    return all_photos
    