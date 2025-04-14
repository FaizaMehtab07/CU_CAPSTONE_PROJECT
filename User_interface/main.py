import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from components import top_bar
from components import recording_area
from components import live_transcription_panel
from components import bottom_bar
from components.result_screen_components import speech_fluency
from components.result_screen_components import body_posture
from components.result_screen_components import emotional_tone
# Load the facial emotion detection model and face cascade
try:
    emotion_model = load_model('models/emotion_model.h5')  # Adjust path if needed
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
except Exception as e:
    st.error(f"Error loading model or face cascade: {e}")
    emotion_model = None
    face_cascade = None

class EmotionDetector(VideoTransformerBase):
    def __init__(self):
        self.detected_emotions = []

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        frame_emotions = []
        for (x, y, w, h) in faces:
            face_roi = gray[y:y + h, x:x + w]
            resized_face = cv2.resize(face_roi, (48, 48))  # Adjust if your model expects a different size
            normalized_face = resized_face / 255.0
            reshaped_face = np.expand_dims(normalized_face, axis=[0, -1])  # Adjust based on your model's input shape
            if emotion_model is not None:
                emotion_prediction = emotion_model.predict(reshaped_face)
                emotion_label = self.get_emotion_label(np.argmax(emotion_prediction))
                frame_emotions.append(emotion_label)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around face
                cv2.putText(img, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) # Display emotion

        self.detected_emotions.extend(frame_emotions)
        return img

    def get_emotion_label(self, label):
        emotion_map = {0: 'anger', 1: 'disgust', 2: 'fear', 3: 'happiness', 4: 'sadness', 5: 'surprise', 6: 'neutral'}
        return emotion_map.get(label, 'unknown')

def main():
    if 'current_screen' not in st.session_state:
        st.session_state['current_screen'] = 'main'
        st.session_state['all_detected_emotions'] = []

    if st.session_state['current_screen'] == 'main':
        top_bar.top_bar()

        with st.container():
            col_left, col_center, col_right = st.columns([1, 2, 1])

            with col_center:
                recording_area.recording_area()
                webrtc_ctx = webrtc_streamer(
                    key="emotion_detection",
                    video_transformer_factory=EmotionDetector,
                    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
                    media_stream_constraints={"video": True, "audio": False},
                    desired_playing_state=st.session_state.get("is_recording", False), # Control based on recording button
                    async_processing=True
                )
                if webrtc_ctx.video_transformer:
                    st.session_state['all_detected_emotions'] = webrtc_ctx.video_transformer.detected_emotions

            with col_right:
                live_transcription_panel.live_transcription_panel()

        bottom_bar.bottom_bar()

        if st.button("View Results"):
            st.session_state['current_screen'] = 'results'

    elif st.session_state['current_screen'] == 'results':
        st.title("Practice Session Results")
        col1, col2, col3 = st.columns(3)
        with col1:
            speech_fluency()
        with col2:
            body_posture()
        with col3:
            st.subheader("Emotional Tone (Facial)")
            if st.session_state['all_detected_emotions']:
                emotion_counts = {}
                for emotion in st.session_state['all_detected_emotions']:
                    emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
                if emotion_counts:
                    st.markdown("**Detected Emotions:**")
                    for emotion, count in emotion_counts.items():
                        st.markdown(f"- {emotion}: {count}")
                    most_frequent_emotion = max(emotion_counts, key=emotion_counts.get)
                    st.markdown(f"**Most Frequent Emotion:** {most_frequent_emotion}")
                    # You can add more detailed display of emotion distribution here (e.g., a bar chart)
                else:
                    st.warning("No faces detected during the recording.")
            else:
                st.info("Start recording to see facial emotion results.")

        st.subheader("Progress Overview")
        st.empty() # Placeholder for progress overview
        if st.button("Go Back to Practice"):
            st.session_state['current_screen'] = 'main'
            st.session_state['all_detected_emotions'] = []

if __name__ == "__main__":
    main()