import random
from datetime import datetime

import streamlit as st
from streamlit.components.v1 import html

MEET_TIME = datetime(2026, 4, 30, 8, 15, 0)

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
    /* Hide Streamlit chrome elements (header/toolbar/footer). */
    header[data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    [data-testid="stSidebarNav"],
    [data-testid="stAppDeployButton"],
    [data-testid="stAppGitHubButton"],
    footer {
        display: none !important;
    }
    [data-testid="stAppViewContainer"] {
        padding-top: 0 !important;
    }
    .main {
        padding-top: 0 !important;
    }
    .block-container {
        max-width: 760px;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    .main .block-container {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .headline {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }
    .subline {
        text-align: center;
        opacity: 0.95;
        margin-bottom: 1.3rem;
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
        margin-top: 1.15rem;
        border-radius: 16px;
        padding: 0.95rem 1rem;
        background: rgba(255, 255, 255, 0.11);
        border-left: 4px solid #ff8fd8;
        font-size: 1rem;
    }
    .stButton {
        margin-top: 1rem;
        margin-bottom: 0.4rem;
    }
    [data-testid="column"] {
        padding-bottom: 0.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
html(
    """
    <script>
      (function () {
        const hideBottomRight = () => {
          const doc = window.parent.document;
          doc.querySelectorAll("*").forEach((el) => {
            const s = window.parent.getComputedStyle(el);
            if (s.position === "fixed") {
              const right = parseInt(s.right || "9999", 10);
              const bottom = parseInt(s.bottom || "9999", 10);
              if (right <= 48 && bottom <= 48) el.style.display = "none";
            }
          });
        };
        hideBottomRight();
        setInterval(hideBottomRight, 1200);
      })();
    </script>
    """,
    height=0,
)

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
