from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
import subprocess
import uuid
import os

app = FastAPI()

@app.post("/compile-latex/")
async def compile_latex(tex_code: str = Form(...)):
    # Create temp directory
    job_id = str(uuid.uuid4())
    temp_dir = f"/tmp/{job_id}"
    os.makedirs(temp_dir, exist_ok=True)

    tex_path = os.path.join(temp_dir, "document.tex")
    pdf_path = os.path.join(temp_dir, "document.pdf")

    # Write LaTeX to file
    with open(tex_path, "w") as f:
        f.write(tex_code)

    # Compile with Tectonic
    try:
        subprocess.run(
            ["/usr/local/bin/tectonic", tex_path, "--outdir", temp_dir],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        return {"error": f"LaTeX compilation failed: {e.stderr.decode()}"}

    # Return compiled PDF
    return FileResponse(pdf_path, media_type="application/pdf", filename="generated.pdf")
