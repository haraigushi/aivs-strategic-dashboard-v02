import streamlit as st
import plotly.graph_objects as go
import random

# --- Set up page ---
st.set_page_config(page_title="AIVS Strategic Dashboard", layout="wide")

# --- Header / Hero ---
st.markdown("""
    <style>
        .header-container {
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f4f4f8, #e0e6ed);
            padding: 30px 20px;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }

        .header-container h1 {
            font-size: 2.5em;
            color: #1a1a2e;
            margin-bottom: 10px;
        }

        .header-container p {
            font-size: 1.1em;
            color: #4a4a4a;
            font-style: italic;
            margin-bottom: 0;
        }

        hr {
            border: none;
            height: 2px;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            margin: 30px auto;
            width: 80%;
            border-radius: 5px;
        }
    </style>

    <div class="header-container">
        <h1>AIVS Strategic Dashboard</h1>
        <p>Prepared by: Strategic Advisor (Saleh Zareei)</p>
    </div>
""", unsafe_allow_html=True)

# --- KPIs Setup ---
kpis = {
    "Assemble Strategy Unit": {
        "desc": "Hire 2–4 additional members including a COO to help operationalize execution.",
        "example": "E.g. 3 new hires including a COO.",
        "value": random.randint(1, 3),
        "total": 4,
        "color": "blue"
    },
    "Product Audit": {
        "desc": "Evaluate readiness, differentiation, and market alignment of 6 internal projects.",
        "example": "E.g. 2 projects evaluated for market readiness.",
        "value": random.randint(1, 3),
        "total": 6,
        "color": "green"
    },
    "Directory Development": {
        "desc": "Populate an internal directory of employee skills, resumes, and capabilities.",
        "example": "E.g. 3 employee profiles completed.",
        "value": random.randint(1, 4),
        "total": 4,
        "color": "orange"
    },
    "Pilot Launch": {
        "desc": "Launch 2–3 most viable projects in Iran.",
        "example": "E.g. 2 pilot products launched in Iran.",
        "value": random.randint(1, 2),
        "total": 3,
        "color": "purple"
    },
    "VC Funnel Prioritization": {
        "desc": "Categorize 240 venture proposals into kill, incubate, or fast-track.",
        "example": "E.g. 80 proposals processed.",
        "value": random.randint(10, 100),
        "total": 240,
        "color": "red"
    },
    "Brand Positioning": {
        "desc": "Define AIVS's core brand messaging and value proposition.",
        "example": "E.g. Brand message finalized and presented.",
        "value": random.randint(1, 2),
        "total": 2,
        "color": "pink"
    },
    # Phase 2 KPIs
    "Industry Partnerships": {
        "desc": "Secure 3–5 pilot clients (B2B) in petrochemical, steel, education sectors.",
        "example": "E.g. 2 pilot clients secured.",
        "value": random.randint(1, 5),
        "total": 5,
        "color": "cyan"
    },
    "Product Refinement": {
        "desc": "Use feedback loops from pilots to iterate rapidly.",
        "example": "E.g. 2 product iterations completed.",
        "value": random.randint(1, 4),
        "total": 4,
        "color": "orange"
    },
    "Marketing Foundation": {
        "desc": "Build scalable marketing assets (case studies, whitepapers, landing pages).",
        "example": "E.g. 1 whitepaper and 2 landing pages built.",
        "value": random.randint(1, 3),
        "total": 3,
        "color": "purple"
    },
    "Revenue Model Design": {
        "desc": "Define monetization strategies per product type.",
        "example": "E.g. 1 monetization strategy designed for AI products.",
        "value": random.randint(1, 2),
        "total": 2,
        "color": "blue"
    },
    "B2C Opportunities": {
        "desc": "Identify and pilot test at least one product with consumer-facing potential.",
        "example": "E.g. AI-powered learning tool pilot tested.",
        "value": random.randint(0, 1),
        "total": 1,
        "color": "green"
    },
    # Phase 3 KPIs
    "Domestic Expansion": {
        "desc": "Broaden client base across Iran’s industrial and public sectors.",
        "example": "E.g. 2 new clients from public sector.",
        "value": random.randint(1, 4),
        "total": 4,
        "color": "teal"
    },
    "International Soft Launches": {
        "desc": "Test-market in 1–2 other MENA countries.",
        "example": "E.g. Soft launch in UAE and Qatar.",
        "value": random.randint(0, 2),
        "total": 2,
        "color": "violet"
    },
    "Partner Ecosystem": {
        "desc": "Build a partner/reseller network for non-Iranian markets.",
        "example": "E.g. 1 new partnership in the GCC region.",
        "value": random.randint(0, 2),
        "total": 2,
        "color": "yellow"
    },
    "Thought Leadership": {
        "desc": "Establish AIVS as a thought leader in AI-for-industry in MENA.",
        "example": "E.g. 3 keynote speeches at industry events.",
        "value": random.randint(0, 3),
        "total": 3,
        "color": "red"
    }
}

# --- Reusable pie chart builder ---
def build_pie(title, value, total, color, desc, example, key_prefix):
    fig = go.Figure(go.Pie(
        labels=["Completed", "Remaining"],
        values=[value, total - value],
        hole=0.5,
        marker_colors=[color, "#e0e0e0"]
    ))
    
    # Title, description, and example text color match pie chart color
    st.markdown(f"<h3 style='color: {color};'>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {color};'>{desc}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {color};'><i>Example: {example}</i></p>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, key=f"{key_prefix}_{title}_pie")

# --- Reusable dial builder ---
def build_dial(kpi_name, value, total, color, key_prefix):
    st.markdown(f"**{kpi_name}**")
    st.markdown(f"Current value: {value}/{total}")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': kpi_name},
        gauge={'axis': {'range': [0, total]}, 'bar': {'color': color}}
    ))
    st.plotly_chart(fig, use_container_width=True, key=f"{key_prefix}_{kpi_name}_dial")
    new_value = st.number_input(f"Set new value for {kpi_name}", min_value=0, max_value=total, value=value, key=f"{key_prefix}_{kpi_name}_input")
    return new_value

