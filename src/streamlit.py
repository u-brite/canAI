import streamlit as st
from canai_utils.summary import summary
from canai_utils.feature_selection import feature_selection

# Config the whole app
st.set_page_config(
    page_title="canAI", page_icon="🧊", layout="wide", initial_sidebar_state="expanded",
)

st.write(
    "<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>",
    unsafe_allow_html=True,
)
#st.write(
#    "<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-right:50px;}</style>",
#    unsafe_allow_html=True,
#)


def main():
    """Navigating streamlit app"""

    # st.sidebar.title("Tools")
    st.title('canAI')
    st.markdown('Comparing feature extraction methods for biomarker discovery in a pan-cancer study')
    st.markdown('U-BRITE Hackin\' Omics 2022 Project')

    PAGES = {"Home": summary, "Biomarkers": feature_selection}

    # Select pages
    # Use dropdown if you prefer
    selection = st.radio("", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading Page {selection} ..."):
        page = page()


if __name__ == "__main__":
    main()
