#display the console processing on streamlit UI
import streamlit as st 
import re
from main import crewai_setup
import sys 
import os 


class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer))
            self.buffer = []


# # Redirect stdout to our custom stream
# sys.stdout = StreamToUI(st)
# sys.stdout = sys.__stdout__

def run_crewai_app():
    st.title("💼 Crew AI multi agent system")

    st.markdown("""# Agents""")
    st.markdown("""
            ### Social Media Analyst 
            Goal : Be a dominant leader in Social Media marketing, using Twitter, Reddit and Facebook to drive digital engagement to a company's audience and beyond helping grow their brand
        """)
    st.markdown("""
            ### Market Research Analyst
            Goal : Deliver deep insights into market dynamics, customer preferences, and competitive landscapes to inform strategic planning
        """)
    
    st.markdown("""
            ### Creative Director
            Goal : Steer the creative direction of marketing campaigns to ensure they are impactful, cohesive, and aligned with brand values
        """)

    st.divider()

    st.markdown("""
        Task 1 : Find information for the company we are working with.
        """)
    
    company = st.text_input("Please input the company you're working with")

    
    st.markdown("""
        Task 2 : Draft content on social media 
        """)


    # with st.expander("🎯 goal"):
    #     st.write(""" Aims to develop a cutting-edge AI tool for improving investor relations and awareness through social media engagement across Twitter, Reddit, and Facebook. The primary goals are to establish leadership in social media marketing, enhance digital engagement, and promote the services of www.xespn.com. They seek to grow a company's brand and awareness by leveraging data from the company's own resources as well as information scraped from competitors' social media and industry blogs.
    #               """)
    
    # n = st.sidebar.selectbox('You want to generate', ("All Prompts","Few Prompts"),placeholder="How many prompts you want?")
    # if n =="Few Prompts":
    #     nb=st.sidebar.number_input('How many prompts you want ? ', min_value=1, max_value=88)
    #     st.session_state['nb'] = nb
    #     st.sidebar.write(f"You're going to generatethe {nb} first prompts ")
    
    c1,c2=st.columns(2)    
    run = c1.button("Run Analysis")
    if run:
        stop=c2.button('stop')
        if not stop:
            with st.container(border=True):
                sys.stdout = StreamToExpander(st)
                
                with st.spinner("Generating Results"):
                    crew_result = crewai_setup()
            
        st.header("Results:")
        st.markdown(crew_result)
        with st.expander("Output"):
            # Redirect stdout to our custom stream
            sys.stdout = StreamToExpander(st)
if __name__ == "__main__":
    run_crewai_app()