import requests
import os
import shutil


def download_picture(folder, filename, url):
    file_path = f"{folder}/{filename}"
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def main():
    folder = "dogs"
    if os.path.isdir(folder):
        shutil.rmtree(folder)
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


if __name__ == '__main__':
    main()
