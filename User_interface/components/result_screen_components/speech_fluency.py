import streamlit as st

def speech_fluency():
    st.subheader("Speech Fluency")
    st.markdown("**Pace:** 120 wpm")
    st.markdown("**Fillers:** 3")
    st.markdown("**Clarity:** 95%")
    st.image("https://static.streamlit.io/examples/wave_chart.png", caption="Fluency Trend", width=200) # Placeholder image

if __name__ == "__main__":
    speech_fluency()