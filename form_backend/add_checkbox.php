<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the new checkbox title from the form
    $newCheckbox = $_POST["newweb"];
    $newurl= $_POST["weburl"];
    $usr=$_POST["username"];
    $email=$_POST["newemail"];

    include('../Database/db.php');

    if($newCheckbox!="" && $usr!="" && $email!="" && $newurl!="")
    {
        try{
        $insertOrder="INSERT INTO websites(web_name,web_url,username,email) VALUES('$newCheckbox','$newurl','$usr','$email')";
        $result=mysqli_query($conn,$insertOrder);
        }catch(Exception $e)
        {
            echo '<script type="text/javascript">alert("Error in form data.") </script>';
        }
    }
    else{
        echo '<script type="text/javascript">alert("No Null values accepted!! \n Please fill all fields in form.") </script>';
    }

    // Append the new checkbox title to the file
    // if ($newCheckbox!="")
    // file_put_contents("checkboxes.txt", $newCheckbox ."-".$newurl."\n", FILE_APPEND);

    // if($usr!="" && $email!="")
    // {
    // file_put_contents("admindetails.txt", $usr ." ".$email, FILE_APPEND);
    // }


    // Redirect back to the index page
    header("Location: ../index.php");
    exit();
}
?>
