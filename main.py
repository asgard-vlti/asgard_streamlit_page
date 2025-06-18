import streamlit as st

st.set_page_config(page_title="Asgard Instrument Suite", layout="wide")

# Title and Introduction
st.title("🔭 Asgard: A New Era for the VLTI")
st.markdown("""
ESO's **Very Large Telescope Interferometer (VLTI)** has a history of record-breaking discoveries in astrophysics and instrumentation.  
The **Asgard** project is the next leap forward: an integrated instrumental suite pushing the limits of infrared interferometry.
""")

# Instrument Overview
st.header("🧰 The Four Asgard Instruments")

cols = st.columns(2)
with cols[0]:
    st.subheader("🔹 HEIMDALLR")
    st.markdown("""
    - Operates in the **K band**  
    - Performs **fringe tracking** and **stellar interferometry** **simultaneously**
    - Uses a **common optical path** for both
    """)

    st.subheader("🔹 BALDR")
    st.markdown("""
    - Works in the **J or H band**  
    - Zernike Wavefront Sensing to Optimize the **Strehl ratio**  
    - Enhances wavefront correction for high-quality imaging
    """)

with cols[1]:
    st.subheader("🔹 BIFROST")
    st.markdown("""
    - Operates in **Y, J, and H bands**  
    - Aims to study **stellar and planetary formation** processes  
    - Provides **broadband combination** for deep insight into circumstellar environments
    """)

    st.subheader("🔹 NOTT")
    st.markdown("""
    - Operates in the **L band**  
    - A dedicated **nulling interferometer**  
    - Focused on **imaging young planetary systems** nearby
    """)

# Project Status
st.header("🚧 Current Status")
st.markdown("""
- Asgard is currently in the **integration phase** in Europe  
- Target shipment to **Paranal Observatory**: **early 2025**  
- Pending final approval by **ESO**
""")

# Science Cases
st.header("🌌 Key Science Cases")
st.markdown("""
- **Fringe tracking and interferometry synergy** (HEIMDALLR)  
- **High Strehl imaging** in the near-infrared (BALDR)  
- **Protoplanetary disk characterization** (BIFROST)  
- **Direct detection of young exoplanets** (NOTT)
""")

st.info("This page provides a preview of Asgard, its instruments, and its mission to enable next-generation interferometric science.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ for the Asgard Project | VLTI | ESO")

