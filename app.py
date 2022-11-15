import streamlit as st

from keypointDetection import *
def forImage(x):
    detector = Detector(model_type=x)
    image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
    if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        st.write(file_details)
        img = Image.open(image_file)
        st.image(img, caption='Uploaded Image.')
        with open(image_file.name,mode = "wb") as f: 
            f.write(image_file.getbuffer())         
        st.success("Saved File")
        detector.onImage(image_file.name)
        img_ = Image.open("result.jpg")
        st.image(img_, caption='Proccesed Image.')

def forVideo(x):
    detector = Detector(model_type=x)
    uploaded_video = st.file_uploader("Upload Video", type = ['mp4','mpeg','mov'])
    if uploaded_video != None:
        
        vid = uploaded_video.name
        with open(vid, mode='wb') as f:
            f.write(uploaded_video.read()) # save video to disk
    
        st_video = open(vid,'rb')
        video_bytes = st_video.read()
        st.video(video_bytes)
        st.write("Uploaded Video")
        detector.onVideo(vid)
        st_video = open('output.mp4','rb')
        video_bytes = st_video.read()
        st.video(video_bytes)
        st.write("Detected Video") 



def main():
   


    option = st.selectbox(
     'Files to work with',
     ('Images', 'Videos'))

    
    if option == "Images":
        st.title('Keypoint Detection for Images')
        st.subheader("""
    For image
    """)
        forImage('keypointsDetection')
    else:
        st.title('Keypoint Detection for Videos')
        st.subheader("""
    For video
    """)
        forVideo('keypointsDetection')

if __name__ == '__main__':
		main()