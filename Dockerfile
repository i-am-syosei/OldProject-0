FROM python:3.10
FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
RUN apt update && \
  apt install -y software-properties-common git curl 
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install diffusers --upgrade transformers accelerate scipy safetensors
RUN pip install Flask
RUN pip install Redis
RUN pip install mysql-connector-python
RUN pip install flask-socketio
