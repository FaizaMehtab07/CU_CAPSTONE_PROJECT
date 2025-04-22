import streamlit as st

def top_bar():
    st.markdown("""
        <style>
            .top-bar {
                background-color: #1f1f2e;
                padding: 10px 20px;
                border-radius: 12px;
                margin-bottom: 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .top-bar h3 {
                color: white;
                margin: 0;
                font-weight: 600;
            }
            .top-button {
                background-color: #444654;
                color: white;
                padding: 6px 16px;
                border-radius: 6px;
                font-size: 14px;
                border: none;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="top-bar">
            <h3>🎙️ SpeakSmart</h3>
            <button class="top-button">Practice Mode</button>
        </div>
    """, unsafe_allow_html=True)
