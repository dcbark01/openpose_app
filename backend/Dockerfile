FROM cwaffles/openpose:latest

RUN cd /openpose/models && \
    bash getModels.sh

WORKDIR /openpose/build/python/openpose
RUN make install && \
    cp ./pyopenpose.cpython-36m-x86_64-linux-gnu.so /usr/local/lib/python3.6/dist-packages && \
    cd /usr/local/lib/python3.6/dist-packages && \
    ln -s pyopenpose.cpython-36m-x86_64-linux-gnu.so pyopenpose
ENV LD_LIBRARY_PATH=/usr/local/python


WORKDIR /openpose


# Setup the app inference server
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install setuptools && \
    pip3 install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY ./src ./

EXPOSE 8081

CMD ["python3", "main.py"]
