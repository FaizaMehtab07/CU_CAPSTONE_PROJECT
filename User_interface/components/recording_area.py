import streamlit as st
from streamlit_webrtc import webrtc_streamer

def recording_area():
    st.subheader("🎥 Video Recording")

    # Live webcam preview using streamlit-webrtc
    ctx = webrtc_streamer(
        key="camera",
        media_stream_constraints={"video": True, "audio": False}
    )

    # Use Streamlit's session state to track recording status
    if 'is_recording' not in st.session_state:
        st.session_state['is_recording'] = False

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("⏺️ Record" if not st.session_state['is_recording'] else "⏹️ Stop"):
            st.session_state['is_recording'] = not st.session_state['is_recording']
            if st.session_state['is_recording']:
                st.success("Recording started... (This is a visual simulation)")
            else:
                st.warning("Recording stopped.")

    with col2:
        st.button("⏸️ Pause", disabled=not st.session_state['is_recording'])

    with col3:
        if st.button("🔁 Reset"):
            st.session_state['is_recording'] = False
            st.rerun()

if __name__ == "__main__":
    recording_area()