import streamlit as st

def bottom_bar():
    st.markdown("""
        <style>
            .bottom-bar {
                background-color: #1f1f2e;
                padding: 20px 0;
                border-radius: 12px;
                margin-top: 30px;
                text-align: center;
            }
            .stButton > button {
                background-color: #2f303e;
                color: white;
                border: none;
                padding: 12px 30px;
                font-size: 16px;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="bottom-bar">', unsafe_allow_html=True)
    st.button("View Results")
    st.markdown('</div>', unsafe_allow_html=True)
