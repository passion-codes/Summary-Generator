import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import tensorflow as tf
import streamlit.components.v1 as components

# Mock user database
users_db = {"admin": "admin123", "user": "user123"}

# Style and header section for the website
def app_header():
    st.markdown("""
    <style>
    /* Responsive header and navbar */
    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 40px 0 0 0;
        text-align: center;
        background-color: #4CAF50;
        color: white;
        font-size: 24px;
        z-index: 1000;
    }
    .navbar {
        position: fixed;
        margin-top: 83px;
        top: 80px;
        left: 0;
        width: 100%;
        background-color: #333;
        z-index: 999;
    }
    .navbar a {
        color: #f2f2f2;
        text-align: center;
        display: block;
        float: left;
        padding: 14px 16px;
        text-decoration: none;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    .content {
        padding: 62px 20px;
        margin: 0 auto;
        max-width: 800px;  /* Content width */
        text-align: center;
        border-radius: 10px;
        
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px 0;
    }
                
    
                
    .signin{
        background-color:blue;
        padding:2px;
        color:white; 
        float: right;
        margin: 12px 3px ;
               
    }
                
    .login,signin{
        background-color:blue;
        padding:2px;
        color:white; 
        float: right;
        margin: 12px;       
    }
                
    /* Sidebar buttons styled like clickable boxes */
    .sidebar-box {
        border: 2px solid #04AA6D;
        border-radius: 25px;
        padding: 15px;
        margin-bottom: 20px;
        text-align: center;
        cursor: pointer;
        transition: 0.3s;
    }
    .sidebar-box:hover {
        background-color: #04AA6D;
        color: white;
    }
    /* Responsive layout for better adaptability */
    @media screen and (max-width: 768px) {
        .navbar {
            flex-direction: column;
        }
        .navbar a {
            padding: 12px;
        }
        .content {
            padding: 62px 20px;  
        }
    }
    #facultySearch{
        margin-top: 15px;
        width: 400px;
                }

    </style>
    <div class="header">
      <h1>Automated Publication Summary Generator</h1>
      <p>AI-Driven Publication Insights and Dynamic Filtering</p>
    </div>
    <div class="navbar">
      <a href="#upload">Upload Data</a>
      <a href="#faculty">Faculty Profiles</a>
      <a href="#insights">AI/ML Insights</a>
      <a href="#citations">Visualize Citations</a>
      <a href="#report">Download Report</a>
     <input type="text"  placeholder="Search Faculty..." id="facultySearch">
      <button class="login">Login</button>
      <button class="signin">Sign In</button>       
    </div>
    """, unsafe_allow_html=True)
    # JavaScript for live search (mock search functionality)
components.html("""
    <script>
    document.getElementById('facultySearch').addEventListener('keyup', function(e) {
      const query = e.target.value.toLowerCase();
      const names = document.querySelectorAll('h3');
      names.forEach(name => {
        if (name.textContent.toLowerCase().includes(query)) {
          name.parentElement.style.display = 'block';
        } else {
          name.parentElement.style.display = 'none';
        }
      });
    });
    </script>
""", height=0)

# Login/Sign-up functionality
def login_form():
    st.sidebar.subheader("Login / Sign Up")
    choice = st.sidebar.selectbox("Select", ["Login", "Sign Up"])
    
    if choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        login_button = st.sidebar.button("Login")
        
        if login_button:
            if username in users_db and users_db[username] == password:
                st.sidebar.success(f"Welcome {username}!")
                return True
            else:
                st.sidebar.error("Invalid username or password!")
                return False
    elif choice == "Sign Up":
        st.sidebar.write("Sign-up functionality coming soon!")
        return False

