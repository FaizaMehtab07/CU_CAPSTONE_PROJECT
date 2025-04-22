import streamlit as st
from streamlit_webrtc import webrtc_streamer

def recording_area():
    st.markdown("### 🎥 Video Recording")
    webrtc_streamer(
        key="camera",
        media_stream_constraints={"video": True, "audio": False}
    )

    # Recording Controls
    if 'is_recording' not in st.session_state:
        st.session_state['is_recording'] = False

    st.selectbox("Select Device", ["Default Cam"])
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🔴 Record" if not st.session_state['is_recording'] else "⏹️ Stop"):
            st.session_state['is_recording'] = not st.session_state['is_recording']
    with col2:
        st.button("⏸️ Pause", disabled=not st.session_state['is_recording'])
    with col3:
        if st.button("🔁 Reset"):
            st.session_state['is_recording'] = False
            st.rerun()

    st.button("START", use_container_width=True)
    st.selectbox("Select Device", ["Mic 1", "Mic 2"])
