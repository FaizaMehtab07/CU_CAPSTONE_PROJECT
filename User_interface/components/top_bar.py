import streamlit as st

def top_bar():
    st.markdown("""
        <div style='background-color: #94c0e6; padding: 1.5rem; border-radius: 1rem;'>
            <h1 style='color: #003366; text-align: center; margin: 0;'>SpeakSmart</h1>
            <p style='color: #1a1a1a; text-align: center;'>Your AI-powered communication coach</p>
        </div>
    """, unsafe_allow_html=True)
