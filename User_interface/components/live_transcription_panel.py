import streamlit as st

def live_transcription_panel():
    st.markdown("### 📝 Live Transcription")
    st.markdown("""
        <div style="color:white; font-size: 15px;">
            <p>Thank you for joining today’s presentation.</p>
            <p>I'm excited to share with you our latest findings...</p>
            <p><b>Tip:</b> Try to maintain a steady pace</p>
        </div>
    """, unsafe_allow_html=True)

    st.button("🔄 Restart")
