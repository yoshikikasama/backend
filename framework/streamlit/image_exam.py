import io
import os
import requests
import streamlit as st
from PIL import Image, ImageDraw

st.title("顔認識アプリ")

SUBSCCRIPTION_KEY = os.environ["SUBSCCRIPTION_KEY"]
assert SUBSCCRIPTION_KEY

face_api_url = "<face_api_url>"
# img = Image.open("sample.jpg")


uploaded_file = st.file_uploader("Chose an image...", type="png")
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    with io.BytesIO() as output:
        img.save(output, format="JPEG")
    binary_img = output.getvalue()  ## バイナリ取得
    headers = {"Content-Type": "application/octet_stream", "Ocp-Apim-Subscription-Key": SUBSCCRIPTION_KEY}

    params = {
        "returnFaceId": "true",
        "returnFaceAttributes": "age, gender,headPose, smile, facialHair, glasses, emotion, hair,makeup, occulusion",
    }

    response = requests.post(face_api_url, params=params, headers=headers, data=binary_img)
    result = response.json()
    result

    draw = ImageDraw.Draw(img)
    draw.line([(0, 50), (200, 50), (0, 150), (200, 150)], fill="red", width=5)
    st.image(img, caption="test Image", use_column_width=True)

# with open("sample.jpg", "rb") as f:
#     binary_img = f.read()
