import os

import pyopenpose as op


OPENPOSE_BIN = os.environ.get('OPENPOSE_BIN', '/openpose/build/examples/openpose/openpose.bin')
OPENPOSE_MODELS_DIR = os.environ.get('OPENPOSE_MODELS_DIR', '/openpose/models')


def inference_on_single_image(img):
    """ Perform OpenPose inference on a single input image (should be numpy RGB array). """

    # Starting OpenPose
    params = dict()
    params["model_folder"] = OPENPOSE_MODELS_DIR
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    # Process Image
    datum = op.Datum()
    datum.cvInputData = img
    opWrapper.emplaceAndPop([datum])

    return datum.poseKeypoints, datum.cvOutputData
