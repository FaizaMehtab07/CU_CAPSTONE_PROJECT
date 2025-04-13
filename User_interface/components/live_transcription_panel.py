import streamlit as st

def live_transcription_panel():
    st.subheader("Live Transcription")
    st.markdown('"Thank you for joining today\'s presentation. I\'m excited to share with you our latest findings..."')  # Placeholder transcription text
    st.markdown("---")  # Separator
    st.markdown("**Tip:** Try to maintain a steady pace")

if __name__ == "__main__":
    live_transcription_panel()