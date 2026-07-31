import os
import uuid
from datetime import datetime

import streamlit as st

from styles import load_css
from voices import VOICE_OPTIONS
from utils import (
    text_to_speech,
    estimate_duration
)
from transcriber import speech_to_text


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Neural Text ↔️ Speech AI Toolkit",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    load_css(),
    unsafe_allow_html=True
)


# ==========================================================
# PROJECT DIRECTORIES
# ==========================================================

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "generated_audio"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==========================================================
# SESSION STATE
# ==========================================================

DEFAULT_STATE = {

    "history": [],

    "generated_audio": None,

    "generated_filename": "",

    "transcript": "",

    "language": "English",

    "voice": list(
        VOICE_OPTIONS["English"].keys()
    )[0],

    "speed": 1.0,

    "input_text": ""

}

for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ==========================================================
# COMPACT HEADER BAR (replaces sidebar - fully horizontal)
# ==========================================================

logo_col, title_col, badge_col, stat_col = st.columns(
    [0.6, 3, 2, 2]
)

with logo_col:

    st.image(
        "assets/logo.png",
        width=60
    )

with title_col:

    st.markdown(
        "<h1 style='margin-bottom:0;'>🧠 Neural Text ↔️ Speech AI Toolkit</h1>"
        "<p style='margin-top:0;color:#4B5563;font-size:0.85rem;'>"
        "AI Powered Voice Generation & Speech Recognition"
        "</p>",
        unsafe_allow_html=True
    )

with badge_col:

    b1, b2 = st.columns(2)

    with b1:

        st.success("✅ Edge Neural TTS")

    with b2:

        st.info("🎧 Faster Whisper")

with stat_col:

    s1, s2, s3 = st.columns(3)

    with s1:

        st.metric("Languages", len(VOICE_OPTIONS))

    with s2:

        st.metric(
            "Voices",
            sum(len(v) for v in VOICE_OPTIONS.values())
        )

    with s3:

        st.metric("Generated", len(st.session_state.history))

st.divider()


# ==========================================================
# TABS
# ==========================================================

voice_tab, speech_tab = st.tabs(
[
    "🎙 Text → Speech",

    "🎤 Speech → Text"
]
)

# ==========================================================
# TEXT → SPEECH (fully horizontal: input | settings | analytics)
# ==========================================================

with voice_tab:

    left_col, mid_col, right_col = st.columns([2.2, 1.3, 1.3])

    # ------------------------------------------------------
    # LEFT PANEL - INPUT
    # ------------------------------------------------------

    with left_col:

        st.subheader("📝 Enter Your Text")

        text = st.text_area(
            "Input Text",
            key="input_text",
            placeholder="Type or paste your text here...",
            height=200,
            label_visibility="collapsed"
        )

        col_btn1, col_btn2 = st.columns(2)

        with col_btn1:

            generate = st.button(
                "🎙 Generate AI Voice",
                use_container_width=True,
                type="primary"
            )

        with col_btn2:

            clear = st.button(
                "🗑 Clear Text",
                use_container_width=True
            )

        if clear:

            st.session_state.input_text = ""

            st.rerun()

    # ------------------------------------------------------
    # MIDDLE PANEL - VOICE SETTINGS
    # ------------------------------------------------------

    with mid_col:

        st.subheader("⚙ Voice Settings")

        language = st.selectbox(
            "🌍 Language",
            options=list(VOICE_OPTIONS.keys()),
            key="language"
        )

        voice = st.selectbox(
            "🎤 Voice",
            options=list(
                VOICE_OPTIONS[language].keys()
            ),
            key="voice"
        )

        speed = st.slider(
            "🎚 Speech Speed (0.5× - 2.0×)",
            min_value=0.50,
            max_value=2.00,
            value=st.session_state.speed,
            step=0.05,
            key="speed"
        )

    # ------------------------------------------------------
    # RIGHT PANEL - ANALYTICS
    # ------------------------------------------------------

    with right_col:

        st.subheader("📊 Voice Analytics")

        a1, a2, a3 = st.columns(3)

        with a1:

            st.metric("Chars", len(text))

        with a2:

            st.metric("Words", len(text.split()))

        with a3:

            st.metric("Dur (s)", estimate_duration(text))

        st.caption(
            f"🌍 **{language}** &nbsp;|&nbsp; 🎤 **{voice}** &nbsp;|&nbsp; "
            f"⚡ **{speed:.2f}×**"
        )