# Footer for the website
def footer():
    st.markdown("""
    <div class="footer">
      <p>Smart India Hackathon 2024 | Publication Summary Generator | Team AgriTech_1</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation with radio buttons designed like boxes
def sidebar_navigation():
    st.sidebar.title("Automated Publication Summary Generator")
    selected_option = st.sidebar.radio("Choose an option", 
                                       ["Home","Upload Data", "View Faculty Profiles", "AI/ML Insights", "Visualize Citations", "Download Report"],
                                       index=0)
    login_form()

    # Style the radio buttons as box-like clickable items
    st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .stRadio > div > label {
        background: #f2f2f2;
        border-radius: 8px;
        padding: 10px;
        transition: background-color 0.3s ease;
        cursor: pointer;
        text-align: center;
    }
    .stRadio > div > label:hover {
        background-color: #04AA6D;
        color: white;
    }
    .stRadio > div > label input[type="radio"] {
        display: none;
    }
    .stRadio > div > label:has(input[type="radio"]:checked) {
        background-color: #04AA6D;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    return selected_option

# Login/Sign-up functionality
def login_form():
    st.sidebar.subheader("Login / Sign Up")
    choice = st.sidebar.selectbox("Select", ["Login", "Sign Up"])
    
    if choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        login_button = st.sidebar.button("Login")
        
        if login_button:
            if username in users_db and users_db[username] == password:
                st.sidebar.success(f"Welcome {username}!")
                return True
            else:
                st.sidebar.error("Invalid username or password!")
                return False
    elif choice == "Sign Up":
        st.sidebar.write("Sign-up functionality coming soon!")
        return False

def home():
    st.header("Automated Publication Summary Generator")


# Content area for "Upload Data"
def upload_section():
    st.header("Upload Faculty Publication Data")
    uploaded_file = st.file_uploader("Upload your publication file (Excel)", type=["xlsx"])
    

# Content area for "View Faculty Profiles"
def view_faculty_profiles():
    st.header("Faculty Profiles")
    if 'df' in st.session_state:
        df = st.session_state['df']
        faculties = df.groupby('Faculty Name')
        
        for name, group in faculties:
            st.subheader(name)
            st.write(f"Department: {group['Department'].values[0]}")
            st.write(f"Total Publications: {len(group)}")
            st.write(f"Most Recent Publication: {group.sort_values('Year', ascending=False).iloc[0]['Title']}")
    else:
        st.warning("Please upload publication data first.")

# Content area for "AI/ML Insights"
def ai_insights_section():
    st.header("AI/ML Insights on Publications")
    
    if 'df' in st.session_state:
        df = st.session_state['df']
        st.subheader("Collaboration Insights (AI/ML Simulated)")
        faculty_collab_scores = {name: np.random.rand() for name in df['Faculty Name'].unique()}
        st.write(f"Simulated collaboration scores for each faculty:")
        st.write(faculty_collab_scores)

        st.subheader("Trend Analysis (Simulated Publication Predictions)")
        trend_years = list(range(2010, 2024))
        simulated_trend = np.random.poisson(lam=3, size=(len(faculty_collab_scores), len(trend_years)))
        st.write(f"Simulated publication trends from 2010 to 2024.")
        fig, ax = plt.subplots()
        sns.heatmap(simulated_trend, annot=False, cmap="YlGnBu", cbar=True, ax=ax)
        ax.set_xlabel("Year")
        ax.set_ylabel("Faculty (simulated)")
        st.pyplot(fig)
    else:
        st.warning("Please upload publication data first.")

# Content area for "Visualize Citations"
def visualize_citations():
    st.header("Citation Visualization")
    
    if 'df' in st.session_state:
        df = st.session_state['df']
        
        st.subheader("Citations Over Time")
        fig, ax = plt.subplots()
        df.groupby('Year')['Citations'].sum().plot(kind='bar', ax=ax)
        ax.set_title("Citations by Year")
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Citations")
        st.pyplot(fig)
    else:
        st.warning("Please upload publication data first.")

# Content area for "Download Report"
def download_report():
    st.header("Generate and Download Publication Summary Report")
    
    if 'df' in st.session_state:
        df = st.session_state['df']
        
        st.subheader("Downloadable Summary Report")
        if st.button("Download Excel Report"):
            # Create Excel report
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df.to_excel(writer, index=False, sheet_name='Summary')
            writer.save()
            output.seek(0)
            
            st.download_button(label="Download Excel Report", data=output, file_name='publication_summary.xlsx', mime="application/vnd.ms-excel")
        
        if st.button("Download Word Report"):
            # Placeholder for Word report generation (could use python-docx)
            st.info("Word report generation coming soon!")
    else:
        st.warning("Please upload publication data first.")

# Main Function
def main():
    app_header()
    
    # Sidebar navigation and radio button functionality
    selected_option = sidebar_navigation()

    # Content wrapped in a centered div for all selected options
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    
    # Display content based on selected option
    if selected_option == "Upload Data":
        upload_section()
    elif selected_option == "Home":
        home()
    elif selected_option == "View Faculty Profiles":
        view_faculty_profiles()
    elif selected_option == "AI/ML Insights":
        ai_insights_section()
    elif selected_option == "Visualize Citations":
        visualize_citations()
    elif selected_option == "Download Report":
        download_report()
    
    st.markdown("</div>", unsafe_allow_html=True)

    footer()

# Run the Streamlit app
if __name__ == '__main__':
    main()
