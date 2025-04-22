import streamlit as st
from streamlit_webrtc import webrtc_streamer

def recording_area():
    st.markdown("""
        <div style='background-color: #e6f0fa; padding: 1rem; border-radius: 1rem; margin-bottom: 1rem;'>
            <h3 style='color: #003366;'>🎥 Video Recording</h3>
        </div>
    """, unsafe_allow_html=True)

    ctx = webrtc_streamer(
        key="camera",
        media_stream_constraints={"video": True, "audio": False}
    )

    if 'is_recording' not in st.session_state:
        st.session_state['is_recording'] = False

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("⏺️ Record" if not st.session_state['is_recording'] else "⏹️ Stop"):
            st.session_state['is_recording'] = not st.session_state['is_recording']
            if st.session_state['is_recording']:
                st.success("Recording started... (simulated)")
            else:
                st.warning("Recording stopped.")

    with col2:
        st.button("⏸️ Pause", disabled=not st.session_state['is_recording'])

    with col3:
        if st.button("🔁 Reset"):
            st.session_state['is_recording'] = False
            st.rerun()
