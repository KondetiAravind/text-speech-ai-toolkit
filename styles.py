def load_css():
    return """
<style>

/* ==========================================================
   GOOGLE FONT
========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html,
body,
[class*="css"]{
    font-family:'Poppins',sans-serif;
}


/* ==========================================================
   MAIN PAGE - NO SCROLL, FIT SCREEN
========================================================== */

html, body{
    overflow:hidden !important;
    height:100vh;
}

.stApp{

    background:#F5F7FB;

    color:#111827;

    height:100vh;

    overflow:hidden;

}


/* ==========================================================
   REMOVE STREAMLIT DEFAULTS
========================================================== */

#MainMenu{

    visibility:hidden;

}

footer{

    visibility:hidden;

}

header{

    visibility:hidden;

}

section[data-testid="stSidebar"]{

    display:none !important;

}


/* ==========================================================
   PAGE WIDTH / HEIGHT (compact so it fits one screen)
========================================================== */

.block-container{

    max-width:1600px;

    padding-top:0.6rem;

    padding-bottom:0.4rem;

    padding-left:1.2rem;

    padding-right:1.2rem;

}


/* ==========================================================
   HEADINGS (kept smaller/compact)
========================================================== */

h1{

    color:#111827 !important;

    font-weight:700 !important;

    font-size:1.5rem !important;

}

h2{

    color:#111827 !important;

    font-weight:700 !important;

    font-size:1.2rem !important;

}

h3{

    color:#1F2937 !important;

    font-weight:600 !important;

    font-size:1.05rem !important;

}

h4{

    color:#374151 !important;

}


/* ==========================================================
   NORMAL TEXT
   (scoped to markdown/body text only - NOT buttons,
   which was the bug causing invisible button text)
========================================================== */

.stMarkdown p,
[data-testid="stCaptionContainer"] p{

    color:#374151 !important;

}

label{

    color:#111827 !important;

    font-weight:600 !important;

}


/* ==========================================================
   TABS
========================================================== */

.stTabs [data-baseweb="tab-list"]{

    gap:8px;

}

.stTabs [data-baseweb="tab"]{

    background:#EEF2FF;

    color:#374151 !important;

    border-radius:10px;

    padding:6px 16px;

    font-weight:600;

}

.stTabs [data-baseweb="tab"] p{

    color:#374151 !important;

}

.stTabs [aria-selected="true"]{

    background:#4F46E5;

}

.stTabs [aria-selected="true"] p{

    color:#FFFFFF !important;

}


/* ==========================================================
   BUTTON - force white text on every child element
   (fixes the invisible/low-contrast button text bug)
========================================================== */

.stButton>button{

    width:100%;

    border:none;

    border-radius:10px;

    padding:0.5rem;

    background:#4F46E5;

    color:#FFFFFF !important;

    font-weight:600;

    transition:.2s;

}

.stButton>button *{

    color:#FFFFFF !important;

}

.stButton>button:hover{

    background:#4338CA;

}

.stButton>button:hover *{

    color:#FFFFFF !important;

}


/* ==========================================================
   DOWNLOAD BUTTON - same fix
========================================================== */

.stDownloadButton>button{

    width:100%;

    border:none;

    border-radius:10px;

    background:#2563EB;

    color:#FFFFFF !important;

    font-weight:600;

}

.stDownloadButton>button *{

    color:#FFFFFF !important;

}

.stDownloadButton>button:hover{

    background:#1D4ED8;

}

.stDownloadButton>button:hover *{

    color:#FFFFFF !important;

}


/* ==========================================================
   TEXT AREA (compact height for no-scroll fit)
========================================================== */

textarea{

    background:#FFFFFF !important;

    color:#111827 !important;

    border:2px solid #D1D5DB !important;

    border-radius:12px !important;

    font-size:14px !important;

}

textarea::placeholder{

    color:#9CA3AF !important;

}


/* ==========================================================
   INPUT BOXES
========================================================== */

input{

    color:#111827 !important;

}


/* ==========================================================
   SELECT BOX
========================================================== */

div[data-baseweb="select"]>div{

    background:white;

    color:#111827 !important;

    border-radius:10px;

    border:1px solid #D1D5DB;

}

div[data-baseweb="select"] *{

    color:#111827 !important;

}


/* ==========================================================
   METRIC CARDS (compact)
========================================================== */

div[data-testid="metric-container"]{

    background:white;

    border:1px solid #E5E7EB;

    border-radius:12px;

    padding:8px;

    box-shadow:0 1px 4px rgba(0,0,0,.05);

}

div[data-testid="stMetricValue"]{

    color:#111827 !important;

    font-size:1.3rem !important;

}

div[data-testid="stMetricLabel"]{

    color:#4B5563 !important;

}


/* ==========================================================
   AUDIO PLAYER
========================================================== */

audio{

    width:100%;

    border-radius:10px;

    height:36px;

}


/* ==========================================================
   ALERTS
========================================================== */

.stSuccess, .stSuccess *{

    border-radius:10px;

    color:#065F46 !important;

}

.stWarning, .stWarning *{

    border-radius:10px;

    color:#92400E !important;

}

.stInfo, .stInfo *{

    border-radius:10px;

    color:#1E3A8A !important;

}


/* ==========================================================
   HORIZONTAL LINE (thinner, less vertical space)
========================================================== */

hr{

    border-color:#E5E7EB;

    margin:0.5rem 0 !important;

}


/* ==========================================================
   SCROLLBAR
========================================================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#CBD5E1;

    border-radius:20px;

}


/* ==========================================================
   IMAGE
========================================================== */

img{

    border-radius:14px;

}


/* ==========================================================
   CAPTION
========================================================== */

.caption, [data-testid="stCaptionContainer"]{

    color:#6B7280 !important;

}


/* ==========================================================
   HIDE DEPLOY BUTTON
========================================================== */

button[kind="header"]{

    display:none;

}


/* ==========================================================
   EXPANDER (history) - compact
========================================================== */

.streamlit-expanderHeader, [data-testid="stExpander"] summary{

    color:#111827 !important;

    font-weight:600;

}

</style>
"""