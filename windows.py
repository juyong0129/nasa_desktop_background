import requests
from bs4 import BeautifulSoup
import ctypes
import os

def set_wallpaper(image_path):
    abs_path = os.path.abspath(image_path)
    result = ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)


url = "https://www.nasa.gov/image-of-the-day/"

response = requests.get(url)
print(response)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    big_div = soup.find("div", class_="hds-gallery-items")
    parent_div = next(big_div.children, None)
    self_a = next(parent_div.children, None)
    self_list = list(self_a.children)
    img_tag = self_list[1]
    img_url = img_tag["src"]
    img = requests.get(img_url)
    save_path = "wallpaper.jpg"

    with open(save_path, "wb") as file:
        file.write(img.content)

    print("saved correctly")

    set_wallpaper(save_path)

    print("The wallpaper has been applied successfully.")