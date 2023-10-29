import streamlit as st
from PIL import Image
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import load_image
from streamlit_image_select import image_select
import time
import io


pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-refiner-1.0")

def main():
    st.title("Welcome to SurgiLook.ai!")
    st.write("With this tool, you can easily visualize the results of a surgical procedure before it happens")
    
    # Add an image input field
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
     # Add padding
    st.write("")
    st.write("")

    # Add padding
    st.write("")
    st.write("")
    
    # Add a section to select an image

    img = image_select(
    label="Or use a Demo Image insted",
    images=[
        
        Image.open("chin.jpg"),
        Image.open("facelift.jpg"),
        Image.open("nose.jpg"),
        
    ],
    use_container_width=False,
    captions=["chin implant", "face lift", "nose adjustment", ],
    return_value="index"
)
    
    # Add padding
    st.write("")
    st.write("")

    # Add a section with multiple options
    st.header("Select an option:")
    option = st.selectbox("", ("Face Lift", "Nose correction", "Chin implant"))
    st.write("You selected:", option)
    
    # Add padding
    st.write("")
    st.write("")
    
    # Add a horizontal bar with images for each option
    strg=""
    if option == "Face Lift":
        strg="Face Lift"
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("fl1.jpg")
        with col2:
            st.image("fl2.jpg")
        with col3:
            st.image("fl3.jpg")
    elif option == "Nose correction":
        strg="Nose correction"
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("nose1.jpg")
        with col2:
            st.image("nose3.jpg")
        with col3:
            st.image("nose4.jpg")
    elif option == "Chin implant":
        strg="Chin implant"
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("chin1.jpg")
        with col2:
            st.image("chin2.jpg")
        with col3:
            st.image("chin3.jpg")
    

    # Add padding
    st.write("")
    st.write("")
    # Add a text input field
    text_input = st.text_input("Enter some text...")
    
    # Add a generate button
    if st.button("Generate"):
        # Check if an image was uploaded
        if uploaded_file is not None:
            image_bytes = uploaded_file.read()
            pil_image = Image.open(io.BytesIO(image_bytes))
            init_image = load_image(pil_image).convert("RGB")
            prompt = f"generate image of how this person would look after {strg} also use this additional information{text_input}"
            image = pipeline(prompt, image=init_image).images
            st.image(image, caption="Uploaded Image", use_column_width=True)
        else:
            time.sleep(4)
            if img==0:
                st.image('chinop.jpg',width=300)
            elif img==1:
                st.image('faceliftop.jpg',width=300)
            elif img==2:
               st.image('noseop.jpg',width=300)
            
        # Add padding
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    # Add a section with instructions and images
    col1, col2 = st.columns(2)
    with col1:
        st.header("How to use this website")
        st.write("Here are some steps to get you started:")
        st.write("1. Upload an image using the image input field above.")
        st.write("2. select the type of cosmetic sugery you want to perform.")
        st.write("3. Add some text to describe any specific details")
        st.write("4. Click the generate button to generate output.")    
    with col2:
        st.image("step1.jpeg")

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)
    with col2:
        st.header("Transforming the cosmatic surgeriy experiance")
        st.write("Our SugiLook AI model generates realistic before and after images of cosmetic surgery.")
        st.write("Generate Precise image by providing detailed feedback")
        st.write("Feel more confident on your decision")
        st.write("Assist doctors in communicating the potential results of the procedure.")

    with col1:
        st.image("step2.jpeg")
    # Set up the footer container

    # Add a footer
    st.write("")
    st.write("")
    st.write("")   
    st.write("")
    st.write("")
    st.write("")   
    st.write("")
    st.write("")
    st.write("")   
    st.write("")
    st.write("")
    st.write("")
       
    
   

    footer_container = st.container()
    with footer_container:
            st.write("Terms of Use | Privacy Policy | Contact Us")
            st.write("Language: English | Spanish | French | German")
    




    
if __name__ == "__main__":
    main()