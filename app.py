import streamlit as st
from pypdf import PdfReader
import sqlite3


# ==========================================
# DATABASE SETUP
# ==========================================

def create_database():

    conn = sqlite3.connect("study_assistant.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            score INTEGER,
            total INTEGER,
            percentage REAL
        )
    """)

    conn.commit()
    conn.close()


create_database()


# ==========================================
# SAVE QUIZ RESULT
# ==========================================

def save_quiz_result(topic, score, total):

    percentage = (score / total) * 100

    conn = sqlite3.connect("study_assistant.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO quiz_results
        (topic, score, total, percentage)
        VALUES (?, ?, ?, ?)
        """,
        (topic, score, total, percentage)
    )

    conn.commit()
    conn.close()


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("🎓 AI Study Assistant")

st.write(
    "Your personal AI-powered study companion"
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📚 Study Menu")

option = st.sidebar.selectbox(
    "Choose an option",
    [
        "Home",
        "Ask AI",
        "Generate Notes",
        "Generate Quiz",
        "PDF Summarizer",
        "Study Planner",
        "Progress Tracker"
    ]
)


# ==========================================
# HOME
# ==========================================

if option == "Home":

    st.header("Welcome! 👋")

    st.write(
        """
        Welcome to your AI Study Assistant!

        Use this application to:

        📖 Learn difficult topics

        📝 Generate study notes

        ❓ Practice quizzes

        📄 Read and summarize PDFs

        📅 Create study plans

        📊 Track your progress
        """
    )

    st.success(
        "🚀 Your study assistant is ready!"
    )


# ==========================================
# ASK AI
# ==========================================

elif option == "Ask AI":

    st.header("🤖 Ask AI")

    question = st.text_area(
        "What would you like to learn?",
        placeholder="Example: Explain binary search in simple words"
    )

    if st.button("Ask AI"):

        if question:

            st.success(
                "Question received! ✅"
            )

            st.subheader("Your Question")

            st.write(question)

            st.subheader("🤖 AI Response")

            st.info(
                """
                AI Demo Mode

                Your question was successfully received.

                Real AI responses will be connected
                when API credits are available.
                """
            )

        else:

            st.warning(
                "Please enter a question first."
            )


# ==========================================
# GENERATE NOTES
# ==========================================

elif option == "Generate Notes":

    st.header("📝 Generate Notes")

    topic = st.text_input(
        "Enter a topic",
        placeholder="Example: Python Functions"
    )

    if st.button("Generate Notes"):

        if topic:

            st.success(
                "Topic received! ✅"
            )

            st.subheader(
                f"📚 Study Notes: {topic}"
            )

            st.markdown(
                f"""
                ### Introduction

                **{topic}** is an important topic
                for students to learn.

                ### Key Concepts

                - Important concept 1
                - Important concept 2
                - Important concept 3

                ### Example

                A simple example related to
                **{topic}**.

                ### Important Points

                - Understand the main definition.
                - Learn the basic concepts.
                - Practice with examples.

                🤖 Real AI-generated notes will be
                connected later.
                """
            )

        else:

            st.warning(
                "Please enter a topic first."
            )


# ==========================================
# GENERATE QUIZ
# ==========================================

elif option == "Generate Quiz":

    st.header("❓ Generate Quiz")

    st.write(
        "Choose a topic and test your knowledge!"
    )

    topic = st.selectbox(
        "Choose a quiz topic",
        [
            "Python",
            "Computer Science",
            "General Knowledge"
        ]
    )


    # ======================================
    # PYTHON QUIZ
    # ======================================

    if topic == "Python":

        st.subheader("🐍 Python Quiz")

        q1 = st.radio(
            "1. What is Python?",
            [
                "A programming language",
                "An operating system",
                "A web browser",
                "A database"
            ],
            key="python_q1"
        )

        q2 = st.radio(
            "2. Which symbol is used for comments?",
            [
                "//",
                "#",
                "/* */",
                "<!-- -->"
            ],
            key="python_q2"
        )

        q3 = st.radio(
            "3. Which function displays output?",
            [
                "display()",
                "show()",
                "print()",
                "output()"
            ],
            key="python_q3"
        )

        q4 = st.radio(
            "4. Which data type stores True or False?",
            [
                "String",
                "Integer",
                "Boolean",
                "List"
            ],
            key="python_q4"
        )

        q5 = st.radio(
            "5. Which keyword defines a function?",
            [
                "function",
                "define",
                "def",
                "func"
            ],
            key="python_q5"
        )

        if st.button("Submit Python Quiz"):

            score = 0

            if q1 == "A programming language":
                score += 1

            if q2 == "#":
                score += 1

            if q3 == "print()":
                score += 1

            if q4 == "Boolean":
                score += 1

            if q5 == "def":
                score += 1

            save_quiz_result(
                "Python",
                score,
                5
            )

            percentage = (score / 5) * 100

            st.success(
                "🎉 Quiz Completed!"
            )

            st.subheader(
                f"Your Score: {score} / 5"
            )

            st.progress(
                percentage / 100
            )

            st.write(
                f"Percentage: **{percentage:.0f}%**"
            )

            if percentage == 100:

                st.balloons()

                st.success(
                    "🏆 Perfect score!"
                )

            elif percentage >= 60:

                st.info(
                    "👍 Good job! Keep practicing!"
                )

            else:

                st.warning(
                    "📚 Keep studying and try again!"
                )


    # ======================================
    # COMPUTER SCIENCE QUIZ
    # ======================================

    elif topic == "Computer Science":

        st.subheader("💻 Computer Science Quiz")

        q1 = st.radio(
            "1. What does CPU stand for?",
            [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Computer Processing User"
            ],
            key="cs_q1"
        )

        q2 = st.radio(
            "2. What is RAM?",
            [
                "Permanent storage",
                "Temporary memory",
                "A programming language",
                "A network"
            ],
            key="cs_q2"
        )

        q3 = st.radio(
            "3. Which is an operating system?",
            [
                "Python",
                "Google",
                "Windows",
                "HTML"
            ],
            key="cs_q3"
        )

        q4 = st.radio(
            "4. What does HTTP relate to?",
            [
                "Web communication",
                "Computer memory",
                "Graphics",
                "File compression"
            ],
            key="cs_q4"
        )

        q5 = st.radio(
            "5. What does URL identify?",
            [
                "A web resource address",
                "A CPU",
                "A keyboard",
                "A programming variable"
            ],
            key="cs_q5"
        )

        if st.button("Submit Computer Science Quiz"):

            score = 0

            if q1 == "Central Processing Unit":
                score += 1

            if q2 == "Temporary memory":
                score += 1

            if q3 == "Windows":
                score += 1

            if q4 == "Web communication":
                score += 1

            if q5 == "A web resource address":
                score += 1

            save_quiz_result(
                "Computer Science",
                score,
                5
            )

            percentage = (score / 5) * 100

            st.success(
                "🎉 Quiz Completed!"
            )

            st.subheader(
                f"Your Score: {score} / 5"
            )

            st.progress(
                percentage / 100
            )

            st.write(
                f"Percentage: **{percentage:.0f}%**"
            )


    # ======================================
    # GENERAL KNOWLEDGE QUIZ
    # ======================================

    elif topic == "General Knowledge":

        st.subheader("🌎 General Knowledge Quiz")

        q1 = st.radio(
            "1. What is the capital of France?",
            [
                "Paris",
                "London",
                "Rome",
                "Berlin"
            ],
            key="gk_q1"
        )

        q2 = st.radio(
            "2. How many continents are there?",
            [
                "5",
                "6",
                "7",
                "8"
            ],
            key="gk_q2"
        )

        q3 = st.radio(
            "3. Which planet is known as the Red Planet?",
            [
                "Earth",
                "Mars",
                "Jupiter",
                "Venus"
            ],
            key="gk_q3"
        )

        q4 = st.radio(
            "4. How many days are in a week?",
            [
                "5",
                "6",
                "7",
                "8"
            ],
            key="gk_q4"
        )

        q5 = st.radio(
            "5. Which is the largest ocean?",
            [
                "Atlantic Ocean",
                "Indian Ocean",
                "Pacific Ocean",
                "Arctic Ocean"
            ],
            key="gk_q5"
        )

        if st.button("Submit General Knowledge Quiz"):

            score = 0

            if q1 == "Paris":
                score += 1

            if q2 == "7":
                score += 1

            if q3 == "Mars":
                score += 1

            if q4 == "7":
                score += 1

            if q5 == "Pacific Ocean":
                score += 1

            save_quiz_result(
                "General Knowledge",
                score,
                5
            )

            percentage = (score / 5) * 100

            st.success(
                "🎉 Quiz Completed!"
            )

            st.subheader(
                f"Your Score: {score} / 5"
            )

            st.progress(
                percentage / 100
            )

            st.write(
                f"Percentage: **{percentage:.0f}%**"
            )


# ==========================================
# PDF SUMMARIZER
# ==========================================

elif option == "PDF Summarizer":

    st.header("📄 PDF Summarizer")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if uploaded_file:

        st.success(
            "PDF uploaded successfully! ✅"
        )

        reader = PdfReader(
            uploaded_file
        )

        page_count = len(
            reader.pages
        )

        st.write(
            f"📑 Number of pages: **{page_count}**"
        )

        full_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:

                full_text += text + "\n"

        if full_text.strip():

            st.success(
                "PDF text extracted successfully! ✅"
            )

            with st.expander(
                "📖 View Extracted Text"
            ):

                st.text(full_text)

            words = full_text.split()

            st.subheader(
                "📝 Basic Summary"
            )

            if len(words) > 100:

                summary = " ".join(
                    words[:100]
                )

                st.write(
                    summary + "..."
                )

            else:

                st.write(full_text)

        else:

            st.warning(
                "⚠️ No readable text was found."
            )


# ==========================================
# STUDY PLANNER
# ==========================================

elif option == "Study Planner":

    st.header("📅 Study Planner")

    subject = st.text_input(
        "Enter subject",
        placeholder="Example: Mathematics"
    )

    days = st.number_input(
        "How many days?",
        min_value=1,
        max_value=30,
        value=7
    )

    if st.button("Create Plan"):

        if subject:

            st.success(
                f"Study plan created for {subject}! ✅"
            )

            st.subheader(
                f"📅 {days}-Day Study Plan"
            )

            for day in range(1, days + 1):

                st.write(
                    f"**Day {day}:** Study "
                    f"{subject} for 1 hour."
                )

        else:

            st.warning(
                "Please enter a subject first."
            )


# ==========================================
# PROGRESS TRACKER
# ==========================================

elif option == "Progress Tracker":

    st.header("📊 Progress Tracker")

    st.write(
        "Your completed quiz results are saved here."
    )

    conn = sqlite3.connect(
        "study_assistant.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT topic, score, total, percentage
        FROM quiz_results
        ORDER BY id DESC
        """
    )

    results = cursor.fetchall()

    conn.close()


    # --------------------------------------
    # NO RESULTS
    # --------------------------------------

    if not results:

        st.info(
            "📚 No quiz results yet. "
            "Complete a quiz first!"
        )


    # --------------------------------------
    # SHOW RESULTS
    # --------------------------------------

    else:

        st.subheader(
            "📚 Quiz History"
        )

        for result in results:

            topic = result[0]
            score = result[1]
            total = result[2]
            percentage = result[3]

            st.write(
                f"**{topic}** — "
                f"{score}/{total} — "
                f"{percentage:.0f}%"
            )

            st.progress(
                percentage / 100
            )


        # ----------------------------------
        # STATISTICS
        # ----------------------------------

        total_quizzes = len(results)

        average_score = sum(
            result[3] for result in results
        ) / total_quizzes

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total Quizzes",
                total_quizzes
            )

        with col2:

            st.metric(
                "Average Score",
                f"{average_score:.0f}%"
            )


        # ----------------------------------
        # CLEAR HISTORY
        # ----------------------------------

        st.divider()

        if st.button(
            "🗑️ Clear Quiz History"
        ):

            conn = sqlite3.connect(
                "study_assistant.db"
            )

            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM quiz_results"
            )

            conn.commit()
            conn.close()

            st.success(
                "Quiz history cleared! ✅"
            )

            st.rerun()