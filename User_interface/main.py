import streamlit as st
from components import top_bar
from components import recording_area
from components import live_transcription_panel

def main():
    top_bar.top_bar()

    col_left, col_center, col_right = st.columns([1, 2, 1]) # Adjust column widths

    with col_center:
        recording_area.recording_area()

    with col_right:
        live_transcription_panel.live_transcription_panel()

if __name__ == "__main__":
    main()