# --- Tab layout ---
tabs = st.tabs(["Executive Summary", "Phase 1: Foundation", "Phase 2: Market", "Phase 3: Scale"])

# --- Tab 1: Executive Summary ---
with tabs[0]:
    st.subheader("Overall KPI Progress")
    cols = st.columns(3)
    keys = list(kpis.keys())
    for i in range(3):
        with cols[i]:
            k = keys[i]
            build_pie(k, **kpis[k], key_prefix="summary")

    cols = st.columns(3)
    for i in range(3, 6):
        with cols[i - 3]:
            k = keys[i]
            build_pie(k, **kpis[k], key_prefix="summary")

    st.markdown('<h3 style="color: red;">🚨 Danger Zone</h3>', unsafe_allow_html=True)
    if kpis["Product Audit"]["value"] < 2:
        st.warning("⚠️ Product audits are behind schedule.")
    if kpis["Brand Positioning"]["value"] < 2:
        st.warning("⚠️ Brand positioning is not finalized.")

    st.markdown("**Suggested Solutions (Peer-reviewed):**")
    st.markdown("""
    1. **Product-Market Fit Refinement**  
       Blank, S. (2013). *Why the Lean Start-Up Changes Everything*. Harvard Business Review.  
       → Focus product iterations directly on real client pain points.

    2. **Internal Knowledge Management Systems**  
       Davenport, T. H., & Prusak, L. (1998). *Working Knowledge: How Organizations Manage What They Know*.  
       → Use metadata tagging and employee-driven profiling to scale skills directory.
    """)

# --- Tab 2: Phase 1 ---
# --- Tab 2: Phase 1 ---
# --- Tab 2: Phase 1 ---
with tabs[1]:
    st.subheader("Phase 1: Foundation (Next 3 Months)")
    st.markdown("🧱 Initial setup of teams, audits, and first pilots.")
    st.info("Includes product audits, COO hire, and first VC funnel analysis.")

    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            k = list(kpis.keys())[i]

            # KPI Title (Underlined and Bolder, matching pie chart color)
            st.markdown(f"**<span style='color: {kpis[k]['color']}; text-decoration: underline; font-weight: bold;'> {k} </span>", unsafe_allow_html=True)

            # Description and Example
            st.markdown(f"**Description:** {kpis[k]['desc']}")
            st.markdown(f"**Example:** {kpis[k]['example']}")

            build_dial(k, kpis[k]["value"], kpis[k]["total"], kpis[k]["color"], key_prefix="phase1")

    cols = st.columns(3)
    for i in range(3, 6):
        with cols[i - 3]:
            k = list(kpis.keys())[i]

            # KPI Title (Underlined and Bolder, matching pie chart color)
            st.markdown(f"**<span style='color: {kpis[k]['color']}; text-decoration: underline; font-weight: bold;'> {k} </span>", unsafe_allow_html=True)

            # Description and Example
            st.markdown(f"**Description:** {kpis[k]['desc']}")
            st.markdown(f"**Example:** {kpis[k]['example']}")

            build_dial(k, kpis[k]["value"], kpis[k]["total"], kpis[k]["color"], key_prefix="phase1")

    st.button("Submit Phase 1 KPIs")

# --- Tab 3: Phase 2 ---
# --- Tab 3: Phase 2 ---
with tabs[2]:
    st.subheader("Phase 2: Market (Next 6 Months)")
    st.markdown("🚀 Focus on scaling and securing strategic market partnerships.")
    st.info("Includes securing new partners, refining products, and expanding sales.")

    cols = st.columns(3)
    for i in range(6, 9):
        with cols[i - 6]:
            k = list(kpis.keys())[i]

            # KPI Title (Underlined and Bolder, matching pie chart color)
            st.markdown(f"**<span style='color: {kpis[k]['color']}; text-decoration: underline; font-weight: bold;'> {k} </span>", unsafe_allow_html=True)

            # Description and Example
            st.markdown(f"**Description:** {kpis[k]['desc']}")
            st.markdown(f"**Example:** {kpis[k]['example']}")

            build_dial(k, kpis[k]["value"], kpis[k]["total"], kpis[k]["color"], key_prefix="phase2")

    st.button("Submit Phase 2 KPIs")

# --- Tab 4: Phase 3 ---
# --- Tab 4: Phase 3 ---
with tabs[3]:
    st.subheader("Phase 3: Scale (Next 12 Months)")
    st.markdown("🌍 Expand into new regions and consolidate partnerships.")
    st.info("Includes expanding into MENA, soft launches, and thought leadership efforts.")

    cols = st.columns(3)
    for i in range(9, 12):
        with cols[i - 9]:
            k = list(kpis.keys())[i]

            # KPI Title (Underlined and Bolder, matching pie chart color)
            st.markdown(f"**<span style='color: {kpis[k]['color']}; text-decoration: underline; font-weight: bold;'> {k} </span>", unsafe_allow_html=True)

            # Description and Example
            st.markdown(f"**Description:** {kpis[k]['desc']}")
            st.markdown(f"**Example:** {kpis[k]['example']}")

            build_dial(k, kpis[k]["value"], kpis[k]["total"], kpis[k]["color"], key_prefix="phase3")

    st.button("Submit Phase 3 KPIs")


