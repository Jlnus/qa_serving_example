import os
from pathlib import Path

import streamlit as st
from confirm_button_hack import cache_on_button_press
import requests

# SETTING PAGE CONFIG TO WIDE MODE
ASSETS_DIR_PATH = os.path.join(Path(__file__).parent.parent.parent.parent, "assets")

st.set_page_config(layout="wide")

root_password = "password"


def main():
    st.title("Question Answering")

    if "context" not in st.session_state:
        st.session_state["context"] = ""
    if "question" not in st.session_state:
        st.session_state["question"] = ""

    with st.form(key="my_form", clear_on_submit=True):
        st.text_input(
            "Context를 입력해주세요.",
            placeholder="context",
            key="context",
        )

        st.text_input(
            "Question를 입력해주세요.",
            placeholder="question",
            key="question",
        )

        submit = st.form_submit_button(label="Answer")

    if submit:
        if st.session_state["context"] == "" or st.session_state["question"] == "":
            st.error("문장을 입력해주세요")
        else:
            with st.spinner("계산 중..."):
                input = {
                    "context": st.session_state["context"],
                    "question": st.session_state["question"],
                }
                response = requests.post("http://localhost:8001/order", json=input)
                answer = response.json()["products"][0]["result"]
                st.text("Answer :")
                st.text(answer)


@cache_on_button_press("Authenticate")
def authenticate(password) -> bool:
    return password == root_password


password = st.empty()
pw = password.text_input("password (default : 'password')", type="password")

if authenticate(pw):
    password.success("You are authenticated!")
    password.empty()
    main()
else:
    st.error("The password is invalid.")
