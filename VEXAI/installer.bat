
---

### 5. How to Upload to GitHub (Step-by-Step)

1.  **Go to [GitHub.com](https://github.com)** $\rightarrow$ Log in $\rightarrow$ Click the **"+"** icon $\rightarrow$ **New Repository**.
2.  **Name it:** `VEXAI` (or `VexAI-Multiverse`).
3.  **Settings:** Set it to **Public**.
4.  **Upload:**
    *   Click **"uploading an existing file"**.
    *   Drag and drop your 4 files (`vexai_ultimate.py`, `requirements.txt`, `Modelfile`, `README.md`).
    *   Click **"Commit changes"**.

### Final Pro Tip:
If you want to make it even easier for your friends, you can create a file called `install.bat` (for Windows) and put this inside:
```batch
@echo off
echo Installing VEXAI dependencies...
pip install -r requirements.txt
echo.
echo Launching VEXAI...
python -m streamlit run vexai_ultimate.py
pause
