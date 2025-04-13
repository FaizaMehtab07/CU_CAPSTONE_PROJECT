import streamlit as st

def recording_area():
    st.subheader("Video Recording")
    video_placeholder = st.empty() # Placeholder for the video feed

    # Use Streamlit's session state to track the recording status
    if 'is_recording' not in st.session_state:
        st.session_state['is_recording'] = False

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("Stop" if st.session_state['is_recording'] else "Record"):
            st.session_state['is_recording'] = not st.session_state['is_recording']

    with col2:
        st.button("Pause", disabled=not st.session_state['is_recording']) # Enable/disable based on recording state

    with col3:
        st.button("Reset")

if __name__ == "__main__":
    recording_area()