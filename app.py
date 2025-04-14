import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page layout to wide
st.set_page_config(page_title="Growth Mindset Tracker", layout="wide")

# Header with image and title
st.image("https://images.unsplash.com/photo-1593642532973-d31b6557fa68", use_container_width=True)
st.title("🌱 Growth Mindset Tracker 🌱")
st.write("""
    Welcome to the Growth Mindset Tracker! 🌟  
    This app helps you track your progress, reflect on challenges, and celebrate your learning journey.
    Remember, every step counts, whether big or small!
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a Section",
    ["Growth Mindset Challenges", "Track Your Goals", "Progress Tracker", "Reflection Log"]
)

# Daily Growth Mindset Challenge
if option == "Growth Mindset Challenges":
    st.subheader("Daily Growth Mindset Challenge")
    
    challenges = [
        "Embrace a challenge today—what’s one task you’ve been avoiding?",
        "Think about a recent mistake—what can you learn from it?",
        "Celebrate one effort you made today, no matter how small.",
        "Identify one area you want to improve and set a goal for it.",
        "Help someone else overcome a challenge today."
    ]
    
    challenge = random.choice(challenges)
    st.write(f"**Today's Challenge:** {challenge}")
    
    st.write("**Tip:** Write down the challenge in your journal and reflect on it later.")
    # st.image("https://images.unsplash.com/photo-1506748686219-c7d839738477", caption="Keep pushing your limits! 💪", use_container_width=True)
    st.image("https://media.istockphoto.com/id/536094835/photo/silhouette-of-helping-hand-between-two-climber.jpg?s=612x612&w=0&k=20&c=HdvyUSxYPbMhvFNd-nrqyN_yP_2YZUzBeddoHUw_kD4=", caption="Keep pushing your limits! 💪", use_container_width=True)


# Track Your Learning Goals
elif option == "Track Your Goals":
    st.subheader("Set and Track Your Learning Goals 📚")
    
    goal = st.text_input("What is your learning goal for today?")
    if goal:
        st.write(f"🌟 **Goal for Today:** {goal}")
    
    progress = st.slider("How much progress have you made today?", 0, 100, 0)
    if progress:
        st.write(f"✅ **Your progress:** {progress}%")
        
    if st.button("Submit Progress"):
        st.success("Goal and progress submitted! Keep going!")
        
    st.subheader("Progress Visualization 📊")
    data = {
        "Days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Progress": [random.randint(0, 100) for _ in range(7)]
    }
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="Days", y="Progress", data=df, marker="o", color="green")
    plt.title("Your Weekly Progress")
    st.pyplot(plt)

# Reflection Log
elif option == "Reflection Log":
    st.subheader("Reflect on Your Mistakes and Learn from Them 💡")
    
    mistake = st.text_area("What mistake did you make today, and how did you learn from it?")
    if mistake:
        st.write(f"**Reflection:** {mistake}")
    
    st.write("**Tip:** Mistakes are proof that you're trying! Keep learning, keep growing! 🌱")
    st.write("_“The only way to fail is to quit trying.”_ — Unknown")

# Progress Tracker
elif option == "Progress Tracker":
    st.subheader("Track Your Learning Journey 📈")
    
    st.write("Here's a detailed graph of your growth over time!")
    st.write("Each bar represents your weekly growth.")

    data = {
        "Week": [f"Week {i}" for i in range(1, 11)],
        "Progress": [random.randint(50, 100) for _ in range(10)]
    }
    df = pd.DataFrame(data)
    
    st.bar_chart(df.set_index('Week')['Progress'])
    
    st.write("🌟 **Tip:** Consistent effort leads to big results. Keep pushing yourself forward!")

# Footer with image and motivational message
st.sidebar.write("💡 Remember, a growth mindset is about learning, evolving, and overcoming obstacles. Keep going, you've got this! 🚀")
st.sidebar.image("https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=800&q=60", 
                 caption="Believe in yourself! 🌈", use_container_width=True)
st.sidebar.write("Made with ❤️ by [SAHAR]")