import streamlit as st

# App title
st.title("Alumni Connect")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "My Profile", "Mentor Connect"))

# Home Page
if page == "Home":
    st.header("Welcome to the Alumni Connect Portal!")
    
    # Post section
    st.subheader("Post an update")
    post_content = st.text_area("Share some news...")
    if st.button("Share"):
        st.success("Your post has been shared!")
    
    # Poll section
    st.subheader("Create a Poll")
    poll_question = st.text_input("Poll Question")
    if poll_question:
        st.success(f"Poll created: {poll_question}")

    # Options for adding media to posts
    st.subheader("Attach media")
    st.file_uploader("Add a photo")
    st.file_uploader("Add a video")
    st.file_uploader("Attach files")

# My Profile Page
elif page == "My Profile":
    st.header("My Profile")
    
    # Example user profile details
    st.subheader("Alex Smith")
    st.text("Email: alex.smith@example.com")
    st.text("Graduated: 2020")
    st.text("Major: Computer Science")
    st.text("Company: Tech Innovations Inc.")
    st.text("Position: Software Engineer")
    st.text("Location: New York, NY")

# Mentor Connect Page
elif page == "Mentor Connect":
    st.header("Mentor Connect")
    
    # Nearby Mentors
    st.subheader("Nearby Mentors")
    st.write("**Alice Brown** \nLocal Tech \nDistance: 2 km")
    st.write("**Charlie Green** \nNearby Solutions \nDistance: 5 km")
    
    # Recommended Mentors
    st.subheader("Recommended Mentors")
    st.write("**John Doe** \nTech Corp \nExperience: 5 years \nLocation: Boston, MA")

# Run the app with "streamlit run <script_name.py>"
