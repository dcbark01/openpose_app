import json
import requests
from PIL import Image

import streamlit as st


# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("OpenPose Web App")

# displays a file uploader widget
image = st.file_uploader("Choose an image")

# displays the select widget for the styles
# style = st.selectbox("Choose the style", [i for i in STYLES.keys()])
style = 'placeholder'

# displays a button
if st.button("Run Inference"):
    # if image is not None and style is not None:
    if image is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://openpose_backend:8081/{style}", files=files)
        paths = res.json()
        image = Image.open(paths.get("img_name"))

        with open(paths['pose_name'], 'r') as f:
            pose_data = json.loads(f.read())
        st.image(image, width=600)
        json_string = json.dumps(pose_data)

        st.download_button(label='Download Image',
                           data=open(paths.get('img_name'), 'rb').read(),
                           file_name='img_pose_001.png',
                           mime='image/png')
        st.download_button(
            label="Download Pose JSON",
            file_name="pose_001.json",
            mime="application/json",
            data=json_string,
        )
        st.json(json_string)
