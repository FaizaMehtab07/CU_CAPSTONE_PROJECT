import streamlit as st
from components import top_bar
from components import recording_area
from components import live_transcription_panel
from components import bottom_bar
from components.result_screen_components.speech_fluency import speech_fluency
from components.result_screen_components.body_posture import body_posture
from components.result_screen_components.emotional_tone import emotional_tone

def main():
    if 'current_screen' not in st.session_state:
        st.session_state['current_screen'] = 'main'

    if st.session_state['current_screen'] == 'main':
        top_bar.top_bar()

        with st.container():
            col_left, col_center, col_right = st.columns([1, 2, 1])

            with col_center:
                recording_area.recording_area()

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
            emotional_tone()
        st.subheader("Progress Overview")
        st.empty() # Placeholder for progress overview
        if st.button("Go Back to Practice"):
            st.session_state['current_screen'] = 'main'

if __name__ == "__main__":
    main()