import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Employee Retention Predictor",
    page_icon="💼",
    layout="wide"
)
# ===========================================
# SIDEBAR
# ===========================================

with st.sidebar:

    st.title("💼 HR Dashboard")

    st.markdown("---")

    st.subheader("📌 Project Details")

    st.write("**Project:** Employee Retention Predictor")

    st.write("**Model:** Random Forest Classifier")

    st.write("**Features:** 35 Employee Attributes")

    st.write("**Developer:** Bhuvana")

    st.write("**Version:** 1.0")

    st.markdown("---")

    st.subheader("📖 Prediction Guide")

    st.success("🟢 Stay = Employee likely to remain")

    st.error("🔴 Leave = Employee at risk of attrition")

    st.info("📊 Confidence shows model certainty.")

# -----------------------------
# LOAD MODEL & ENCODERS
# -----------------------------
model = joblib.load("../Dataset/employee_retention_model.pkl")
encoders = joblib.load("../Dataset/label_encoders.pkl")

# -----------------------------
# PROFESSIONAL HEADER
# -----------------------------

st.markdown("""
<style>

.dashboard-title{
background:linear-gradient(135deg,#0F4C81,#1E88E5);
padding:30px;
border-radius:18px;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,0.20);
margin-bottom:20px;
}

.dashboard-title h1{
font-size:42px;
margin-bottom:8px;
}

.dashboard-title h3{
font-weight:400;
margin-top:0px;
}

.dashboard-title p{
font-size:18px;
color:#ECEFF1;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-title">

<h1>💼 HR Analytics Dashboard</h1>

<h3>Employee Retention Prediction System</h3>

<p>
Leverage Machine Learning to predict employee attrition, support HR decisions,
and improve workforce retention with intelligent analytics.
</p>

</div>
""", unsafe_allow_html=True)

# ----------# -----------------------------
# INPUT FORM
# -----------------------------

st.header("📝 Employee Details")

# ======================================================
# EMPLOYEE IDENTITY
# ======================================================

st.subheader("👤 Employee Identity")

EmployeeName = st.text_input(
    "Employee Name",
    placeholder="Enter employee name"
)

EmployeeID = st.text_input(
    "Employee ID",
    placeholder="EMP001"
)

Designation = st.text_input(
    "Designation",
    placeholder="Software Engineer"
)

st.divider()

# ======================================================
# EMPLOYEE PROFILE
# ======================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#1565C0,#42A5F5);
padding:15px;
border-radius:12px;
color:white;
margin-top:10px;
margin-bottom:20px;
">

<h3>👤 Employee Profile</h3>

<p>Basic personal and educational details.</p>

</div>
""", unsafe_allow_html=True)
Age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=30
)

Gender = st.selectbox(
    "Gender",
    list(encoders["Gender"].classes_)
)

MaritalStatus = st.selectbox(
    "Marital Status",
    list(encoders["MaritalStatus"].classes_)
)

Education = st.selectbox(
    "Education",
    [1,2,3,4,5]
)

EducationField = st.selectbox(
    "Education Field",
    list(encoders["EducationField"].classes_)
)

EmployeeNumber = st.number_input(
    "Employee Number",
    value=1
)

EmployeeCount = st.number_input(
    "Employee Count",
    value=1
)

st.divider()

# ======================================================
# JOB INFORMATION
# ======================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#00897B,#26A69A);
padding:15px;
border-radius:12px;
color:white;
margin-top:10px;
margin-bottom:20px;
box-shadow:0 3px 8px rgba(0,0,0,0.15);
">

<h3>💼 Job Information</h3>

<p>Employee job-related information.</p>

</div>
""", unsafe_allow_html=True)

BusinessTravel = st.selectbox(
    "Business Travel",
    list(encoders["BusinessTravel"].classes_)
)

Department = st.selectbox(
    "Department",
    list(encoders["Department"].classes_)
)

JobRole = st.selectbox(
    "Job Role",
    list(encoders["JobRole"].classes_)
)

JobLevel = st.selectbox(
    "Job Level",
    [1, 2, 3, 4, 5]
)

DistanceFromHome = st.number_input(
    "Distance From Home",
    min_value=0,
    max_value=50,
    value=5
)

OverTime = st.selectbox(
    "Over Time",
    list(encoders["OverTime"].classes_)
)

st.divider()

