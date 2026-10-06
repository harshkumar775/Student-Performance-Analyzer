import streamlit as st
import pandas as pd
import os


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)


# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================

st.sidebar.title("🎓 Student Analyzer")

st.sidebar.write("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Student Analysis",
        "Saved Records"
    ]
)


# ==========================================================
# STUDENT ANALYSIS PAGE
# ==========================================================

if page == "Student Analysis":

    st.title("🎓 Student Performance & Attendance Analyzer")

    st.write(
        "Analyze student marks, attendance and academic performance."
    )

    # ------------------------------------------------------
    # STUDENT INFORMATION
    # ------------------------------------------------------

    st.header("👨‍🎓 Student Information")

    name = st.text_input("Student Name")

    roll_number = st.text_input("Roll Number")

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
            "Semester 8"
        ]
    )

    # ------------------------------------------------------
    # SUBJECT MARKS
    # ------------------------------------------------------

    st.header("📚 Subject Marks")

    st.write("Enter marks obtained out of 100.")

    dsa = st.number_input(
        "DSA",
        min_value=0,
        max_value=100,
        value=0
    )

    daa = st.number_input(
        "DAA",
        min_value=0,
        max_value=100,
        value=0
    )

    java = st.number_input(
        "Java / OOPs",
        min_value=0,
        max_value=100,
        value=0
    )

    python = st.number_input(
        "Python",
        min_value=0,
        max_value=100,
        value=0
    )

    communication = st.number_input(
        "Professional Communication",
        min_value=0,
        max_value=100,
        value=0
    )

    # ------------------------------------------------------
    # ATTENDANCE
    # ------------------------------------------------------

    st.header("📅 Attendance")

    st.write(
        "Enter attendance percentage for each subject."
    )

    dsa_attendance = st.number_input(
        "DSA Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    daa_attendance = st.number_input(
        "DAA Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    java_attendance = st.number_input(
        "Java / OOPs Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    python_attendance = st.number_input(
        "Python Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    communication_attendance = st.number_input(
        "Communication Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    # ------------------------------------------------------
    # CALCULATE PERFORMANCE
    # ------------------------------------------------------

    if st.button("Calculate Performance"):

        # --------------------------------------------------
        # MARKS CALCULATION
        # --------------------------------------------------

        total_marks = (
            dsa +
            daa +
            java +
            python +
            communication
        )

        percentage = total_marks / 5

        # --------------------------------------------------
        # GRADE CALCULATION
        # --------------------------------------------------

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

        # --------------------------------------------------
        # ATTENDANCE CALCULATION
        # --------------------------------------------------

        overall_attendance = (
            dsa_attendance +
            daa_attendance +
            java_attendance +
            python_attendance +
            communication_attendance
        ) / 5

        # --------------------------------------------------
        # PERFORMANCE RESULT
        # --------------------------------------------------

        st.success(
            "Performance calculated successfully!"
        )

        st.subheader("📊 Performance Result")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Marks",
                f"{total_marks}/500"
            )

        with col2:

            st.metric(
                "Percentage",
                f"{percentage:.2f}%"
            )

        with col3:

            st.metric(
                "Grade",
                grade
            )

        # --------------------------------------------------
        # ATTENDANCE RESULT
        # --------------------------------------------------

        st.subheader("📅 Attendance Result")

        st.metric(
            "Overall Attendance",
            f"{overall_attendance:.2f}%"
        )

        # --------------------------------------------------
        # ATTENDANCE STATUS
        # --------------------------------------------------

        st.write("### Attendance Status")

        if overall_attendance >= 75:

            st.success(
                "✅ Overall attendance is above 75%."
            )

        else:

            st.warning(
                "⚠️ Overall attendance is below 75%."
            )

        # Subject attendance warnings

        if dsa_attendance < 75:

            st.warning(
                "⚠️ DSA attendance is below 75%."
            )

        if daa_attendance < 75:

            st.warning(
                "⚠️ DAA attendance is below 75%."
            )

        if java_attendance < 75:

            st.warning(
                "⚠️ Java / OOPs attendance is below 75%."
            )

        if python_attendance < 75:

            st.warning(
                "⚠️ Python attendance is below 75%."
            )

        if communication_attendance < 75:

            st.warning(
                "⚠️ Communication attendance is below 75%."
            )

        # --------------------------------------------------
        # CHART DATA
        # --------------------------------------------------

        subjects = [
            "DSA",
            "DAA",
            "Java / OOPs",
            "Python",
            "Communication"
        ]

        marks = [
            dsa,
            daa,
            java,
            python,
            communication
        ]

        attendance = [
            dsa_attendance,
            daa_attendance,
            java_attendance,
            python_attendance,
            communication_attendance
        ]

        # --------------------------------------------------
        # MARKS CHART
        # --------------------------------------------------

        st.subheader("📊 Subject-wise Performance")

        st.write("### 📚 Marks")

        marks_chart_data = pd.DataFrame(
            {
                "Subject": subjects,
                "Marks": marks
            }
        )

        st.bar_chart(
            marks_chart_data,
            x="Subject",
            y="Marks"
        )

        # --------------------------------------------------
        # ATTENDANCE CHART
        # --------------------------------------------------

        st.write("### 📅 Attendance")

        attendance_chart_data = pd.DataFrame(
            {
                "Subject": subjects,
                "Attendance": attendance
            }
        )

        st.bar_chart(
            attendance_chart_data,
            x="Subject",
            y="Attendance"
        )

        # --------------------------------------------------
        # WEAK SUBJECT DETECTION
        # --------------------------------------------------

        st.subheader("⚠️ Subject Analysis")

        weak_subjects = []

        if dsa < 50:
            weak_subjects.append("DSA")

        if daa < 50:
            weak_subjects.append("DAA")

        if java < 50:
            weak_subjects.append("Java / OOPs")

        if python < 50:
            weak_subjects.append("Python")

        if communication < 50:
            weak_subjects.append("Communication")

        if len(weak_subjects) == 0:

            st.success(
                "🎉 No weak subjects! Your performance is good."
            )

        else:

            st.warning(
                "You need to improve these subjects:"
            )

            for subject in weak_subjects:

                st.write(
                    "🔴",
                    subject
                )

        # --------------------------------------------------
        # ACADEMIC STATUS
        # --------------------------------------------------

        st.subheader("🎓 Academic Status")

        if percentage >= 50 and len(weak_subjects) == 0:

            st.success(
                "✅ PASS — Excellent academic performance!"
            )

        elif percentage >= 50:

            st.success(
                "✅ PASS — But some subjects need improvement."
            )

        else:

            st.error(
                "❌ FAIL — Overall performance needs improvement."
            )

        # --------------------------------------------------
        # PERFORMANCE LEVEL
        # --------------------------------------------------

        if percentage >= 80:

            performance_level = "Excellent 🌟"

        elif percentage >= 70:

            performance_level = "Good 👍"

        elif percentage >= 50:

            performance_level = "Average 🙂"

        else:

            performance_level = "Needs Improvement ⚠️"

        st.info(
            f"📈 Performance Level: {performance_level}"
        )

        # --------------------------------------------------
        # PERFORMANCE INSIGHTS
        # --------------------------------------------------

        st.subheader("🧠 Performance Insights")

        subject_marks = {

            "DSA": dsa,

            "DAA": daa,

            "Java / OOPs": java,

            "Python": python,

            "Communication": communication
        }

        # Best subject

        best_subject = max(
            subject_marks,
            key=subject_marks.get
        )

        best_marks = subject_marks[best_subject]

        # Weakest subject

        weakest_subject = min(
            subject_marks,
            key=subject_marks.get
        )

        weakest_marks = subject_marks[weakest_subject]

        col1, col2 = st.columns(2)

        with col1:

            st.success(
                f"🏆 Best Subject: {best_subject} "
                f"({best_marks}/100)"
            )

        with col2:

            st.warning(
                f"⚠️ Needs Improvement: "
                f"{weakest_subject} "
                f"({weakest_marks}/100)"
            )

        # --------------------------------------------------
        # RECOMMENDATION
        # --------------------------------------------------

        st.write("### 💡 Recommendation")

        if weakest_marks < 50:

            st.error(
                f"Focus more on {weakest_subject}. "
                "Your marks are below 50."
            )

        elif weakest_marks < 70:

            st.warning(
                f"You should practice more in "
                f"{weakest_subject} "
                "to improve your performance."
            )

        else:

            st.success(
                "🎉 Your performance is well balanced "
                "across all subjects."
            )

        # --------------------------------------------------
        # SAVE STUDENT DATA
        # --------------------------------------------------

        student_data = {

            "Name": name,

            "Roll Number": roll_number,

            "Semester": semester,

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

            "Weakest Subject": weakest_subject
        }

        student_df = pd.DataFrame(
            [student_data]
        )

        file_name = "student_records.csv"

        if os.path.exists(file_name):

            student_df.to_csv(
                file_name,
                mode="a",
                header=False,
                index=False
            )

        else:

            student_df.to_csv(
                file_name,
                index=False
            )

        st.success(
            "💾 Student record saved successfully!"
        )


# ==========================================================
# SAVED RECORDS PAGE
# ==========================================================

elif page == "Saved Records":

    st.title("📋 Saved Student Records")

    st.write(
        "Search and view previously saved student performance."
    )

    if os.path.exists("student_records.csv"):

        records = pd.read_csv(
            "student_records.csv"
        )

        # --------------------------------------------------
        # SEARCH STUDENT
        # --------------------------------------------------

        search_roll = st.text_input(
            "🔎 Search by Roll Number"
        )

        if search_roll:

            search_result = records[
                records["Roll Number"].astype(str)
                == search_roll
            ]

            if not search_result.empty:

                st.success(
                    "✅ Student found!"
                )

                st.dataframe(
                    search_result,
                    width="stretch"
                )

            else:

                st.warning(
                    "⚠️ Student not found."
                )

        # --------------------------------------------------
        # ALL RECORDS
        # --------------------------------------------------

        st.subheader(
            "📊 All Student Records"
        )

        st.dataframe(
            records,
            width="stretch"
        )

    else:

        st.info(
            "No student records available yet."
        )
        