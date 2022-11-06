import json
import uuid

import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import inference


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/{style}")
def get_image(style: str, file: UploadFile = File(...)):
    print(file)
    img = np.array(Image.open(file.file))

    pose_keypoints, cv_output = inference.inference_on_single_image(img)
    print(pose_keypoints.shape)

    uid = str(uuid.uuid4())
    img_name = f"/storage/{uid}.png"
    pose_name = f"/storage/{uid}.json"

    # Write image file
    cv2.imwrite(img_name, cv2.cvtColor(cv_output, cv2.COLOR_RGB2BGR))

    # Write JSON file
    with open(pose_name, 'w') as f:
        json.dump({
            'poses': pose_keypoints
        }, f, cls=NumpyEncoder)

    return {
        "img_name": img_name,
        "pose_name": pose_name
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
