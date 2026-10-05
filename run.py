"""
Student Performance Prediction System - Root Runner Script
Convenience entry-point to run the Flask application directly from the workspace root.
"""
import os
import sys

# Point to the student-performance package directory
pkg_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student-performance")
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)
os.chdir(pkg_dir)

from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Launching Student Performance Prediction System...")
    print(f"Open your browser at: http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=True)
