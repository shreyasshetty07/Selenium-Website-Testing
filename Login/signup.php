<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Register</title>
  <link rel="stylesheet" href="css/style1.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style>
    .line{
    margin-top: 15px;
    width: 360px;
    height: 47px;
    border-top: 3px solid grey;
    position: absolute;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="form-box box">


      <header>Sign Up</header>
      <hr>

      <form action="#" method="POST" enctype="multipart/form-data">


        <div class="form-box">

          <?php

          session_start();

          include "connection.php";

          if (isset($_POST['register'])) {

            $name = $_POST['username'];
            $email = $_POST['email'];
            $pass = $_POST['password'];
            $cpass = $_POST['cpass'];
            $webname=$_POST['webname'];
            str_replace(' ','',$webname);
            $weburl=$_POST['WebURL'];


            $check = "select * from users where email='{$email}'";

            $res = mysqli_query($conn, $check);

            $passwd = password_hash($pass, PASSWORD_DEFAULT);

            $key = bin2hex(random_bytes(12));




            if (mysqli_num_rows($res) > 0) {
              echo "<div class='message'>
        <p>This email is used, Try another One Please!</p>
        </div><br>";

              echo "<a href='javascript:self.history.back()'><button class='btn'>Go Back</button></a>";


            } else {

              if ($pass === $cpass) {

                $sql = "insert into users(name,email,password) values('$name','$email','$passwd')";

                $result = mysqli_query($conn, $sql);

                if ($result) {

                  echo "<div class='message'>
      <p>You are register successfully!</p>
      </div><br>";
      $sql = "insert into websites(web_name,web_url,username,email) values('$webname','$weburl','$name','$email')";

                $result = mysqli_query($conn, $sql);

      echo "<div class='message'>
      <p>Checking the scripts Uploaded...</p>
      </div><br>";
      $webname=str_replace(' ','',$webname);
      if(is_dir("../testscript_uploads/$webname/")==false)
        {
            mkdir("../testscript_uploads/$webname/");
        }
        $folder_path = "../testscript_uploads/$webname/"; 

        if(isset($_POST['register'])) {
        $files = $_FILES['fileUpload'];
      for($i=0; $i<count($files['name']); $i++){


      if (isset($files["name"][$i]) && $files["error"][$i] == 0) {
          $targetDir = "../testscript_uploads/$webname/";
          $targetFile = $targetDir . basename($files["name"][$i]);
          $fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));
  
          // Check if the file is a Python file
          if ($fileType == "py") {
              // If it's a Python file, move it to the uploads directory
              if (move_uploaded_file($files["tmp_name"][$i], $targetFile)) {
                echo "<a href='login.php'><button class='btn'>Login Now</button></a>";

                echo "<div class='message'>
        <p>File uploaded successfully: ".htmlspecialchars(basename($files["name"][$i]))."</p>
        </div><br>";
              } else {
                echo "<div class='message'>
        <p>Fail 1</p>
        </div><br>";
                  echo '<script type="text/javascript">alert("Error uploading file.")</script>';
                  echo "<script type='text/javascript'>window.location.href='newsignuppage.php'</script>";
              }
          } else {
            echo "<div class='message'>
        <p>Fail 2</p>
        </div><br>";
              echo '<script type="text/javascript">alert("Only Python files are allowed.")</script>';
              echo "<script type='text/javascript'>window.location.href='newsignuppage.php'</script>";
          }
      } else {
        echo "<div class='message'>
        <p>Fail 3</p>
        </div><br>";
          echo '<script type="text/javascript">alert(Error: ' . $files["error"][$i].')</script>';
          echo "<script type='text/javascript'>window.location.href='newsignuppage.php'</script>";
      }
  }
}

                 # echo "<a href='login.php'><button class='btn'>Login Now</button></a>";

                } else {
                  echo "<div class='message'>
        <p>This email is used, Try another One Please!</p>
        </div><br>";

                  echo "<a href='javascript:self.history.back()'><button class='btn'>Go Back</button></a>";
                }

              } else {
                echo "<div class='message'>
      <p>Password does not match.</p>
      </div><br>";

                echo "<a href='signup.php'><button class='btn'>Go Back</button></a>";
              }
            }
          } else {

            ?>

            <div class="input-container">
              <i class="fa fa-user icon"></i>
              <input class="input-field" type="text" placeholder="Username" name="username" required>
            </div>

            <div class="input-container">
              <i class="fa fa-envelope icon"></i>
              <input class="input-field" type="email" placeholder="Email Address" name="email" required>
            </div>

            <div class="input-container">
              <i class="fa fa-lock icon"></i>
              <input class="input-field password" type="password" placeholder="Password" name="password" required>
              <i class="fa fa-eye icon toggle"></i>
            </div>

            <div class="input-container">
              <i class="fa fa-lock icon"></i>
              <input class="input-field" type="password" placeholder="Confirm Password" name="cpass" required>
              <i class="fa fa-eye icon"></i>
            </div>

            <div class="line"></div>
            <br><br>

            <div class="input-container">
              <i class="fa fa-user icon"></i>
              <input class="input-field" type="text" placeholder="Website Name" name="webname" required>
            </div>

            <div class="input-container">
              <i class="fa fa-user icon"></i>
              <input class="input-field" type="text" placeholder="Website URL" name="WebURL" required>
            </div>
            <br>
            <label>Upload Test Scripts</label>
            <div class="input-container">
                <input class="input-field" type="file" style="margin-top:20px; padding:60px;" name="fileUpload[]" multiple />
            </div>

            

          </div>


          <center><input type="submit" name="register" id="submit" value="Signup" class="btn"></center>


          <div class="links">
            Already have an account? <a href="login.php">Signin Now</a>
          </div>

        </form>
      </div>
      <?php
          }
          ?>
  </div>

  <script>
    const toggle = document.querySelector(".toggle"),
      input = document.querySelector(".password");
    toggle.addEventListener("click", () => {
      if (input.type === "password") {
        input.type = "text";
        toggle.classList.replace("fa-eye-slash", "fa-eye");
      } else {
        input.type = "password";
      }
    })
  </script>
</body>

</html>