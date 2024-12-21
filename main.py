import requests
import os
import shutil


def download_picture(folder, filename, url):
    file_path = f"{folder}/{filename}"
    response = requests.get(url)
    response.raise_for_status()
    picture = response.content
    with open(file_path, 'wb') as file:
        file.write(picture)


if __name__ == '__main__':
    folder = "dogs"
    if not os.path.isdir(folder):
        os.mkdir(folder)
    else:
        shutil.rmtree(f"{folder}")
        os.mkdir(folder)

    for number in range(50):
        payload = {"filter": "mp4,webm"}
        url = 'https://random.dog/woof.json'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        picture_link = response.json()['url']
        link, picture_extension = os.path.splitext(picture_link)
        filename = f"dog_{number + 1}{picture_extension}"
        download_picture(folder, filename,  picture_link)
