import streamlit as st
# 產生 download_button 按鈕，按下後自動下載（生成）一個二進制文件 (命名為 streamlit_download.bin)
binary_contents = b'a bin file , hehe  da \n I\'m a new line' ## bytes 類型
# Defaults to 'application/octet-stream'
st.download_button('下載為 bin 文件',  binary_contents )
 
 
#建立 上傳 按鈕，按下後可以上傳二進制文件
uploaded_file = st.file_uploader("请选择一个二进制文件：")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue() ## bytes_data 就是 binary_contents
    st.write(bytes_data)

#建立 上傳 按鈕，按下後可以上傳文本文件
uploaded_file2 = st.file_uploader("请选择一个文本文件：")
if uploaded_file2 is not None:
    # To read file as string:
    string_data = uploaded_file2.read().decode("utf-8")
    st.write(string_data)

"""
參考來源：
https://blog.csdn.net/heianduck/article/details/122825922
"""