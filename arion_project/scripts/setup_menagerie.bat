@echo off
cd /d %~dp0\..
if not exist external mkdir external
if not exist external\mujoco_menagerie git clone https://github.com/google-deepmind/mujoco_menagerie.git external\mujoco_menagerie
setx MUJOCO_MENAGERIE_PATH "%CD%\external\mujoco_menagerie"
echo Open a new Anaconda Prompt.
