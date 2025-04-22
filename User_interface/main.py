import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import numpy as np
from keras.models import load_model

from components import top_bar, recording_area, live_transcription_panel, bottom_bar
from components.result_screen_components import speech_fluency, body_posture

# Set Streamlit page config
st.set_page_config(page_title="SpeakSmart", layout="wide")

# Apply pastel theme and font colors
st.markdown("""
    <style>
        body {
            background-color: #f4f9ff;
        }
        .block-container {
            background: linear-gradient(135deg, #fef6e4, #e0f7fa);
            padding: 2rem;
            border-radius: 10px;
        }
        .stButton > button {
            background-color: #4682B4;
            color: white;
            border-radius: 10px;
            padding: 0.5rem 1rem;
        }
        .stButton > button:hover {
            background-color: #5a9bd4;
        }
        h1, h2, h3, h4 {
            color: #30475e !important;
        }
        .results-section h1, .results-section h2, .results-section h3, .results-section h4, .results-section p {
            color: #1e3a5f !important;
        }
        .results-section .stAlert {
            background-color: #fff9c4;
        }
    </style>
""", unsafe_allow_html=True)

# Load emotion model and face cascade
try:
    emotion_model = load_model('models/emotion_model.h5')
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
except Exception as e:
    st.error(f"Error loading model or face cascade: {e}")
    emotion_model = None
    face_cascade = None

# Video transformer class
class EmotionDetector(VideoTransformerBase):
    def __init__(self):
        self.detected_emotions = []

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            face_resized = cv2.resize(face_roi, (48, 48)) / 255.0
            face_input = np.expand_dims(face_resized, axis=(0, -1))

            if emotion_model:
                preds = emotion_model.predict(face_input)
                label = self.get_emotion_label(np.argmax(preds))
                self.detected_emotions.append(label)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(img, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        return img

    def get_emotion_label(self, label):
        emotion_map = {
            0: 'anger', 1: 'disgust', 2: 'fear',
            3: 'happiness', 4: 'sadness', 5: 'surprise', 6: 'neutral'
        }
        return emotion_map.get(label, 'unknown')

# Main logic
def main():
    if 'current_screen' not in st.session_state:
        st.session_state['current_screen'] = 'main'
        st.session_state['all_detected_emotions'] = []

    if st.session_state['current_screen'] == 'main':
        top_bar.top_bar()

        with st.container():
            col_left, col_center, col_right = st.columns([0.7, 2.6, 1.4])
            with col_center:
                recording_area.recording_area()
                ctx = webrtc_streamer(
                    key="emotion_detection",
                    video_transformer_factory=EmotionDetector,
                    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
                    media_stream_constraints={"video": True, "audio": False},
                    desired_playing_state=st.session_state.get("is_recording", False),
                    async_processing=True
                )
                if ctx.video_transformer:
                    st.session_state['all_detected_emotions'] = ctx.video_transformer.detected_emotions

            with col_right:
                live_transcription_panel.live_transcription_panel()

        bottom_bar.bottom_bar()

        if st.button("➡️ View Results"):
            st.session_state['current_screen'] = 'results'

    elif st.session_state['current_screen'] == 'results':
        st.markdown('<div class="results-section">', unsafe_allow_html=True)

        st.title("📊 Practice Session Results")
        col1, col2, col3 = st.columns(3)

        with col1:
            speech_fluency.speech_fluency()
        with col2:
            body_posture.body_posture()
        with col3:
            st.subheader("Emotional Tone (Facial)")
            emotions = st.session_state['all_detected_emotions']
            if emotions:
                counts = {e: emotions.count(e) for e in set(emotions)}
                for emotion, count in counts.items():
                    st.markdown(f"- **{emotion.capitalize()}**: {count}")
                st.success(f"**Most Frequent Emotion:** {max(counts, key=counts.get)}")
            else:
                st.warning("No emotion data available.")

        st.markdown("---")
        if st.button("🔁 Back to Practice"):
            st.session_state['current_screen'] = 'main'
            st.session_state['all_detected_emotions'] = []

        st.markdown('</div>', unsafe_allow_html=True)

# Run app
if __name__ == "__main__":
    main()
