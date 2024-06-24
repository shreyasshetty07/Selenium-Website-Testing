# flask_server.ps1
$scriptPath = "../server/create_server.py"
$process = Start-Process "python" -ArgumentList "$scriptPath" -PassThru -WindowStyle Minimized

# Write the PID to a file
$process.Id | Out-File -FilePath "flask_server_pid.txt"