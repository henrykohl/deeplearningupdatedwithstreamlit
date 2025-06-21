# Xray lung classifier

Data link: https://drive.google.com/file/d/1pfIAlurfeqFTbirUZ5v_vapIoGPgRiXY/view?usp=sharing


## Workflows

- constants
- config_enity
- artifact_enity
- components
- pipeline
- main


## pipeline is completed

## Lecture Note (Lecture 6)

* Lecture Video -- [Evaluate and Deploy Deep Learning Models to the Cloud](https://www.youtube.com/watch?v=jk_YAsI9z5w)

* 用 Streamlit 取代 BentoML (1:47:30)

> - Lecture Github Repository -- [Xray-lung-classifier](https://github.com/sunnysavita10/Xray-lung-classifier)
>
> 1. 檢視 `/xray/components/model_pusher.py`
>
> > * 訓練後模型的路徑 `/model/model.pt`
> 
> > * just upload MODEL file to s3
>
> 2. 檢視 `/app.py`
>
> 3. 檢視 `/xray/cloud_storage/s3_ops.py`
> > * 使用 boto3 來連接 s3
>
> 4. 建立 virtual environment: `conda create -p venv python=3.8 -y` (1:56:45)
>
> 5. 執行 `source activate ./venv` (1:57:40)
> > * 執行 `pip list`
>
> 6. 執行 `pip install -r requirments.txt` (1:58:00)
>
> 7. 執行 `streamlit run app.py`，後開啟 web APP (2:00:50)
>
> 8. google 一張 'pneumonia lungs x ray' 的 jpeg 圖，將其下載，
>
> 9. 將 jpeg 檔上傳至 web APP -- 檔案將存到 `/images/input.jpeg`

## Lecture 7 -- [Deployment with CI-CD pipeline - part1](https://www.youtube.com/watch?v=Tm49jrcKRyI)

* 根據 [Github: Xray lung classifier](https://github.com/henrykohl/deeplearningupdatedwithstreamlit)

* 開啟 terminal，使用 Git bash
  > ```bash
  > source activate base
  > source activate ./venv
  > ```

* 建立 `Dockerfile` 檔案
  > 更多細節，參見 [MLOps Foundations.](https://www.youtube.com/playlist?list=PLmQAMKHKeLZ9iaLWBULDE_hiPtOiHiDz0)

* 建立 `.dockerignore`

* 建立 `.github/workflows/main.yml`

* Docker workflow (17:20)
  > 1. Source code
  > 
  > 2. Build docker image
  > 
  > 3. Push to the Docker hub
  > 
  > 4. Create AWS EC2 instance
  > 
  > 5. Create the IAM USER (have access to the EC2)
  > 
  > 6. Launch docker to the Ec2

  > workflow(yaml)
  >
  > > CI/CD (1: continuous integration/continuous delivery)/CD (2: continuous deployment)
  > 
  > > > 1: github action -- provide you the server 
  > > >
  > > > 2: EC2(self-hosted runner) 此 project 的 continuous deployment 不使用 github action server

* 完成 `Dockerfile` (26:10)

* 完成 `.dockerignore` (33:25) 

* 完成 `.github/workflows/main.yml` (34:45) 

* 介紹 Github action

* Github commit (1:11:00)
  > ```bash
  > git remote -v
  > git add .
  > git commit -m "dockerfile and workflow updated"
  > git push origin main
  > ```

* login Docker Hub

* login AWS
 > EC2 -- launch instance 
 > > Name: `CNNApp`
 > > 
 > > AMI: select a free tier eligible
 > > 
 > > instance type: `t2.medium`
 > > 
 > > Key pair: create new key pair
 > > > key pair name: `CNNaplication`
 > > > 
 > > > key pair type: `RSA`
 > > > 
 > > > private key file format: `.pem`
 > >
 > > Firewall: create security group
 > > 
 > > Configure storage: `16` GiB `gp2` Root volume
 >
 > Done! Then, click `connect`
 >
 > IAM -- Users: click `create user` (username: `deployment`) -- Permissions summary: `AdministratorAccess`
 > > Done! Then, click `create access key` -- `Comand Line Interface (CLI)`
 > > 
 > > `Download .csv`

* Github -- setting -- Secrets and variables -- Secrets (Tab) -- click `New repository secret`
 > * DOCKER_USERNAME
 >
 > * DOCKER_PASSWORD
 >
 > * AWS_REGION: `us-east-1`
 >
 > * REGISTRY: 自己 Docker 的 username
 >
 > * IMAGE_NAME: `cnnapp`
 >
 > * AWS_ACCESS_KEY_ID
 >
 > * AWS_SECRET_ACCESS_KEY

* 打開 [Actions -- Runners 設定頁面](https://github.com/henrykohl/deeplearningupdatedwithstreamlit/settings/actions/runners/new) 同時連線 AWS ec2 (connect) 打開 CLI

* Install Docker on AWS ec2 Linux machine
 > ```bash
 > sudo apt-get update -y
 > sudo apt-get upgrade
 > curl -fsSL https://get.docker.com -o get-docker.sh
 > sudo sh get-docker.sh
 > docker # test
 > docker --help # test
 > docker images # 檢查是否有 images (但此時顯示 permission denied)
 > 
 > sudo usermod -aG docker ubuntu
 > newgrp docker
 > docker images # 此時應該是空的
 > docker ps -a  # 此時應該是空的 (the container is nor running)
 > ```

* 繼續 (1:52:40 ) -- 根據 [Github runners](https://github.com/henrykohl/deeplearningupdatedwithstreamlit/settings/actions/runners/new) with Linux system
 > ```bash
 > curl -o actions-runner-linux-x64-2.313.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.313.0/actions-runner-linux-x64_2.313.0.tar.gz
 > echo "5020da7139d85c776059f351e0de8fdec753affc9c558e892472d43ebeb518f4  actions-runner-linux-x64-2.325.0.tar.gz" | shasum -a 256 -c
 > tar xzf ./actions-runner-linux-x64-2.325.0.tar.gz
 > ./config.sh --url https://github.com/henrykohl/deeplearningupdatedwithstreamlit --token AKJGI45JLAC4GYXWGFL45C3IKRIQC
 >
 > # 連續四個設定都用 default setting即可 (按下 Enter)
 > ./run.sh
 > ```

* AWS EC2 instance -- Security group -- inbound rules -- Edit inbound rules
 >  Select `custom TCP`, port `8501`, source `0.0.0.0/0`
 >
 > click `Add rule`

* (1:59:50)
 > ```bash
 > git add . 
 > git commit -m "changes done"
 > git push origin main
 > ```


## Lecture 8 -- [Deployment with CICD Part -2](https://www.youtube.com/watch?v=TmSGVD2QBKA)

### workflow recap (17:00)

1. Source code -- in GitHub

2. Dockerfile

3. Docker image

4. Docker hub

5. EC2 -> AWS

6. Installing Docker and running

* GitHub
  > providing me a service -- [Github-Action] -- providing me a Server -- [Win/Linux/Mac]




* Workflow
  > for automating each and everything, writing a workflow file - `main.yaml` (.githib/workflow/main.yaml)
  >
  > By using the workflow/main.yaml, achieving CI / CD / CD'
  > > CI: integrate the source code and keep/push the source code to the GitHub
  > > 
  > > CD: push the image to the Docker Hub

* Summary of workflow architecture
  > local sys(source code) --1--> 
  > github(github-Action) 例如 Linux server --2--> 
  > Docker Hub(Registry) --3--> 
  > AWS-EC2(Cloud-Server)
      
  > 1: CI & test \
  > 2: CD \
  > 3: CD' (self-hosted)


## Tech Issue

* Error : RuntimeError: Tried to instantiate class ‘__path__._path’, but it does not exist! Ensure that it is registered via torch::class_

* Reference Solution 1: [Fixing the “RuntimeError: Tried to instantiate class ‘__path__._path’...](https://medium.com/@subash_68978/1b4d1d99509d)

* Reference Solution 2: [Trying to import torch results in asyncio RuntimeError](https://github.com/streamlit/streamlit/issues/10992)
> 執行 `streamlit run myapp.py --server.fileWatcherType none` (實測可行)