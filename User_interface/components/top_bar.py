import streamlit as st

def top_bar():
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust widths as needed

    with col1:
        st.markdown("### SpeakSmart")  # Or use st.image for a logo

    with col2:
        st.button("📹 Practice Mode")  # Using an emoji for the icon

    with col3:
        st.image("https://cdn.jsdelivr.net/gh/streamlit/streamlit/doc/_static/user-icon.png", width=30) # Placeholder user icon

if __name__ == "__main__":
    top_bar()