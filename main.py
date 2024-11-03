# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message

#from helper_functions import ai_agents

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Prompt")

resume = form.text_area("Enter resume link", height=5)

job = form.text_area("Enter Job link", height=5)

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, course_details = process_user_message(user_prompt)
    st.write(response)

    st.divider()

    print(course_details)
    df = pd.DataFrame(course_details)
    df 



    crew = Crew(
    agents=[profiler,analyst, resume_strategist],
    tasks=[extract_requirements, compile_profile,align_with_requirement],
    verbose=True
)



job_application_inputs = {
    'job_posting_url': job
    
    # 'https://www.mycareersfuture.gov.sg/job/information-technology/data-scientist-cpo-03dba75ab1fec49a3aac63d2c676949a?source=MCF&event=Search'
    # 'https://www.mycareersfuture.gov.sg/job/information-technology/full-stack-developer-ntt-data-singapore-12059bf21549d1794e3535de365d0a77'
    ,'cv_content':resume
}


### this execution will take a few minutes to run

result = crew.kickoff(inputs=job_application_inputs)

result






