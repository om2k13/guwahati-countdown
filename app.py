import random
from datetime import datetime

import streamlit as st

MEET_TIME = datetime(2026, 4, 30, 8, 15, 0)
COUNTDOWN_START = datetime(2026, 4, 24, 14, 0, 0)

ROMANTIC_FUNNY_LINES = [
    "Every second without you is suspiciously longer than normal physics allows.",
    "I miss you so much even my coffee tastes emotionally unavailable.",
    "Countdown update: my heart has filed a formal complaint about the distance.",
    "I tried being chill, but my love for you has zero chill settings.",
    "Scientists discovered a new force: me being pulled toward you constantly.",
    "If kisses were Wi-Fi, I would already be fully connected to you.",
    "You are my favorite notification, even when my phone is on silent.",
    "The stars are pretty, but they still lose to your smile by a lot.",
    "My daily cardio is running through memories of you.",
    "Roses are red, time is slow, hurry up universe, I need my girl now.",
    "I would wait a thousand lifetimes, but I still keep checking the timer.",
    "Love status: 100 percent yours, no updates required, lifetime subscription active.",
]

st.set_page_config(page_title="Omkar + Illia", page_icon="💖", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(140deg, #12071f 0%, #2d103c 45%, #5c1d5d 100%);
        color: #fff6fc;
    }
    .main-card {
        border-radius: 24px;
        padding: 1.2rem 1.4rem 1.4rem;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(4px);
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }
    .headline {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .subline {
        text-align: center;
        opacity: 0.95;
        margin-bottom: 1rem;
        font-size: 1.05rem;
    }
    .mini-title {
        text-align: center;
        opacity: 0.85;
        margin-top: 0.7rem;
        margin-bottom: 0.35rem;
    }
    .time-box {
        text-align: center;
        border-radius: 18px;
        padding: 0.8rem 0.4rem;
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .time-number {
        font-size: 1.9rem;
        font-weight: 700;
        line-height: 1.1;
    }
    .time-label {
        opacity: 0.85;
        font-size: 0.9rem;
        letter-spacing: 0.04em;
    }
    .line-card {
        margin-top: 1rem;
        border-radius: 16px;
        padding: 0.95rem 1rem;
        background: rgba(255, 255, 255, 0.11);
        border-left: 4px solid #ff8fd8;
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="headline">Omkar ❤️ Illia</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subline">Time left for us to meet</div>',
    unsafe_allow_html=True,
)

if "last_line" not in st.session_state:
    st.session_state["last_line"] = random.choice(ROMANTIC_FUNNY_LINES)


@st.fragment(run_every="1s")
def render_live_countdown() -> None:
    now = datetime.now()
    diff = MEET_TIME - now

    if diff.total_seconds() > 0:
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(
                f'<div class="time-box"><div class="time-number">{days}</div><div class="time-label">DAYS</div></div>',
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f'<div class="time-box"><div class="time-number">{hours}</div><div class="time-label">HOURS</div></div>',
                unsafe_allow_html=True,
            )
        with col3:
            st.markdown(
                f'<div class="time-box"><div class="time-number">{minutes}</div><div class="time-label">MINUTES</div></div>',
                unsafe_allow_html=True,
            )
        with col4:
            st.markdown(
                f'<div class="time-box"><div class="time-number">{seconds}</div><div class="time-label">SECONDS</div></div>',
                unsafe_allow_html=True,
            )

        total_wait_seconds = max((MEET_TIME - COUNTDOWN_START).total_seconds(), 1)
        remaining_seconds = max((MEET_TIME - now).total_seconds(), 0)
        progress = max(0.0, min(1.0, 1 - (remaining_seconds / total_wait_seconds)))

        st.markdown('<div class="mini-title">Love Bar</div>', unsafe_allow_html=True)
        st.progress(progress)

        if st.button("Give me a new love line 💌", use_container_width=True):
            previous_line = st.session_state.get("last_line", "")
            available_lines = [line for line in ROMANTIC_FUNNY_LINES if line != previous_line]
            st.session_state["last_line"] = random.choice(
                available_lines if available_lines else ROMANTIC_FUNNY_LINES
            )

        st.markdown(
            f'<div class="line-card">{st.session_state["last_line"]}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.balloons()
        st.success("It is finally our moment. I am all yours. ❤️")


render_live_countdown()

st.markdown("</div>", unsafe_allow_html=True)
