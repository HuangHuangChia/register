cd c:\Task\register
c:\Task\register\register_all.py
timeout /t 10 >nul
chcp 65001
IF EXIST "c:\Task\Register_All_info.txt" (
c:\Task\LineNotify\LineNotify_general.exe "0xQH1k7AuD1CERF9Hy12XNv8MnTOE8V6MwitbfdJHe9" "c:\Task\register\register_all_info.txt"
ECHO "沒執行linenotify"
)
