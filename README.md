convert any images to heif or avif format using pillow 


해당 실행파일은 파이썬이 시스템에 설치되어 있는 것을 전제로 합니다.

실행파일은 Release 페이지 안에 있는 링크 타고 원하는 파일 다운 받으세요. (파이썬 버전 안맞으면 실행이 안되는 것 같아요)

윈도우의 경우 더블클릭 실행은 터미널이 막혀 있으므로 tkinter-support이 있다는 가정하에서 gui버전 추천
윈도우는 `pythonw.exe gui.pyz`,  `python.exe cli.pyz`, `python.exe gui.pyz`,  조합으로 실행 가능


macOS는 파일 다운로드하면 gatekeeper로 실행이 차단되므로 `python3 gui.pyz` , `python3 cli.pyz` 처럼 터미널로 직접 실행해야함

(확장자 지우고 gatekeeper 풀어주면 더블클릭으로 실행 가능)

 gui버전은 tkinter-support(gui-support)이 내장된 python이 요구됨

 macOS 

 `brew install python-tk@3.13`

 windows

 `winget install Python.Python.3.13`

 Linux 

 `sudo apt update && sudo apt install python3-tk`
