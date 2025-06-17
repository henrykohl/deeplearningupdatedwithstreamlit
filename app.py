import os
import torch
# torch.classes.__path__ = []  # Neutralizes the path inspection ## 可行方式一
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)]  ## 可行方式二

import streamlit as st

from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path




# this is for saving images and prediction
def save_image(uploaded_file):
    if uploaded_file is not None:
        save_path = os.path.join("images", "input.jpeg") # 設定圖檔存放路徑與建立圖檔名稱
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())                # 將上傳圖檔儲存
        st.success(f"Image saved to {save_path}")        # 於 web 顯示 圖檔存放路徑

        model = torch.load(Path('model/model.pt'), weights_only=False) # load 模型
        ## weights_only=True，會產生 "UnpicklingError: Weights only load failed." 錯誤


        trans = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            ])

        image = Image.open(Path('images/input.jpeg')) # image 類型 PIL.JpegImagePlugin.JpegImageFile

        input = trans(image) # input 類型 torch.Tensor, 大小 [1, 224, 224]

        input = input.view(1, 1, 224, 224).repeat(1, 3, 1, 1) # input 大小 [1, 3, 224, 224]

        output = model(input) # tensor 類型，大小 (1,2)

        ## 警告 DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated
        # prediction = int(torch.max(output.data, 1)[1].numpy()) 

        prediction = torch.max(output.data, 1)[1].item() # prediction 是純量值

        if (prediction == 0):
            print ('Normal')
            st.text_area(label="Prediction:", value="Normal", height=100)
        if (prediction == 1):
            print ('PNEUMONIA')
            st.text_area(label="Prediction:", value="PNEUMONIA", height=100)






if __name__ == "__main__":
    st.title("Xray lung classifier") # 設定 streamlit web 頁 title
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"]) # 建立上傳按鈕功能
    ## 沒按下鈕前， uploaded_file 是 <class 'NoneType'>
    ## 按下按扭後， uploaded_file 是 <class 'streamlit.runtime.uploaded_file_manager.UploadedFile'>
    save_image(uploaded_file)


    


