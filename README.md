# TechChallenge #01: GPT Wrapper

**Workflow:**
- Training model -> Pretrained model
- Import model to API -> API
- UI query API

## Step 1: Training model
In this step, we use 2 environnents depend on situations:

### Solution 1: Training model in colab and save to drive
- Our colab file at https://drive.google.com/file/d/10Yfi-Osm9RsnnwoFmmvQII5ufyOuRuMK/view?usp=sharing

Add path to dataset and convert to txt file
![image](https://user-images.githubusercontent.com/90249100/168620892-53818ef7-8787-4814-84f9-12d995c92447.png)

Add path to dataset txt and output to somewhere in drive
![image](https://user-images.githubusercontent.com/90249100/168622040-2619417c-cb25-44ea-9cec-b91cd47c26cc.png)

Finally, download model after saving & import to API

### Solution 2: Training model in job-runner GPU & save to Owncloud in KMS server 
- In colab, it just keep the state about 12 hours so that we are not able to train model exceed this duration -> Use job-runner

Job-runner will run our container environment through Dockerfile, therfore, we have to dockerize everything needed to train model. Then, we save model into Owncloud server.

```
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel

RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list

RUN apt-get update
RUN apt-get install -y git

RUN git clone https://github.com/tamnpham/KMS_TechChallenge_01.git
WORKDIR "./KMS_TechChallenge_01"

RUN pip install -r requirements.txt --force
RUN chmod +x run.sh

CMD ["sh","run.sh"]
```
- run.sh
```
python load_model.py
python dataset.py -i './data/sample_data.json' -o './data/sample_data.txt'
python trainer.py -i './data/sample_data.txt' -m '125M' -e 3 -o 'baseline' -c True
```
Then build image & push to dockerhub (public)
```
docker build tamnpham/tc-gpt-core .
docker push tamnpham/tc-gpt-core
```
Access to job-runner server, fill image name to create a job
![image](https://user-images.githubusercontent.com/90249100/168628783-5c268dab-d75e-41a2-ad6f-5f78996581ce.png)

![image](https://user-images.githubusercontent.com/90249100/168648512-39b95779-c84a-47d6-9f81-f9772e590022.png)

Check Owncloud
![image](https://user-images.githubusercontent.com/90249100/168648874-6dd94a01-8f95-41dd-9906-ea962736e83e.png)

