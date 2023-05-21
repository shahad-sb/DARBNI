import streamlit as st
from main import suggest

st.markdown('# Training Plan')
st.markdown("### Help your intern thrive in their role with a training plan designed specifically for them. Enter the details below to begin")

st.markdown("### ")
job_postion = st.text_input("What position will the intern hold during their internship?", value="")

st.markdown("### ")
industry = st.text_input("What industry does your company operate in?", value="")

st.markdown("###")
week_no = st.number_input("Please indicate the duration of the intern's stay in weeks", value=1, step=1, min_value=1, max_value=52)

if st.button(label="Generate Training Plan", help="Click! Click!"):

    suggestions = suggest(job_postion, industry, week_no)
    for week, tasks in suggestions.items(): 
        st.markdown(f"## {week}")
        for task in tasks:
            st.markdown(f"- {task}")
            