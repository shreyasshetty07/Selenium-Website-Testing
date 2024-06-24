<?php
// Path to the PID file
$pidFilePath = '../form_backend/flask_server_pid.txt';
// Read the PID from the file
$rrtt=0;
$truval="";
if (file_exists($pidFilePath)) {
    $pid = file_get_contents($pidFilePath);
    $rrtt=substr($pid,2);
    $num=intval($rrtt);
    echo("hi ".$pid);

    $mystr = array($rrtt);
$string = strlen($rrtt);
for($i=0; $i<$string; $i++)
{   
    if(is_numeric($rrtt[$i]))
    {
        $truval.=$rrtt[$i];
    }
    #echo $rrtt[$i]."-"; 
}
/*echo $truval;
for($i=0; $i<=$string; $i++)
{   
    echo $truval[$i]."-"; 
}*/
    // Terminate the process using the PID
    if ($pid) {
        exec("taskkill /F /PID $truval",$output,$res_code);
        //exec("taskkill /f /im cmd.exe");

        if ($res_code === 0) {
            echo "Flask server with PID $truval has been terminated.";
            exec("taskkill /f /im cmd.exe");
            // Optionally delete the PID file
            #unlink($pidFilePath);
        } else {
            echo "Failed to terminate Flask server with PID $truval.";
        }
    } else {
        echo "PID file is empty.";
    }
} else {
    echo "PID file not found.";
}
?>
