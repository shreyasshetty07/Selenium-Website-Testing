<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the new checkbox title from the form
    $newCheckbox = $_POST["checkboxes"];
    foreach ($newCheckbox as $name){ 
        #echo '<script type="text/javascript">alert("'.$name.'")</script>';
        include('../Database/db.php');
              $query1="SELECT *
                       FROM websites
                       WHERE web_name LIKE '$name'";
              $result=mysqli_query($conn,$query1);
              $row=mysqli_fetch_assoc($result);
              $appname=$row["web_name"];
              $usr=$row["username"];
              $email=$row["email"];
              $appname=str_replace(' ','',$appname);

              if($usr!="" && $email!="")
              {
                file_put_contents("admindetails.txt", "");
                file_put_contents("admindetails.txt", $usr ." ".$email." ".$appname, FILE_APPEND);
              }
    }

    if(isset($_POST['submit'])) {

#shell_exec('C:/Users/SHREESHA/AppData/Local/Microsoft/WindowsApps/python3.10.exe "c:/xampp/htdocs/Selenium Website Testing/server/dynamicServer.py"');
$command='start /B cmd /k "python ../server/dynamicServer.py"';
exec($command,$ret_val);

if ($ret_val[0] == "Flask app file generated successfully!"){
    #echo '<script type="text/javascript">alert("Background server setup complete")</script>';

    $command = "powershell.exe -ExecutionPolicy Bypass -File ../flask_server_setup.ps1";
    #$command="powershell.exe -NoLogo -NoProfile -WindowStyle Minimized -Command \"Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ../flask_server_setup.ps1' -WindowStyle Minimized\"";
    exec($command,$valll,$res_code); 
    #echo '<script type="text/javascript">alert("'.$res_code.'")</script>';
    if($res_code == 0)
    {
    echo "<script type='text/javascript'>window.location.href='../dashboard.php?appname=$appname'</script>";
    }
    else{
        echo '<script type="text/javascript">alert("Unable to create Flask server ENV!!")</script>';
        echo "<script type='text/javascript'>window.location.href='../index.php'</script>";
    }
    }

else{
    echo '<script type="text/javascript">alert("Background server setup complete FAILED!!!")</script>';
    header("Location: ../index.php");

}
    // header("Location: ../dashboard.php");
    // exit();
}
}
?>
