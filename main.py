import streamlit as st
import requests
from pathlib import Path
from PIL import Image
st.set_page_config(page_title="Asgard Instrument Suite", layout="wide")

# Title and Introduction
st.title("🔭 Asgard: A New Era for the VLTI")
st.markdown("""
ESO's **Very Large Telescope Interferometer (VLTI)** has a history of record-breaking discoveries in astrophysics and instrumentation.  
The **Asgard** project is the next leap forward: an integrated instrumental suite pushing the limits of infrared interferometry.
""")

# Path to your local figures
fig_dir = Path("figs")
image_files = sorted(fig_dir.glob("*.png"))  # All PNGs in /figs/

for image_path in image_files:
    #st.subheader(image_path.stem.replace("_", " ").title())  # Optional: make title from filename
    img = Image.open(image_path)
    st.image(img, use_column_width=True)  # or width=600 for fixed size

# Instrument Overview
st.header("🧰 The Four Asgard Instruments")

cols = st.columns(2)
with cols[0]:
    st.subheader("🔹 HEIMDALLR")
    st.markdown("""
    - Operates in the **K band**  
    - Dual waveband  **fringe tracking** technology for the entire Asgard suite. 
    - dual-use signals for fringe tracking/cophasing and interferometric science operation. 
    """)

    st.subheader("🔹 BALDR")
    st.markdown("""
    - Operates in the **J or H band** 
    - Zernike Wavefront Sensing to Optimize the **Strehl ratio**  for the entire Asgard suite. 
    - The fastest and most sensitive wavefront sensor at the VLT.
    """)

with cols[1]:
    st.subheader("🔹 BIFROST")
    st.markdown("""
    - Operates in **Y, J, and H bands**  
    - Aims to study **stellar and planetary formation** processes with the highest, VLTI available, spectral and spatial resolution!
    - high spectral dispersion (up to R=25,000) window to unlock powerful avenues for studying accretion & mass-loss processes at the early/late stages of stellar evolution, for detecting accreting protoplanets around young stars, and for probing the spin-orbit alignment in directly-imaged planetary systems and multiple star systems. 
    """)

    st.subheader("🔹 NOTT")
    st.markdown("""
    - Operates in the **L band**  
    - The first **nulling interferometer** observing in the southern hemisphere. 
    - Detecting young planetary systems near the snow line, a critical region for giant planet formation, and nearby main-sequence stars close to the habitable zone, with a focus on detecting exozodiacal dust that could obscure Earth-like planets
    """)

# Project Status
st.header("🚧 Current Status")
st.markdown("""
- Heimdallr & Baldr passed the ESO review and are on their way to Paranal, Chile for comissioning starting June 2025!  
- Bifrost and Nott are is currently in the **integration phase** in Europe and coming over to Paranal in 2026! 
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




st.subheader("Contact Us!")
feedback = st.text_area("Your comments:")
email = st.text_input("Your email (optional):")

if st.button("Send"):
    data = {
        "message": feedback,
        "email": email
    }
    # Replace YOUR_FORMSPREE_ENDPOINT
    res = requests.post("https://formspree.io/f/xeokzkod", data=data)
    if res.status_code == 200:
        st.success("Feedback sent!")
    else:
        st.error("Something went wrong.")

# Footer
st.markdown("---")
st.markdown("Asgard Project | VLTI | ESO")

