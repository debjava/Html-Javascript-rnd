Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "java java -jar testswing.jar" & Chr(34), 0
Set WshShell = Nothing
