sc.exe stop QNBackServer
sc.exe delete QNBackServer
echo "��װQNBackServer����"
sc.exe create QNBackServer binPath=%~dp0\bin\BackServer.exe
sc.exe config QNBackServer start=auto
sc.exe start QNBackServer

.\bin\install.exe
