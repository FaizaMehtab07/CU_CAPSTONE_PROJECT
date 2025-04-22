import streamlit as st

def live_transcription_panel():
    st.markdown("""
        <div style='background-color: #fef6e4; padding: 1rem; border-radius: 1rem;'>
            <h4 style='color: #7f5539;'>Live Transcription</h4>
            <div style='border: 1px dashed #ccc; padding: 1rem; min-height: 200px; background-color: #fff;'>
                <em>Transcription will appear here in real-time...</em>
            </div>
        </div>
    """, unsafe_allow_html=True)
