import streamlit as st
import cv2

st.write("""
#Create Pencil Sketch of an Image""")

#Get Input of image
st.header('Input any image')

st.file_uploader(label='upload image', type=['png', 'jpg'], accept_multiple_files=True, label_visibility="visible")

# Read the image and convert it into an array
img = cv2.imread("original_image.jpg")

# Filters
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # Gray
invert_image = cv2.bitwise_not(grey_img)                    # Invert gray
blur = cv2.GaussianBlur(invert_image, (23,33), 0)           # Gaussian Blur GaussianBlur(source, kernel size, standard dev wrt X)
invert_blur = cv2.bitwise_not(blur)                         # Invert blur
pencil = cv2.divide(grey_img, invert_blur, scale = 256.0)   # Blend gray with invert blur



st.write("Pencil Sketch of the image:", pencil)

# Display the final output
plt.figure(figsize = (15,8))
plt.subplot(1, 2, 1)
plt.title("Original Image", color = 'r', fontsize = 15)
plt.imshow(img)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title("Pencil Sketch of the Original Image", color = 'k', fontsize = 15)
plt.imshow(pencil, cmap = 'gray')
plt.axis('off')
plt.show()