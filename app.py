import streamlit as st
from trip_agents import tripagents
from trip_tasks import triptasks

from crewai import Crew

import datetime

st.set_page_config(page_icon="✈️", layout="wide")



st.title("🏖️ PlanMyTrip")
if __name__ == "__main__":

    st.subheader("Let AI agents plan your next vacation!",
                 divider="rainbow", anchor=False)

    import datetime

    today = datetime.datetime.now().date()
    next_year = today.year + 1
    jan_16_next_year = datetime.date(next_year, 1, 10)

    with st.sidebar:
        st.header("👇 Enter your trip details")
        with st.form("my_form"):
            location = st.text_input(
                "Where are you currently located?", placeholder="San Mateo, CA")
            cities = st.text_input(
                "City and country are you interested in vacationing at?", placeholder="Bali, Indonesia")
            date_range = st.date_input(
                "Date range you are interested in traveling?",
                min_value=today,
                value=(today, jan_16_next_year + datetime.timedelta(days=6)),
                format="MM/DD/YYYY",
            )
            interests = st.text_area("High level interests and hobbies or extra details about your trip?",
                                     placeholder="2 adults who love swimming, dancing, hiking, and eating")

            submitted = st.form_submit_button("Submit")

        st.divider()


city_selection_agent, local_expert_agent, travel_budget_agent = tripagents()
city_selection_task, local_expert_task, travel_budget_task = triptasks(city_selection_agent, local_expert_agent, travel_budget_agent)


if submitted:
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        # with st.container(height=500, border=False):
            # sys.stdout = StreamToExpander(st)
        crew = Crew(
            agents=[city_selection_agent, local_expert_agent, travel_budget_agent],
            tasks=[city_selection_task, local_expert_task, travel_budget_task],
            verbose=True
        )

        inputs={'origin': location, 
        'cities': cities,
        "range" : date_range,
        "interests" : interests}

        result = crew.kickoff(inputs=inputs)

        # status.update(label="✅ Trip Plan Ready!",
        #               state="complete", expanded=False)

    st.subheader("Here is your Trip Plan", anchor=False, divider="rainbow")
    st.markdown(result)