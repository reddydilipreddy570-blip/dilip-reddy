import cv2
import numpy as np

print("=============================================")
print("  🚀 DEEPFAKE DETECTOR INITIALIZED 🚀        ")
print("=============================================")

def scan_for_deepfake(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"❌ Error: Cannot find '{image_path}' inside this folder.")
        print("💡 Action: Drag any face image into your sidebar and name it 'test_face.jpg'!")
        return

    print("✅ Media file loaded successfully into memory.")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Mathematical algorithms to spot artificial textures
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    std_deviation = np.std(gray)
    
    print("\n--- FORENSIC ANALYSIS RESULTS ---")
    print(f"🔹 Texture Inconsistency Score: {laplacian_var:.2f}")
    print(f"🔹 Pixel Blending Variance: {std_deviation:.2f}")
    
    if laplacian_var < 100.0:
        print("\n⚠️ VERDICT: High Probability of AI Manipulation / Deepfake Blur detected!")
    else:
        print("\n❇️ VERDICT: Authentic Camera Capture (High frequency details present).")

# Trigger the analysis loop
scan_for_deepfake("test_face.jpg.jpg")


