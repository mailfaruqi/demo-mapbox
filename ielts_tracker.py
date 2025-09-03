import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, date
import json
import random

# Page configuration
st.set_page_config(
    page_title="IELTS Progress Tracker 🎯",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark blue theme with energy vibes
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f1419 0%, #1a365d 50%, #2d5a87 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a365d 50%, #2d5a87 100%);
    }
    
    .metric-card {
        background: linear-gradient(145deg, #1e3a5f, #2d5a87);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #4a90e2;
        box-shadow: 0 8px 32px rgba(74, 144, 226, 0.3);
        margin: 10px 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 8px 32px rgba(74, 144, 226, 0.3); }
        50% { box-shadow: 0 12px 40px rgba(74, 144, 226, 0.5); }
        100% { box-shadow: 0 8px 32px rgba(74, 144, 226, 0.3); }
    }
    
    .countdown-box {
        background: linear-gradient(145deg, #ff6b6b, #ee5a52);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4);
        animation: glow 3s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4); }
        to { box-shadow: 0 15px 40px rgba(255, 107, 107, 0.8); }
    }
    
    .quote-box {
        background: linear-gradient(145deg, #4ecdc4, #44b3aa);
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-style: italic;
        font-size: 18px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(78, 205, 196, 0.3);
        border-left: 5px solid #ffffff;
    }
    
    .energy-title {
        background: linear-gradient(45deg, #4a90e2, #50c9c3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e3a5f, #2d5a87);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'listening': [],
        'reading': [],
        'writing': [],
        'speaking': []
    }

if 'target_date' not in st.session_state:
    st.session_state.target_date = date(2025, 11, 1)

# Motivational quotes
quotes = [
    "Success is the sum of small efforts, repeated day in and day out. 💪",
    "Every expert was once a beginner. Keep practicing! 🌟",
    "Your limitation—it's only your imagination. Break through! 🚀",
    "Push yourself, because no one else is going to do it for you. 💯",
    "Great things never come from comfort zones. Step up! ⚡",
    "Dream it. Wish it. Do it. Achieve your IELTS goals! 🎯",
    "The harder you work for something, the greater you'll feel when you achieve it. 🏆",
    "Success doesn't just find you. You have to go out and get it. 🔥",
    "Don't stop when you're tired. Stop when you're done! 💪",
    "Wake up with determination. Go to bed with satisfaction. 🌅"
]

# Functions
def calculate_days_left():
    today = date.today()
    days_left = (st.session_state.target_date - today).days
    return max(0, days_left)

def get_daily_quote():
    # Use date as seed for consistent daily quote
    random.seed(date.today().toordinal())
    return random.choice(quotes)

def add_score(test_type, score, test_date):
    st.session_state.scores[test_type].append({
        'date': test_date.strftime('%Y-%m-%d'),
        'score': score
    })

def create_progress_chart(test_type):
    if not st.session_state.scores[test_type]:
        return None
    
    data = st.session_state.scores[test_type]
    dates = [item['date'] for item in data]
    scores = [item['score'] for item in data]
    
    fig = go.Figure()
    
    # Add line trace
    fig.add_trace(go.Scatter(
        x=dates,
        y=scores,
        mode='lines+markers',
        name=f'{test_type.title()} Scores',
        line=dict(color='#4a90e2', width=3),
        marker=dict(size=10, color='#50c9c3')
    ))
    
    # Add target line at 7.0
    fig.add_hline(y=7.0, line_dash="dash", line_color="red", 
                  annotation_text="Target: 7.0")
    
    fig.update_layout(
        title=f'{test_type.title()} Progress',
        xaxis_title='Date',
        yaxis_title='Score',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        yaxis=dict(range=[0, 9]),
        height=400
    )
    
    return fig

def get_latest_score(test_type):
    if st.session_state.scores[test_type]:
        return st.session_state.scores[test_type][-1]['score']
    return 0

def get_average_score(test_type):
    if st.session_state.scores[test_type]:
        scores = [item['score'] for item in st.session_state.scores[test_type]]
        return round(sum(scores) / len(scores), 1)
    return 0

# Main App
st.markdown('<h1 class="energy-title">🎯 IELTS Progress Tracker 🚀</h1>', unsafe_allow_html=True)

# Countdown Timer
days_left = calculate_days_left()
st.markdown(f'''
<div class="countdown-box">
    🔥 {days_left} DAYS LEFT TO IELTS EXAM 🔥<br>
    <small>Target Date: {st.session_state.target_date.strftime("%B %d, %Y")}</small>
</div>
''', unsafe_allow_html=True)

# Daily Quote
st.markdown(f'''
<div class="quote-box">
    💫 Quote of the Day 💫<br>
    "{get_daily_quote()}"
</div>
''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Sidebar for adding scores
st.sidebar.markdown("## 📝 Add New Score")

test_type = st.sidebar.selectbox(
    "Select Test Type",
    ['listening', 'reading', 'writing', 'speaking']
)

score = st.sidebar.slider(
    "Score",
    min_value=0.0,
    max_value=9.0,
    value=5.0,
    step=0.5
)

test_date = st.sidebar.date_input(
    "Test Date",
    value=date.today()
)

if st.sidebar.button("➕ Add Score", type="primary"):
    add_score(test_type, score, test_date)
    st.sidebar.success(f"Added {test_type} score: {score}")

# Option to change target date
st.sidebar.markdown("---")
st.sidebar.markdown("## 🎯 Target Settings")
new_target = st.sidebar.date_input(
    "IELTS Exam Date",
    value=st.session_state.target_date
)

if st.sidebar.button("Update Target Date"):
    st.session_state.target_date = new_target
    st.sidebar.success("Target date updated!")

# Main dashboard
col1, col2, col3, col4 = st.columns(4)

# Display current scores
test_types = ['listening', 'reading', 'writing', 'speaking']
colors = ['#4a90e2', '#50c9c3', '#ff6b6b', '#ffd93d']

for i, (test, color) in enumerate(zip(test_types, colors)):
    with [col1, col2, col3, col4][i]:
        latest = get_latest_score(test)
        average = get_average_score(test)
        total_tests = len(st.session_state.scores[test])
        
        st.markdown(f'''
        <div class="metric-card">
            <h3 style="color: {color}; margin-bottom: 10px;">
                {test.title()} 📊
            </h3>
            <div style="font-size: 28px; font-weight: bold; color: white;">
                {latest if latest > 0 else "N/A"}
            </div>
            <div style="color: #b0b0b0; margin-top: 5px;">
                Avg: {average if average > 0 else "N/A"} | Tests: {total_tests}
            </div>
        </div>
        ''', unsafe_allow_html=True)

# Progress Charts
st.markdown("## 📈 Progress Charts")

# Create tabs for each test type
tab1, tab2, tab3, tab4 = st.tabs(['🎧 Listening', '📖 Reading', '✍️ Writing', '🗣️ Speaking'])

tabs = [tab1, tab2, tab3, tab4]

for i, (tab, test) in enumerate(zip(tabs, test_types)):
    with tab:
        chart = create_progress_chart(test)
        if chart:
            st.plotly_chart(chart, use_container_width=True)
        else:
            st.info(f"No {test} scores recorded yet. Add some scores to see your progress!")

# Overall Progress Summary
st.markdown("## 🎯 Overall Summary")

col1, col2 = st.columns(2)

with col1:
    # Calculate overall average
    all_scores = []
    for test in test_types:
        if st.session_state.scores[test]:
            scores = [item['score'] for item in st.session_state.scores[test]]
            all_scores.extend(scores)
    
    overall_avg = round(sum(all_scores) / len(all_scores), 1) if all_scores else 0
    total_tests = sum(len(st.session_state.scores[test]) for test in test_types)
    
    st.markdown(f'''
    <div class="metric-card">
        <h3 style="color: #4a90e2;">🏆 Overall Performance</h3>
        <div style="font-size: 32px; font-weight: bold; color: white; margin: 15px 0;">
            {overall_avg if overall_avg > 0 else "N/A"}
        </div>
        <div style="color: #b0b0b0;">
            Total Tests Completed: {total_tests}
        </div>
        <div style="color: #50c9c3; margin-top: 10px;">
            {"🔥 You're on fire! Keep going!" if overall_avg >= 7 else "💪 Keep pushing! You're getting there!" if overall_avg >= 6 else "📚 Focus and practice more!"}
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    # Study streak and motivation
    st.markdown(f'''
    <div class="metric-card">
        <h3 style="color: #ff6b6b;">⚡ Energy Boost</h3>
        <div style="color: white; font-size: 18px; line-height: 1.6;">
            🎯 Target: Band 7.0+<br>
            📅 Days to go: {days_left}<br>
            💪 Tests done: {total_tests}<br>
            🚀 {"Almost there!" if overall_avg >= 6.5 else "Keep grinding!" if overall_avg >= 5.5 else "Start strong!"}
        </div>
    </div>
    ''', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #b0b0b0; padding: 20px;">
    💪 Built for IELTS Warriors | Keep practicing, keep improving! 🚀
</div>
""", unsafe_allow_html=True)
