FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel

RUN apt-get update
RUN apt-get install -y git

RUN git clone https://github.com/tamnpham/KMS_TechChallenge_01.git
WORKDIR "./KMS_TechChallenge_01"

RUN pip install -r requirements.txt --force
RUN chmod +x run.sh
CMD ["sh","run.sh"]