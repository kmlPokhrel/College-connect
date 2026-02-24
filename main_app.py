import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd

# ==============================
# 1. INITIALIZE FIREBASE
# ==============================
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ==============================
# 2. GOOGLE OAUTH CONFIG
# ==============================
SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

def google_login():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json",
        SCOPES
    )
    # Using port 0 allows the OS to pick an available port
    credentials_google = flow.run_local_server(port=0)
    service = build("oauth2", "v2", credentials=credentials_google)
    user_info = service.userinfo().get().execute()
    st.session_state.user = user_info
    st.rerun()

# ==============================
# 3. UI SETUP
# ==============================
st.set_page_config(page_title="College Connect", page_icon="🎓", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
if st.session_state.user:
    menu = ["My Profile", "Discover Students", "Logout"]
else:
    menu = ["Login"]
choice = st.sidebar.radio("Go to", menu)

# ==============================
# 4. LOGIN PAGE
# ==============================
if choice == "Login":
    st.title("🎓 College Connect")
    st.subheader("Welcome to the Student Networking Hub")
    st.write("Please sign in with your college Google account to continue.")
    
    if st.button("Login with Google", type="primary"):
        google_login()

# ==============================
# 5. MY PROFILE PAGE
# ==============================
elif choice == "My Profile":
    st.title("👤 My Profile")
    user = st.session_state.user
    user_email = user["email"]

    # Fetch existing data from Firestore if it exists
    doc_ref = db.collection("students").document(user_email)
    doc = doc_ref.get()
    existing_data = doc.to_dict() if doc.exists else {}

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(user.get("picture", ""), width=150)
        st.write(f"**Email:** {user_email}")
    
    with col2:
        name = st.text_input("Full Name", value=existing_data.get("name", user.get("name", "")))
        branch = st.selectbox("Branch", ["CSE", "ECE", "ME", "CE", "EE", "MBA"], 
                              index=["CSE", "ECE", "ME", "CE", "EE", "MBA"].index(existing_data.get("branch", "CSE")))
        skills = st.text_area("Skills (Comma separated)", value=existing_data.get("skills", ""))
        bio = st.text_area("Short Bio", value=existing_data.get("bio", ""))

        if st.button("Save Profile", type="primary"):
            db.collection("students").document(user_email).set({
                "name": name,
                "email": user_email,
                "branch": branch,
                "skills": skills,
                "bio": bio,
                "profile_pic": user.get("picture", "")
            })
            st.success("Profile Updated Successfully!")

# ==============================
# 6. DISCOVER STUDENTS (The Hero Feature)
# ==============================
elif choice == "Discover Students":
    st.title("🔍 Search Students")
    
    search_query = st.text_input("Search by Name, Branch, or Skill")
    
    # Fetch all students from Firestore
    students_ref = db.collection("students")
    docs = students_ref.stream()
    
    student_list = []
    for doc in docs:
        student_list.append(doc.to_dict())

    if student_list:
        df = pd.DataFrame(student_list)
        
        # Simple Filter Logic
        if search_query:
            filtered_df = df[df.apply(lambda row: search_query.lower() in str(row).lower(), axis=1)]
        else:
            filtered_df = df

        if not filtered_df.empty:
            for _, student in filtered_df.iterrows():
                with st.expander(f"🎓 {student['name']} ({student['branch']})"):
                    st.write(f"**Skills:** {student['skills']}")
                    st.write(f"**Bio:** {student['bio']}")
                    st.write(f"**Contact:** {student['email']}")
        else:
            st.warning("No students found matches your search.")
    else:
        st.info("No profiles have been created yet.")

# ==============================
# 7. LOGOUT
# ==============================
elif choice == "Logout":
    st.session_state.user = None
    st.success("Logged out successfully!")
    st.rerun()