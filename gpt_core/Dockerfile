FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel

RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list

RUN apt-get update
RUN apt-get install -y git

RUN git clone https://github.com/tamnpham/KMS_TechChallenge_01.git
WORKDIR "./KMS_TechChallenge_01/gpt_core"

RUN pip install -r requirements.txt --force

RUN python load_model.py
RUN chmod +x entrypoint.sh

CMD ["sh","entrypoint.sh"]