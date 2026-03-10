import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"


def api_post(url, data=None):
    r = requests.post(url, json=data)
    if r.status_code != 200:
        st.error(r.json().get("detail", "API Error"))
        return None
    return r.json()


def api_get(url):
    r = requests.get(url)
    if r.status_code != 200:
        st.error(r.json().get("detail", "API Error"))
        return None
    return r.json()


st.title("Adaptive Diagnostic Engine")

if "session_id" not in st.session_state:
    session = api_post(f"{API_URL}/start_session")
    st.session_state.session_id = session["session_id"]
    st.session_state.q_index = 0
    st.session_state.question = None
    st.session_state.study_plan = None


progress = st.progress(st.session_state.q_index / 10)

if st.session_state.study_plan:

    st.header("Personalized Study Plan")
    st.write(st.session_state.study_plan)

    if st.button("Restart"):
        st.session_state.clear()
        st.rerun()

else:

    if st.session_state.question is None:
        q = api_get(f"{API_URL}/next_question/{st.session_state.session_id}")
        st.session_state.question = q

    q = st.session_state.question

    st.subheader(f"Question {st.session_state.q_index + 1}/10")
    st.write(q["question_text"])
    st.caption(f"Topic: {q['topic']}")

    options = list(q["options"].keys())

    answer = st.radio(
        "Choose an option",
        options,
        format_func=lambda x: f"{x}: {q['options'][x]}",
    )

    if st.button("Submit"):

        result = api_post(
            f"{API_URL}/submit_answer/{st.session_state.session_id}",
            {"answer": answer},
        )

        if result:

            if result["correct"]:
                st.success("Correct")
            else:
                st.error("Incorrect")

            st.info(f"Estimated Ability: {result['new_ability']:.2f}")

            st.session_state.q_index += 1
            st.session_state.question = None

            if st.session_state.q_index == 10:

                plan = api_get(
                    f"{API_URL}/study_plan/{st.session_state.session_id}"
                )

                st.session_state.study_plan = plan["study_plan"]

            st.rerun()