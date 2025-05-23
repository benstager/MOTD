import requests

API_URL = "https://latex-compiler-at6vr.ondigitalocean.app/compile-latex/"

dummy_latex = r"""
\documentclass{article}
\begin{document}
Hello from Streamlit!
\end{document}
"""

response = requests.post(API_URL, data={"tex_code": dummy_latex})

if response.status_code == 200:
    with open("output.pdf", "wb") as f:
        f.write(response.content)
    print("PDF compiled successfully")
else:
    print("Failed to compile PDF:", response.json())