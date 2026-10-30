import streamlit as size_config  # Custom import alias to keep code clean
import streamlit as st
import cv2
import numpy as np
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CBSE Class 12 AI Exploration App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR BEAUTIFUL CBSE THEME ---
st.markdown("""
<style>
    .main-title { font-size: 38px; font-weight: 700; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size: 18px; color: #4B5563; margin-bottom: 25px; }
    .section-card { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #2563EB; margin-bottom: 20px; }
    .metric-box { background-color: #FFFFFF; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://icons8.com", width=80)
st.sidebar.title("AI Lab Dashboard")
st.sidebar.markdown("**CBSE Class 12 (Code 417)**")
st.sidebar.markdown("---")

app_mode = st.sidebar.radio(
    "Select AI Domain Module:",
    ["🏠 Home & Overview", "📷 Computer Vision: Gesture RPS Game", "✍️ NLP: Text Processing Pipeline"]
)

# =========================================================================
# 🏠 MODULE 1: HOME & OVERVIEW
# =========================================================================
if app_mode == "🏠 Home & Overview":
    st.markdown('<div class="main-title">CBSE Class 12 AI Curriculum App</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">An interactive portal demonstrating Core Units: Computer Vision & Natural Language Processing</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="section-card">
            <h3>👁️ Unit 3: Computer Vision (CV)</h3>
            <p>Explore real-time image acquisition, manipulation, and pixel analysis. Test your reflex skills using simulated computer vision algorithms directly with your camera feed or image processing steps.</p>
            <ul>
                <li><strong>Concepts covered:</strong> RGB/Grayscale Conversion, Thresholding, Edge Detection, Shape & Contour Analysis.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="section-card">
            <h3>🔤 Unit 4: Natural Language Processing (NLP)</h3>
            <p>Understand how applications digest human languages by breaking down sentences into mathematical components through a structured textbook processing workflow.</p>
            <ul>
                <li><strong>Concepts covered:</strong> Tokenization, Stop Word Removal, Lemmatization/Stemming, Bag of Words formulation.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 **Getting Started:** Expand the left sidebar panel to alternate between the active Computer Vision camera engine and the NLP textual processing simulator.")

# =========================================================================
# 📷 MODULE 2: COMPUTER VISION & GESTURE GAME
# =========================================================================
elif app_mode == "📷 Computer Vision: Gesture RPS Game":
    st.markdown('<div class="main-title">Computer Vision Interaction Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Simulating gesture extraction and pixel threshold profiling using OpenCV.</div>', unsafe_allow_html=True)

    cv_task = st.selectbox("Select CV Sub-Task:", ["Rock-Paper-Scissors Camera Analyzer", "Image Filter & Processing Sandbox"])

    if cv_task == "Rock-Paper-Scissors Camera Analyzer":
        st.write("### ✊✋✌️ Hand Sign Detection Simulator")
        st.caption("Class 12 AI Concepts: Multi-class classification via bounding boxes and pixel count parameters.")
        
        # Camera layout inputs
        img_file = st.camera_input("Capture your hand sign (Rock, Paper, or Scissors):")
        
        if img_file is not None:
            # Convert bytes file to OpenCV image format
            file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
            opencv_img = cv2.imdecode(file_bytes, 1)
            
            # Simulated CV feature processing (Analyzing hand silhouette size via grayscale pixel count)
            gray = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
            white_pixels = np.sum(thresh == 255)
            
            # Rule-based algorithmic classification mapping based on white pixel density heuristics
            if white_pixels < 30000:
                detected_sign = "Rock ✊"
                ai_choice = "Paper ✋"
                result = "AI wins! Paper covers Rock."
            elif white_pixels < 75000:
                detected_sign = "Scissors ✌️"
                ai_choice = "Rock ✊"
                result = "AI wins! Rock smashes Scissors."
            else:
                detected_sign = "Paper ✋"
                ai_choice = "Scissors ✌️"
                result = "AI wins! Scissors cuts Paper."
                
            # Layout display
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div class="metric-box"><h4>Your Detected Sign</h4><h3>' + detected_sign + '</h3></div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="metric-box"><h4>AI Move Prediction</h4><h3>' + ai_choice + '</h3></div>', unsafe_allow_html=True)
            with c3:
                st.markdown('<div class="metric-box"><h4>Round Outcome</h4><h4>' + result + '</h4></div>', unsafe_allow_html=True)
                
            st.image(opencv_img, channels="BGR", caption="CV Camera Processing Stream Output Frame", use_container_width=True)

    elif cv_task == "Image Filter & Processing Sandbox":
        st.write("### ⚙️ Pixel Transformation Engine")
        img_upload = st.file_uploader("Upload an image asset to transform:", type=["jpg", "png", "jpeg"])
        
        if img_upload is not None:
            f_bytes = np.asarray(bytearray(img_upload.read()), dtype=np.uint8)
            src_img = cv2.imdecode(f_bytes, 1)
            
            filter_mode = st.radio("Choose Convolution / Processing filter:", ["Grayscale Conversion", "Canny Edge Detection", "Otsu Thresholding"])
            
            if filter_mode == "Grayscale Conversion":
                out = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
                st.image(out, caption="Processed Matrix Result", use_container_width=True)
            elif filter_mode == "Canny Edge Detection":
                out = cv2.Canny(src_img, 100, 200)
                st.image(out, caption="Processed Matrix Result", use_container_width=True)
            elif filter_mode == "Otsu Thresholding":
                gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
                _, out = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                st.image(out, caption="Processed Matrix Result", use_container_width=True)

# =========================================================================
# ✍️ MODULE 3: NATURAL LANGUAGE PROCESSING
# =========================================================================
elif app_mode == "✍️ NLP: Text Processing Pipeline":
    st.markdown('<div class="main-title">NLP Pipeline Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Step-by-step extraction mapping raw string records down to numeric representations.</div>', unsafe_allow_html=True)
    
    sample_text = st.text_area(
        "Enter text corpus line to process:",
        "Artificial Intelligence is changing the world. Computer Vision and NLP are part of Class 12 AI syllabus!"
    )
    
    if st.button("Execute Pipeline Step Analysis"):
        st.markdown("### 🛠️ Execution Pipeline Stages")
        
        # Stage 1: Normalization & Tokenization
        lower_text = sample_text.lower()
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = "".join([char for char in lower_text if char not in punctuations])
        tokens = no_punct.split()
        
        st.write("**Step 1: Text Tokenization (Lowercase & Punctuation Cleaned)**")
        st.json(tokens)
        
        # Stage 2: Stop Words Removal
        cbse_stop_words = ["is", "the", "and", "are", "of", "to", "in", "a", "an", "for", "with"]
        filtered_tokens = [w for w in tokens if w not in cbse_stop_words]
        
        st.write("**Step 2: Stop Words Removal (Cleaned Key Terms)**")
        st.success(f"Tokens remaining: {filtered_tokens}")
        
        # Stage 3: Simple Structural Stemming
        def basic_stemmer(word):
            if word.endswith("ing"): return word[:-3]
            if word.endswith("ed"): return word[:-2]
            if word.endswith("s") and len(word) > 3: return word[:-1]
            return word
            
        stemmed_tokens = [basic_stemmer(w) for w in filtered_tokens]
        st.write("**Step 3: Text Stemming (Root Extraction)**")
        st.info(f"Stemmed roots: {stemmed_tokens}")
        
        # Stage 4: Bag of Words (BoW) Representation
        st.write("**Step 4: Vector Generation (Bag of Words Word Frequency Mapping)**")
        vocab_frequency = {}
        for word in stemmed_tokens:
            vocab_frequency[word] = vocab_frequency.get(word, 0) + 1
            
        st.columns(1)[0].table([{"Term (Token)": k, "Frequency Count": v} for k, v in vocab_frequency.items()])

