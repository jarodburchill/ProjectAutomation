@ECHO OFF
cd /D %~dp0..
pip install -r requirements.txt >NUL
python automate_project.py