# ==========================================================
# GENERATE AI VOICE
# ==========================================================

    if generate:

        if not text.strip():

            st.warning(
                "Please enter some text before generating the voice."
            )

        else:

            with st.spinner("Generating AI Voice..."):

                selected_voice = VOICE_OPTIONS[
                    language
                ][
                    voice
                ]

                audio_file = text_to_speech(
                    text=text,
                    voice=selected_voice,
                    speed=speed
                )

            st.session_state.generated_audio = audio_file

            st.session_state.generated_filename = os.path.basename(
                audio_file
            )

            st.session_state.history.append(

                {

                    "language": language,

                    "voice": voice,

                    "speed": speed,

                    "time": datetime.now().strftime(
                        "%I:%M %p"
                    ),

                    "file": audio_file

                }

            )

            st.success(
                "✅ AI Voice Generated Successfully!"
            )


    # ==========================================================
    # AUDIO PLAYER + HISTORY - one horizontal row
    # ==========================================================

    if st.session_state.generated_audio or len(st.session_state.history) > 0:

        st.divider()

        player_col, history_col = st.columns([2, 1])

        with player_col:

            if st.session_state.generated_audio:

                st.subheader("🎧 Audio Preview")

                p1, p2 = st.columns([3, 1])

                with p1:

                    st.audio(
                        st.session_state.generated_audio,
                        format="audio/mp3"
                    )

                with p2:

                    with open(
                        st.session_state.generated_audio,
                        "rb"
                    ) as audio:

                        st.download_button(

                            label="⬇ Download",

                            data=audio,

                            file_name=st.session_state.generated_filename,

                            mime="audio/mpeg",

                            key="generated_audio_download",

                            use_container_width=True

                        )

        with history_col:

            if len(st.session_state.history) > 0:

                with st.expander(
                    f"📜 Generation History ({len(st.session_state.history)})",
                    expanded=False
                ):

                    if st.button(
                        "🗑 Clear History",
                        use_container_width=True,
                        key="clear_history_btn"
                    ):

                        st.session_state.history.clear()

                        st.rerun()

                    for index, item in enumerate(

                        reversed(
                            st.session_state.history
                        )

                    ):

                        st.write(
                            f"🎙 **{item['voice']}** ({item['language']}) "
                            f"• ⚡{item['speed']:.2f}× • {item['time']}"
                        )

                        with open(
                            item["file"],
                            "rb"
                        ) as audio:

                            st.download_button(

                                label="⬇ Download Again",

                                data=audio,

                                file_name=os.path.basename(
                                    item["file"]
                                ),

                                mime="audio/mpeg",

                                key=f"history_download_{index}",

                                use_container_width=True

                            )

# ==========================================================
# SPEECH → TEXT
# ==========================================================

with speech_tab:

    left_col, right_col = st.columns([1, 2])

    # ------------------------------------------------------
    # LEFT PANEL
    # ------------------------------------------------------

    with left_col:

        st.subheader("🎤 Upload Audio")

        uploaded_audio = st.file_uploader(

            "Choose an audio file",

            type=[
                "mp3",
                "wav",
                "m4a",
                "ogg",
                "flac"
            ],

            label_visibility="collapsed"
        )

        if uploaded_audio:

            filename = (
                f"{uuid.uuid4().hex}_"
                f"{uploaded_audio.name}"
            )

            save_path = os.path.join(
                UPLOAD_DIR,
                filename
            )

            with open(
                save_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_audio.read()
                )

            st.audio(save_path)

            transcribe = st.button(

                "🎤 Start Transcription",

                use_container_width=True,

                type="primary"
            )

        else:

            transcribe = False

    # ------------------------------------------------------
    # RIGHT PANEL
    # ------------------------------------------------------

    with right_col:

        st.subheader(
            "📝 AI Transcript"
        )

        if uploaded_audio and transcribe:

            with st.spinner(

                "Transcribing audio..."

            ):

                st.session_state.transcript = speech_to_text(

                    save_path

                )

        st.text_area(

            "Transcript",

            value=st.session_state.transcript,

            height=200,

            label_visibility="collapsed"
        )

        c1, c2, c3, c4 = st.columns([1.3, 1, 1, 1.6])

        with c1:

            st.download_button(

                label="⬇ Download Transcript",

                data=st.session_state.transcript,

                file_name="transcript.txt",

                mime="text/plain",

                key="download_transcript",

                disabled=(
                    st.session_state.transcript == ""
                ),

                use_container_width=True

            )

        with c2:

            if st.button(

                "🗑 Clear",

                use_container_width=True

            ):

                st.session_state.transcript = ""

                st.rerun()

        with c3:

            st.metric(

                "Words",

                len(

                    st.session_state.transcript.split()

                )

            )

        with c4:

            st.caption(

                f"Characters: {len(st.session_state.transcript)}  |  "
                f"Reading Time: "
                f"{max(1, len(st.session_state.transcript.split())//180)} min"

            )