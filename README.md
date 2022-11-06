# Overview

This repo contains simple code for deploying [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) pose 
detection as a lightweight web app that can be accessed via a simple front-end image upload or programmatic requests 
sent via REST API.

**Note on hardware**: The docker images are built with the expectation of a CUDA enabled GPU being present on the host.
Code was developed on a machine with an NVIDIA RTX 2080ti. The code might still work with CPU only, but I have
not tested this.

# Quickstart

## Option #1: Using Frontend UI

From the project root dir, run:

```bash
# Note: Depending on your Docker Compose version, you may need to run 'docker-compose' instead of 'docker compose'
docker compose up   # Add the -d flag if you want to run in detached mode
```

**Alternatively**, if you want to make modifications and build the images from the local dockerfiles, use:
```bash
# Note: Depending on your Docker Compose version, you may need to run 'docker-compose' instead of 'docker compose'
docker compose -f docker-compose.build.yaml up --build   # Add the -d flag if you want to run in detached mode
```

You should now be able to visit [http://localhost:8501/](http://localhost:8501/) in your browser. Use the file upload
button to upload an example image of your choosing, and click "Run Inference". You can use the download button to 
download the results image and/or pose data JSON file. The ```./storage``` directory is also mounted inside the
container, so results are available there as well.

![Alt text](/examples/frontend_ui.png?raw=true "Frontend UI Screenshot")

To stop the running containers:

```bash
docker compose down
```

## Option #2: Post requests to REST API

See the ```demo.ipynb``` file for an example.