# ======================================================
# EMPLOYEE SATISFACTION
# ======================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#8E24AA,#BA68C8);
padding:15px;
border-radius:12px;
color:white;
margin-top:10px;
margin-bottom:20px;
box-shadow:0 3px 8px rgba(0,0,0,0.15);
">

<h3>😊 Employee Satisfaction</h3>

<p>Employee engagement and workplace satisfaction.</p>

</div>
""", unsafe_allow_html=True)

EnvironmentSatisfaction = st.selectbox(
    "Environment Satisfaction",
    [1, 2, 3, 4]
)

JobInvolvement = st.selectbox(
    "Job Involvement",
    [1, 2, 3, 4]
)

JobSatisfaction = st.selectbox(
    "Job Satisfaction",
    [1, 2, 3, 4]
)

RelationshipSatisfaction = st.selectbox(
    "Relationship Satisfaction",
    [1, 2, 3, 4]
)

WorkLifeBalance = st.selectbox(
    "Work Life Balance",
    [1, 2, 3, 4]
)

st.divider()

# ======================================================
# SALARY & COMPENSATION
# ======================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#F57C00,#FFA726);
padding:15px;
border-radius:12px;
color:white;
margin-top:10px;
margin-bottom:20px;
box-shadow:0 3px 8px rgba(0,0,0,0.15);
">

<h3>💰 Salary & Compensation</h3>

<p>Salary, compensation and employee benefits.</p>

</div>
""", unsafe_allow_html=True)

DailyRate = st.number_input(
    "Daily Rate",
    min_value=100,
    max_value=2000,
    value=800
)

HourlyRate = st.number_input(
    "Hourly Rate",
    min_value=0,
    max_value=200,
    value=80
)

MonthlyIncome = st.number_input(
    "Monthly Income",
    min_value=1000,
    max_value=100000,
    value=5000
)

MonthlyRate = st.number_input(
    "Monthly Rate",
    min_value=0,
    value=5000
)

PercentSalaryHike = st.number_input(
    "Percent Salary Hike",
    min_value=0,
    max_value=100,
    value=15
)

StockOptionLevel = st.selectbox(
    "Stock Option Level",
    [0, 1, 2, 3]
)

st.divider()

# ======================================================
# PERFORMANCE & EXPERIENCE
# ======================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#2E7D32,#66BB6A);
padding:15px;
border-radius:12px;
color:white;
margin-top:10px;
margin-bottom:20px;
box-shadow:0 3px 8px rgba(0,0,0,0.15);
">

<h3>📈 Performance & Experience</h3>

<p>Career growth, experience and performance metrics.</p>

