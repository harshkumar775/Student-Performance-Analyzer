import os
import pandas as pd
import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Student Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #0b1120;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #243044;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 0px;
}

.hero-subtitle {
    font-size: 17px;
    color: #94a3b8;
    margin-top: 5px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 23px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.dashboard-card {
    background: linear-gradient(145deg, #172033, #101827);
    border: 1px solid #273449;
    border-radius: 16px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
}

.card-icon {
    font-size: 22px;
}

.card-label {
    color: #94a3b8;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    margin-top: 5px;
}

.card-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

.feature-card {
    background-color: #111827;
    border: 1px solid #273449;
    border-radius: 16px;
    padding: 20px;
    margin-top: 10px;
}

.feature-title {
    font-size: 15px;
    color: #94a3b8;
}

.feature-value {
    font-size: 21px;
    font-weight: 700;
    margin-top: 7px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""",
    unsafe_allow_html=True,
)


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.markdown(
    """
<div style="font-size:27px;font-weight:800;margin-bottom:5px;">
    🎓 Student
</div>

<div style="color:#94a3b8;font-size:14px;margin-bottom:25px;">
    Analytics Dashboard
</div>
""",
    unsafe_allow_html=True,
)

page = st.sidebar.radio("Navigation", ["🏠 Student Analysis", "📋 Saved Records"])

st.sidebar.markdown("---")

st.sidebar.caption("Student Performance & Attendance Analyzer")

st.sidebar.caption("Built with Python + Streamlit")


# ==========================================================
# SESSION STATE
# ==========================================================

if "calculated" not in st.session_state:
    st.session_state.calculated = False

if "student_result" not in st.session_state:
    st.session_state.student_result = None


# ==========================================================
# STUDENT ANALYSIS PAGE
# ==========================================================

if page == "🏠 Student Analysis":

  # ------------------------------------------------------
  # HERO
  # ------------------------------------------------------

  st.markdown(
      """
<div class="hero-title">
    🎓 Student Analytics
</div>

<div class="hero-subtitle">
    Turn academic data into clear performance insights.
</div>
""",
      unsafe_allow_html=True,
  )

  # ------------------------------------------------------
  # STUDENT PROFILE
  # ------------------------------------------------------

  st.markdown(
      '<div class="section-title">👤 Student Profile</div>',
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns(3)

  with col1:
    name = st.text_input("Student Name", placeholder="Enter student name")

  with col2:
    roll_number = st.text_input("Roll Number", placeholder="Enter roll number")

  with col3:
    semester = st.selectbox(
        "Semester",
        [
            "Semester 1",
            "Semester 2",
            "Semester 3",
            "Semester 4",
            "Semester 5",
            "Semester 6",
            "Semester 7",
            "Semester 8",
        ],
    )

  # ------------------------------------------------------
  # ACADEMIC PERFORMANCE
  # ------------------------------------------------------

  st.markdown(
      '<div class="section-title">📚 Academic Performance</div>',
      unsafe_allow_html=True,
  )

  st.caption("Enter marks obtained out of 100.")

  col1, col2, col3, col4, col5 = st.columns(5)

  with col1:
    dsa = st.number_input("DSA", min_value=0, max_value=100, value=0)

  with col2:
    daa = st.number_input("DAA", min_value=0, max_value=100, value=0)

  with col3:
    java = st.number_input("Java / OOPs", min_value=0, max_value=100, value=0)

  with col4:
    python = st.number_input("Python", min_value=0, max_value=100, value=0)

  with col5:
    communication = st.number_input(
        "Communication", min_value=0, max_value=100, value=0
    )

  # ------------------------------------------------------
  # ATTENDANCE
  # ------------------------------------------------------

  st.markdown(
      '<div class="section-title">📅 Attendance Overview</div>',
      unsafe_allow_html=True,
  )

  col1, col2, col3, col4, col5 = st.columns(5)

  with col1:
    dsa_attendance = st.number_input(
        "DSA (%)", min_value=0.0, max_value=100.0, value=0.0
    )

  with col2:
    daa_attendance = st.number_input(
        "DAA (%)", min_value=0.0, max_value=100.0, value=0.0
    )

  with col3:
    java_attendance = st.number_input(
        "Java / OOPs (%)", min_value=0.0, max_value=100.0, value=0.0
    )

  with col4:
    python_attendance = st.number_input(
        "Python (%)", min_value=0.0, max_value=100.0, value=0.0
    )

  with col5:
    communication_attendance = st.number_input(
        "Communication (%)", min_value=0.0, max_value=100.0, value=0.0
    )

  # ------------------------------------------------------
  # ANALYZE BUTTON
  # ------------------------------------------------------

  st.markdown("")

  analyze = st.button("🚀 ANALYZE PERFORMANCE", type="primary", width="stretch")

  # ------------------------------------------------------
  # CALCULATIONS
  # ------------------------------------------------------

  if analyze:

    if not name.strip() or not roll_number.strip():

      st.error("Please enter Student Name and Roll Number.")

    else:

      total_marks = dsa + daa + java + python + communication

      percentage = total_marks / 5

      overall_attendance = (
          dsa_attendance
          + daa_attendance
          + java_attendance
          + python_attendance
          + communication_attendance
      ) / 5

      # ------------------------------------------------
      # GRADE
      # ------------------------------------------------

      if percentage >= 90:
        grade = "A+"

      elif percentage >= 80:
        grade = "A"

      elif percentage >= 70:
        grade = "B"

      elif percentage >= 60:
        grade = "C"

      elif percentage >= 50:
        grade = "D"

      else:
        grade = "F"

      # ------------------------------------------------
      # PERFORMANCE LEVEL
      # ------------------------------------------------

      if percentage >= 80:
        performance_level = "Excellent 🌟"

      elif percentage >= 70:
        performance_level = "Good 👍"

      elif percentage >= 50:
        performance_level = "Average 🙂"

      else:
        performance_level = "Needs Improvement ⚠️"

      # ------------------------------------------------
      # SUBJECT DATA
      # ------------------------------------------------

      subject_marks = {
          "DSA": dsa,
          "DAA": daa,
          "Java / OOPs": java,
          "Python": python,
          "Communication": communication,
      }

      subjects = list(subject_marks.keys())

      marks = list(subject_marks.values())

      attendance = [
          dsa_attendance,
          daa_attendance,
          java_attendance,
          python_attendance,
          communication_attendance,
      ]

      # ------------------------------------------------
      # BEST / WEAKEST
      # ------------------------------------------------

      best_subject = max(subject_marks, key=subject_marks.get)

      weakest_subject = min(subject_marks, key=subject_marks.get)

      best_marks = subject_marks[best_subject]

      weakest_marks = subject_marks[weakest_subject]

      # ------------------------------------------------
      # WEAK SUBJECTS
      # ------------------------------------------------

      weak_subjects = [
          subject for subject, mark in subject_marks.items() if mark < 50
      ]

      # ------------------------------------------------
      # STORE RESULT
      # ------------------------------------------------

      st.session_state.student_result = {
          "Name": name,
          "Roll Number": roll_number,
          "Semester": semester,
          "Total Marks": total_marks,
          "DSA": dsa,
          "DAA": daa,
          "Java / OOPs": java,
          "Python": python,
          "Communication": communication,
          "Percentage": percentage,
          "Grade": grade,
          "Attendance": overall_attendance,
          "Performance Level": performance_level,
          "Best Subject": best_subject,
          "Weakest Subject": weakest_subject,
          "Best Marks": best_marks,
          "Weakest Marks": weakest_marks,
          "Weak Subjects": weak_subjects,
          "Subjects": subjects,
          "Marks": marks,
          "Attendance Data": attendance,
      }

      st.session_state.calculated = True

  # ======================================================
  # RESULTS
  # ======================================================

  if st.session_state.calculated:

    result = st.session_state.student_result

    st.markdown("---")

    st.markdown(
        '<div class="section-title">📊 Performance Dashboard</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # METRIC CARDS
    # --------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

      st.markdown(
          f"""
<div class="dashboard-card">
    <div class="card-icon">📊</div>
    <div class="card-label">Total Marks</div>
    <div class="card-value">{result["Total Marks"]}/500</div>
</div>
""",
          unsafe_allow_html=True,
      )

    with col2:

      st.markdown(
          f"""
<div class="dashboard-card">
    <div class="card-icon">🎯</div>
    <div class="card-label">Percentage</div>
    <div class="card-value">{result["Percentage"]:.1f}%</div>
</div>
""",
          unsafe_allow_html=True,
      )

    with col3:

      st.markdown(
          f"""
<div class="dashboard-card">
    <div class="card-icon">🏆</div>
    <div class="card-label">Grade</div>
    <div class="card-value">{result["Grade"]}</div>
</div>
""",
          unsafe_allow_html=True,
      )

    with col4:

      st.markdown(
          f"""
<div class="dashboard-card">
    <div class="card-icon">📅</div>
    <div class="card-label">Attendance</div>
    <div class="card-value">{result["Attendance"]:.1f}%</div>
</div>
""",
          unsafe_allow_html=True,
      )

    # --------------------------------------------------
    # STATUS
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">🎓 Academic Status</div>',
        unsafe_allow_html=True,
    )

    if result["Percentage"] >= 50:

      st.success("✅ PASS — Academic performance is satisfactory.")

    else:

      st.error("❌ FAIL — Academic performance needs improvement.")

    if result["Attendance"] >= 75:

      st.success("🟢 Attendance Status: Safe")

    else:

      st.warning("🟠 Attendance Status: Below 75%")

    # --------------------------------------------------
    # CHARTS
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">📈 Visual Analytics</div>',
        unsafe_allow_html=True,
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

      st.write("### 📚 Subject Performance")

      marks_df = pd.DataFrame(
          {"Subject": result["Subjects"], "Marks": result["Marks"]}
      )

      st.bar_chart(marks_df, x="Subject", y="Marks")

    with chart_col2:

      st.write("### 📅 Attendance")

      attendance_df = pd.DataFrame(
          {"Subject": result["Subjects"], "Attendance": result["Attendance Data"]}
      )

      st.bar_chart(attendance_df, x="Subject", y="Attendance")

    # --------------------------------------------------
    # INSIGHTS
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">🧠 Performance Insights</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
      st.markdown(
          f'<div class="feature-card">'
          f'<div class="feature-title">🏆 BEST SUBJECT</div>'
          f'<div class="feature-value">{result["Best Subject"]} —'
          f' {result["Best Marks"]}/100</div>'
          f"</div>",
          unsafe_allow_html=True,
      )

    with col2:
      st.markdown(
          f'<div class="feature-card">'
          f'<div class="feature-title">⚠️ NEEDS ATTENTION</div>'
          f'<div class="feature-value">{result["Weakest Subject"]} —'
          f' {result["Weakest Marks"]}/100</div>'
          f"</div>",
          unsafe_allow_html=True,
      )

    # --------------------------------------------------
    # WEAK SUBJECTS
    # --------------------------------------------------

    if result["Weak Subjects"]:
      st.warning("Subjects below 50 marks:")

      for subject in result["Weak Subjects"]:
        st.write(f"🔴 {subject}")
    else:
      st.success("🎉 No subject is below 50 marks.")

    # --------------------------------------------------
    # RECOMMENDATION
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">💡 Personalized Recommendation</div>',
        unsafe_allow_html=True,
    )

    if result["Weakest Marks"] < 50:
      st.error(
          f"Focus strongly on {result['Weakest Subject']}. Your marks are below"
          " 50."
      )
    elif result["Weakest Marks"] < 70:
      st.warning(
          f"Spend additional practice time on {result['Weakest Subject']}."
      )
    else:
      st.success("Your performance is balanced across all subjects.")


# ==========================================================
# SAVED RECORDS PAGE
# ==========================================================

elif page == "📋 Saved Records":

  st.markdown(
      """
<div class="hero-title">
    📋 Saved Records
</div>

<div class="hero-subtitle">
    Manage and search student performance records.
</div>
""",
      unsafe_allow_html=True,
  )

  file_name = "student_records.csv"

  if os.path.exists(file_name):
    try:
      records = pd.read_csv(file_name)

      # ------------------------------------------------
      # SUMMARY
      # ------------------------------------------------

      total_students = len(records)

      average_percentage = records["Percentage"].mean() if not records.empty else 0

      average_attendance = records["Attendance"].mean() if not records.empty else 0

      col1, col2, col3 = st.columns(3)

      with col1:
        st.metric("👨‍🎓 Students", total_students)

      with col2:
        st.metric("📊 Avg Percentage", f"{average_percentage:.1f}%")

      with col3:
        st.metric("📅 Avg Attendance", f"{average_attendance:.1f}%")

      # ------------------------------------------------
      # SEARCH
      # ------------------------------------------------

      st.markdown("---")

      st.markdown(
          '<div class="section-title">🔎 Find Student</div>',
          unsafe_allow_html=True,
      )

      search_roll = st.text_input(
          "Search using Roll Number", placeholder="Example: 101"
      )

      if search_roll:
        search_result = records[
            records["Roll Number"].astype(str).str.strip() == search_roll.strip()
        ]

        if not search_result.empty:
          st.success("✅ Student found!")

          st.dataframe(search_result, width="stretch", hide_index=True)

        else:
          st.warning("⚠️ Student not found.")

      # ------------------------------------------------
      # ALL RECORDS
      # ------------------------------------------------

      st.markdown("---")

      st.markdown(
          '<div class="section-title">📊 All Student Records</div>',
          unsafe_allow_html=True,
      )

      st.dataframe(records, width="stretch", hide_index=True)

    except Exception as error:
      st.error(f"Unable to read student records file: {error}")

  else:
    st.info("📂 No student records available yet.")