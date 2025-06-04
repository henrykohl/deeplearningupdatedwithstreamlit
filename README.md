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

## Lecture Note 

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
> 4. 建立 virtual environment: `conda create -p venv python=3.8 -y`
>
> 5. 執行 `source activate ./venv`
>
> 6. 執行 `pip install -r requirments.txt`
>
> 7. 執行 `streamlit run app.py`，後開啟 web APP (2:00:50)
>
> 8. google 一張 'pneumonia lungs x ray' 的 jpeg 圖，將其下載，
>
> 9. 將 jpeg 檔上傳至 web APP -- 檔案將存到 `/images/input.jpeg`