</div>
""", unsafe_allow_html=True)

PerformanceRating = st.selectbox(
    "Performance Rating",
    [1, 2, 3, 4]
)

NumCompaniesWorked = st.number_input(
    "Number of Companies Worked",
    min_value=0,
    max_value=20,
    value=1
)

TotalWorkingYears = st.number_input(
    "Total Working Years",
    min_value=0,
    max_value=50,
    value=10
)

TrainingTimesLastYear = st.number_input(
    "Training Times Last Year",
    min_value=0,
    max_value=20,
    value=2
)

YearsAtCompany = st.number_input(
    "Years At Company",
    min_value=0,
    max_value=40,
    value=5
)

YearsInCurrentRole = st.number_input(
    "Years In Current Role",
    min_value=0,
    max_value=20,
    value=3
)

YearsSinceLastPromotion = st.number_input(
    "Years Since Last Promotion",
    min_value=0,
    max_value=20,
    value=1
)

YearsWithCurrManager = st.number_input(
    "Years With Current Manager",
    min_value=0,
    max_value=20,
    value=3
)
st.divider()


# -----------------------------
# PREDICTION BUTTON
# -----------------------------

predict = st.button(
    "🚀 Predict Employee Retention",
    use_container_width=True
)

if predict:

    if not EmployeeName or not EmployeeID or not Designation:
        st.warning("⚠ Please enter Employee Name, Employee ID and Designation before prediction.")
        st.stop()

    # Create input dataframe
    input_df = pd.DataFrame([{

        "Age": Age,
        "BusinessTravel": BusinessTravel,
        "DailyRate": DailyRate,
        "Department": Department,
        "DistanceFromHome": DistanceFromHome,
        "Education": Education,
        "EducationField": EducationField,
        "EmployeeCount": EmployeeCount,
        "EmployeeNumber": EmployeeNumber,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "Gender": Gender,
        "HourlyRate": HourlyRate,
        "JobInvolvement": JobInvolvement,
        "JobLevel": JobLevel,
        "JobRole": JobRole,
        "JobSatisfaction": JobSatisfaction,
        "MaritalStatus": MaritalStatus,
        "MonthlyIncome": MonthlyIncome,
        "MonthlyRate": MonthlyRate,
        "NumCompaniesWorked": NumCompaniesWorked,
        "OverTime": OverTime,
        "Over18": "Y",
        "PercentSalaryHike": PercentSalaryHike,
        "PerformanceRating": PerformanceRating,
        "RelationshipSatisfaction": RelationshipSatisfaction,
        "StandardHours": 80,
        "StockOptionLevel": StockOptionLevel,
        "TotalWorkingYears": TotalWorkingYears,
        "TrainingTimesLastYear": TrainingTimesLastYear,
        "WorkLifeBalance": WorkLifeBalance,
        "YearsAtCompany": YearsAtCompany,
        "YearsInCurrentRole": YearsInCurrentRole,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "YearsWithCurrManager": YearsWithCurrManager

    }])
    # Encode categorical columns
    for column in input_df.columns:
        if column in encoders:
            input_df[column] = encoders[column].transform(input_df[column])

    # Arrange columns exactly as the model expects
    input_df = input_df[model.feature_names_in_]


    # Prediction
    prediction = model.predict(input_df)[0]

    # Prediction probability (if supported)
    try:
        probability = model.predict_proba(input_df)[0]
        stay_prob = probability[0] * 100
        leave_prob = probability[1] * 100
    except:
        stay_prob = None
        leave_prob = None

    st.markdown("---")

    st.subheader("🎯 Prediction Result")

    if prediction == 1:

        st.error("## ⚠️ Employee is Likely to Leave")

        risk = "🔴 HIGH RISK"

        recommendation = """
        - Conduct a one-on-one discussion
        - Review salary and benefits
        - Improve employee engagement
        - Consider career growth opportunities
        """

    else:

        st.success("## ✅ Employee is Likely to Stay")

        risk = "🟢 LOW RISK"

        recommendation = """
        - Continue employee engagement
        - Recognize good performance
        - Provide leadership opportunities
        - Encourage career development
        """

    # ===========================================
    # DASHBOARD METRICS
    # ===========================================

    if prediction == 1:
        prediction_text = "🔴 Leave"
    else:
        prediction_text = "🟢 Stay"

    if stay_prob is not None:
        confidence = max(stay_prob, leave_prob)
    else:
        confidence = 0

    card1, card2, card3, card4 = st.columns(4)

    with card1:
        st.metric(
            "👤 Employee",
            EmployeeName if EmployeeName else "N/A"
        )

    with card2:
        st.metric(
            "🎯 Prediction",
            prediction_text
        )

    with card3:
        st.metric(
            "⚠ Risk",
            risk
        )

    with card4:
        st.metric(
            "📊 Confidence",
            f"{confidence:.2f}%"
        )
    if stay_prob is not None:

        with st.expander("📊 Prediction Probability"):

            st.write(f"🟢 Stay : {stay_prob:.2f}%")
            st.progress(stay_prob / 100)

            st.write(f"🔴 Leave : {leave_prob:.2f}%")
            st.progress(leave_prob / 100)

    st.markdown("### 💡 HR Recommendation")

    st.info(recommendation)
    # ===========================================
    # DOWNLOAD REPORT
    # ===========================================

    report = f"""
    EMPLOYEE RETENTION PREDICTION REPORT

    Generated On:
    {datetime.now().strftime("%d-%m-%Y %I:%M %p")}

    --------------------------------------------

    Employee Name : {EmployeeName}

    Employee ID : {EmployeeID}

    Designation : {Designation}

    --------------------------------------------

    Prediction : {prediction_text}

    Risk Level : {risk}

    Confidence : {confidence:.2f}%

    Stay Probability : {stay_prob:.2f}%

    Leave Probability : {leave_prob:.2f}%

    --------------------------------------------

    HR Recommendation

    {recommendation}

    --------------------------------------------

    Employee Retention Predictor
    Developed by Bhuvana
    """
    st.download_button(
        label="📄 Download Prediction Report",
        data=report,
        file_name=f"{EmployeeID}_Prediction_Report.txt",
        mime="text/plain",
        use_container_width=True
    )

st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray;'>

<b>Developed by Bhuvana</b><br>

Employee Retention Predictor using Machine Learning

</div>
""", unsafe_allow_html=True)