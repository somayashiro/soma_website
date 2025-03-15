import os
import streamlit as st
from streamlit_image_select import image_select
st.set_page_config(page_title="Soma's Website",page_icon="🎮⚽")


image_dir="images"

images=["image-1.jpg","image-2.jpg","image-3.jpg"]
# Full paths for images
image_paths = [os.path.join(image_dir, img) for img in images]

# Check if images exist before passing to image_select
existing_images = [img for img in image_paths if os.path.exists(img)]

if existing_images:
    selected_image = image_select("Slideshow", existing_images)

    # Display selected image
    if selected_image:
        st.image(selected_image, caption="Selected Image", use_container_width=True)
else:
    st.error("No images found in the specified directory.")

st.header("About me")
col1,col2=st.columns([1,2])
with col1:
    st.image(os.path.join(image_dir, "image-4.jpg"), width=300) 
with col2:
    st.write("I am almost 10. I am from Japan and I live in Malaysia. My family has me, mom, dad and my sister.")


st.header("My hobbies")
col3,col4=st.columns([1,1])
with col3:
    st.image(os.path.join(image_dir, "image-5.jpg"), width=300) 
with col4:
    st.image(os.path.join(image_dir, "image-6.png"), width=300) 
st.write("My hobbies are to play Roblox with my friends and to play football as a goalkeeper and shooting. My favourite board game is UNO and Monopoly and chess. LEGO is my favourite toy out of all.")
st.header("My dreams")
col5,col6=st.columns([1,1])
with col5:
    st.write("I want to be forever happy and have a nice life. I also want to be very rich and healthy.")
with col6:
    st.image(os.path.join(image_dir, "image-7.jpg"), width=300) 


st.header("My YouTube videos")
st.write("My YouTube link 👉#https://www.youtube.com/@topgoat_fc ")
yt_videos = ["https://www.youtube.com/embed/mvuKt3HsxOg" , "https://www.youtube.com/embed/rPpFlz8GYtQ"]
cols=st.columns(len(yt_videos))
for i,url in enumerate(yt_videos):
    with cols [i]:
        st.video(url)
st.header("Contact me")


st.write("My Discord Username 👉w_soma777")
st.write ("Thanks for visiting my first website. Take care and have a good day!🥳🥳🥳")

