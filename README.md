# 🗺️ PlanMyTrip : Agentic AI-Powered Travel Planner

PlanMyTrip utilizes the CrewAI framework to automate and elevate the trip planning process, featuring an intuitive Streamlit interface. This project showcases the seamless collaboration and execution of complex tasks by autonomous AI agents, enhanced by the interactive and accessible nature of Streamlit.

## 🚀 Tech stack used
1. CrewAI
2. Python
3. Groq
4. streamlit

## 🔮 CrewAI Framework

CrewAI simplifies the orchestration of role-playing AI agents. In VacAIgent, these agents collaboratively decide on cities and craft a complete itinerary for your trip based on specified preferences, all accessible via a streamlined Streamlit user interface.

## 🏃‍♂️ Running the Application

To experience the PlanMyTrip app:

- **Configure Environment**: Set up the environment variables for [Serper](https://serper.dev/), and [Groq](https://console.groq.com/). Use the `secrets.example` as a guide to add your keys then move that file (`secrets.toml`) to `.streamlit/secrets.toml`.

- **Install Dependencies**: Execute `pip install -r requirements.txt` in your terminal.
- **Launch the App**: Run `streamlit run app.py` to start the Streamlit interface.

## 📈 Details & Explanation

- **Streamlit UI**: The Streamlit interface is implemented in `app.py`, where users can input their trip details.
- **Components**:
  - `./trip_tasks.py`: Contains task prompts for the agents.
  - `./trip_agents.py`: Manages the creation of agents.
  - `./tools directory`: Houses tool classes used by agents.
  - `./app.py`: The heart of the Streamlit app.

## 📜 License

PlanMyTrip is open-sourced under the MIT License.

## 📧 Contact 
For any questions or suggestions, feel free to reach out:

- **Email**: mayur.dabade21@vit.edu
- **GitHub** : [mayurd8862](https://github.com/mayur8862)
- **LinkedIn** : [https://www.linkedin.com/in/mayur-dabade-b527a9230](https://www.linkedin.com/in/mayur-dabade-b527a9230)

---
[Click here](#) to use the web application.
