import streamlit as st

def body_posture():
    st.subheader("Body Posture")
    st.image("https://static.streamlit.io/examples/dog_chart.png", caption="Posture Analysis", width=150) # Placeholder image
    st.markdown("**Status:** Correct Posture")

if __name__ == "__main__":
    body_posture()