# Import Library
import streamlit as st 
import numpy as np
from PIL import Image
import cv2

# Title
st.title('Pencil sketch')

# Cache
@st.cache

# Function for determining 'Dodge'
def DodgeV2(x,y):
  return cv2.divide(x, 255-y, scale=256)

# Function for processing images
def pencilskecth(inp_img):
  img_gray = cv2.cvtColor(inp_img,cv2.COLOR_BGR2GRAY)
  img_invert = cv2.bitwise_not(img_gray)
  img_smoothing = cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
  final_img = DodgeV2(img_gray,img_smoothing)
  return final_img
st.set_option('deprecation.showfileUploaderEncoding', False)

# Upload File and Create Output
file_image = st.file_uploader("", type=["jpg","jpeg","png"])

if file_image is None:
  st.warning('Please upload Image or Photo that you will use first!')
else:
  input_img = Image.open(file_image)
  final_sketch = pencilskecth(np.array(input_img))
  st.success('It worked!!!')
  st.image(final_sketch, use_column_width=True)
