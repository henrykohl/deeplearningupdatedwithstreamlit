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

### 用 Streamlit 取代 BentoML (1:47:30)

- Lecture Github Repository -- [Xray-lung-classifier](https://github.com/sunnysavita10/Xray-lung-classifier)

1. 檢視 `/xray/components/model_pusher.py`

   > * 訓練後模型的路徑 `/model/model.pt`
 
   > * just upload MODEL file to s3

2. 檢視 `/app.py`

3. 檢視 `/xray/cloud_storage/s3_ops.py`

   > * 使用 boto3 來連接 s3

4. 建立 virtual environment: `conda create -p venv python=3.8 -y` (1:56:45)

5. 執行 `source activate ./venv` (1:57:40)

   > * 執行 `pip list`

6. 執行 `pip install -r requirments.txt` (1:58:00)

7. 執行 `streamlit run app.py`，後開啟 web APP (2:00:50)

8. google 一張 'pneumonia lungs x ray' 的 jpeg 圖，將其下載，

9. 將 jpeg 檔上傳至 web APP -- 檔案將存到 `/images/input.jpeg`

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
  > > whenever pushing the code from the local to GitHub 
so automatically this workflow will be triggered and this pipeline will be executed
  >
  > By using the workflow/main.yaml, achieving CI / CD / CD'
  > > CI: integrate the source code and keep/push the source code to the GitHub
  > > 
  > > CD: push the image to the Docker Hub

* Summary of workflow architecture
  > local sys(source code) --1--> 
  > github(github-Action, doing CI&CD) 例如 Linux server --2--> 
  > Docker Hub(Registry) --3--> 
  > AWS-EC2(Cloud-Server, doing CD')
      
  > 1: CI & test \
  > 2: CD (push to Docker Hub)\
  > 3: CD' (pull from Docker Hub), self-hosted service

### Review the code (28:50)

* explain `.github/workflows/main.yml`

* (35:37)
  > The 1st thing is source code. \
  > The 2nd thins is Docker file inside your system. \
  > The 3rd one is the configuration yaml file. \
  > The 4th thing requires the particular credential 

* You should have a Docker Hub account.

* You should have to create the ec2 instance on the AWS

* Add the secret inside the GitHub action

### (41:55)

* open Git Bash terminal
  > ```bash
  > source activate base
  > source activate ./venv # 假設 已經建立了 venv 虛擬環境
  > ```

  > ```bash 
  > # 由於 main.yaml 中 comment更新
  > git add .
  > git commit -m "code updated please check"
  > git push origin main
  > ```

* (56:10) GitHub Action Runners 處於 `offline` 狀態，於是在 AWS ec2 instance 下 (若沒有連線，則需要 connect) terminal 執行 `./actions-runner/.run.sh` ， GitHub Action Runners 狀態改為 `Active`，最後成為 `Idle`。
  > 此時 GitHub Actions 中 Continuous-Deployment 中出現錯誤，而 AWS ec2 instance 的 terminal 也顯示 `Job Continuous-Deployment completed with result: Failed`！因此把 GitHub setting/secrets and variables/Actions 中的 IMAGE_NAME 的 value 改成 `mycnnimage` 
  >
  > 此時為了要再次 commit GitHub code，所以將 `app.py` 中的 comment 稍微更新一下，之後執行：
  > ```bash
  > git add .
  > git commit -m "code updated"
  > git push origin main
  > ```

* (1:06:10) Push Docker image to Docker Hub (GitHub Actions) 完成: 可以(在Docker Hub)看到 image 已經 Docker Hub 上被成功建立

* (1:08:25) Continuout-Deployment (GitHub Actions) 出現錯誤

* (1:12:50) 在 AWS ec2 instance 的 terminal 執行 `docker ps -a`，複製 CONTAINER ID，再次執行 `docker stop {剛剛複製的CONTAINER ID}`，(1:13:49) 接著執行 `docker ps -a` 或 `docker ps`，可以看到沒有 container 被執行。(1:15:02) 在 `/actions-runner`中執行 `./run.sh`

* (1:15:29) 在 GitHub/Actions 中點選剛剛出錯的 workflow run，點選 `Re-run failed jobs`。(1:16:20) 還是出現相同錯誤錯

* (1:17:08) 在 AWS ec2 instance 的 terminal 執行 `docker ps -a`，複製 CONTAINER ID，再次執行 `docker rm {剛剛複製的CONTAINER ID}`，接著執行 `docker ps -a`，可以看到有 container 被移除。

* (1:18:51) 在 GitHub/Actions 中點選剛剛出錯的 workflow run，點選 `Re-run failed jobs`。這次問題解決了！

* (1:19:47) 複製 AWS ec2 instance 的 public ip，再加上 `:8501` ，輸入到瀏覽器位置欄後開啟，即可 demo 圖形辨識功能！

* (1:22:10) 注意 AWS ec2 instance 中的 Security，進入 Security groups，在 inbound rules 中打開 Edit inbound rules，需要設定 Type 為 `Custom TCP` 且 Port 為 `8501` (by default, this Streamlit is running on `8501`. We expose in our Docker image & mention the expose instruction. So, we have to map it over here.) 

---

### Quick Overview (1:28:23) 

how we can test our application at the time of integration. It's development level testing (1:26:35)

* 在 deeplearningupdatedwithstreamlit github repository 中新增 /.github/workflows/notebook/experiments.ipynb

* 執行 `pip install pytest` (VS Code terminal)

* GOOGLE 查一下 **pytest** 與 **unittest**

* 建立/完成 `test.py` 檔案(1:37:18)。執行 `pytest test.py` (1:38:49)

* (1:43:25) 建立 test 資料夾，在 test 下建立 integrationtest 資料夾 與 unitest 資料夾，在 integrationtest 下建立 integration.py，在 unitest 下建立 unit.py


## Tech Issue

* Error : RuntimeError: Tried to instantiate class ‘__path__._path’, but it does not exist! Ensure that it is registered via torch::class_

* Reference Solution 1: [Fixing the “RuntimeError: Tried to instantiate class ‘__path__._path’...](https://medium.com/@subash_68978/1b4d1d99509d)

* Reference Solution 2: [Trying to import torch results in asyncio RuntimeError](https://github.com/streamlit/streamlit/issues/10992)
  > 執行 `streamlit run myapp.py --server.fileWatcherType none` (實測可行)