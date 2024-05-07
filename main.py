import requests
from api import API_TOKEN_KEY
from datetime import datetime
import sys

# taqaddum, which means 'progress'.
from tqdm import tqdm


# create bg_changer function
def bg_changer(img, bg_color):
    response = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(img, "rb")},
        data={"size": "auto", "bg_color": bg_color},
        headers={"X-Api-Key": API_TOKEN_KEY},
    )

    # get response content in bytes
    total_length = int(response.headers.get("content-length", 0))

    # create progress bar
    progress_bar = tqdm(total=total_length, unit="iB")

    if response.status_code == requests.codes.ok:
        with open(
            "output/hasil-%s.png" % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), "wb"
        ) as out:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    # update progress bar
                    progress_bar.update(len(chunk))

                    out.write(chunk)
    else:
        print("Error:", response.status_code, response.text)

    # close progress bar after download
    progress_bar.close()


# image path `python.exe .\main.py .\images\gambar_aku.jpg`
image_path = sys.argv[1]

# alternative way
# image_path = "images/profile-1.jpg"

# user can input the hex color code #1D76DB (blue), #DB231D (red), #FFFF00 (yellow)
color_name = str(input("Enter the color name: "))

bg_changer(image_path, color_name)
