import sys, os
from time import sleep

sys.path.insert(0, "./../../../../..")
from src.Controller.Pages.mangafree.mangaPage.controls import find_image
from src.Controller.pattern.horizontal import alternate_page
from src.Model.save import download_images

def walk(driver, init_counter = 1, total_pages = 0, file_name = "None", folder_file = "None"):

    counter = init_counter
    not_found_pages = []
    
    while total_pages >= counter:

        image = find_image(driver, ".manga-image img")
        downloaded = download_images(image,file_name, counter, folder_file)

        if download_images is False:
            not_found_pages.append({
                "url_img": image,
                 "page": counter}
                 )

        alternate_page(driver)
        sleep(9)

        counter+=1

    return True 

