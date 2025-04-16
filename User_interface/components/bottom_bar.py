import streamlit as st

def bottom_bar():
    col1, col2, col3 = st.columns([1, 2, 1]) # Adjusting widths

    with col1:
        st.button("⬅️") # Left arrow

    with col2:
        pass # Placeholder for potential central navigation elements

    with col3:
        st.button("Restart")

if __name__ == "__main__":
    bottom_bar()