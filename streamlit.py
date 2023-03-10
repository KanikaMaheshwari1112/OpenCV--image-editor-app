# Import Library
import streamlit as st 
import numpy as np
from PIL import Image
import cv2
from io import BytesIO

# Title
st.title('CONVERT AN IMAGE TO A SKETCH')

# Cache
@st.cache

# function to load an image
def load_an_image(image):
    img = Image.open(image)
    return img

  # Function for determining 'Dodge'
def DodgeV2(x,y):
  return cv2.divide(x, 255-y, scale=256)

#Function for water color sketch
def convertto_watercolorsketch(inp_img):
    img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8)
    img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5)
    return(img_water_color)
  
# Function for pencil sketch
def pencilsketch(inp_img):
  img_gray = cv2.cvtColor(inp_img,cv2.COLOR_BGR2GRAY)
  img_invert = cv2.bitwise_not(img_gray)
  img_smoothing = cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
  final_img = DodgeV2(img_gray,img_smoothing)
  return final_img

#Function for Gray image
def grayimage(inp_img):
  img_gray= cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
  return img_gray

#Function for Blur effect
def blurimage(inp_img):
  blur_img = cv2.cvtColor(inp_img, cv2.COLOR_RGB2BGR)
  blur_image = cv2.GaussianBlur(blur_img,(21,21), 0, 0)
  return blur_image
  
st.sidebar.markdown("**:blue[An Image Editor App]**")
with st.sidebar.expander("About the App"):
     st.write("""
        Use this simple application to convert your favorite photos to a watercolor sketch, a pencil sketch, a black and white image or an image with blurring effect.  \n Hope you enjoy!
     """)


st.set_option('deprecation.showfileUploaderEncoding', False)

# Upload File and Create Output
file_image = st.file_uploader("Upload the Photo", type=["jpg","jpeg","png"])
if file_image is not None:
    input_img = Image.open(file_image)


    st.write('Please select an option from below.')
    filter = st.radio('Covert your photo to:', ['Water Color','Black and White', 'Pencil Sketch', 'Blur Effect']) 
  
    if filter== 'Water Color':
        final_sketch= convertto_watercolorsketch(np.array(input_img))
        im_pil = Image.fromarray(final_sketch)
        st.success('Your Water Color Sketch is ready. You can download it now.')
        buf = BytesIO()
        img = im_pil
        img.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        st.download_button(
                    label="Download sketch",
                    data=byte_im,
                    file_name="watercolorsketch.png",
                    mime="image/png"
                )
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(input_img, width=250)
  
        with col2:
            st.header("Water Color Sketch")
            st.image(im_pil, width=250)
       
    elif filter== 'Black and White':
        final_sketch= grayimage(np.array(input_img))
        im_pil = Image.fromarray(final_sketch)
        st.success('Your Black and White Sketch is ready. You can download it now.')
        buf = BytesIO()
        img = im_pil
        img.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        st.download_button(
                    label="Download sketch",
                    data=byte_im,
                    file_name="blackandwhitesketch.png",
                    mime="image/png"
                )
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(input_img, width=250)
  
        with col2:
            st.header("Black and White Sketch")
            st.image(im_pil, width=250)
      
    elif filter== 'Pencil Sketch':
        final_sketch= pencilsketch(np.array(input_img))
        im_pil = Image.fromarray(final_sketch)
        st.success('Your Pencil Sketch is ready. You can download it now.')
        buf = BytesIO()
        img = im_pil
        img.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        st.download_button(
                    label="Download sketch",
                    data=byte_im,
                    file_name="blackandwhitesketch.png",
                    mime="image/png"
                )
     
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(input_img, width=250)
  
        with col2:
            st.header("Pencil Sketch")
            st.image(im_pil, width=250)
       
    elif filter== 'Blur Effect':
        final_sketch= blurimage(np.array(input_img))
        im_pil = Image.fromarray(final_sketch)
        st.success('Your Blur Image is ready. You can download it now.')
        buf = BytesIO()
        img = im_pil
        img.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        st.download_button(
                    label="Download sketch",
                    data=byte_im,
                    file_name="blurimage.png",
                    mime="image/png"
                )  
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(input_img, width=250)
  
        with col2:
            st.header("Blur Effect Image")
            st.image(im_pil, width=250)
       
  
    
  
  
  
   

