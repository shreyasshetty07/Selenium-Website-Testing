<?php
session_start();

include("Login/connection.php");

if (!isset($_SESSION['username'])) {
    header("location:Login/login.php");
}




?>
<!DOCTYPE html>
<html lang="en">
  
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Impact Bootstrap Template - Index</title>
  <meta content="" name="description">
  <meta content="" name="keywords">

  <!-- Favicons -->
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600;1,700&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="assets/css/main.css" rel="stylesheet">

  <!-- =======================================================
  * Template Name: Impact
  * Updated: Sep 18 2023 with Bootstrap v5.3.2
  * Template URL: https://bootstrapmade.com/impact-bootstrap-business-website-template/
  * Author: BootstrapMade.com
  * License: https://bootstrapmade.com/license/
  ======================================================== -->
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
<style>
#myform{
  height:500px;
  font-size: 20px;
  width:600px;
  background-color:white;
  margin-left:auto;
  margin-right:auto;
  border-radius:30px;
  padding:30px;
}
.open-button {
  background-color: #555;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  opacity: 0.8;
  position: fixed;
  bottom: 23px;
  right: 28px;
  width: 280px;
}

/* The popup form - hidden by default */
.form-popup {
  display: none;
  position: fixed;
  bottom: 0;
  right: 15px;
  border: 3px solid #f1f1f1;
  z-index: 9;
}

/* Add styles to the form container */
.form-container {
  height:auto;
  width:300px;
  background-color:white;
  margin-left:auto;
  margin-right:auto;
  border-radius:10px;
  padding:10px;
}

/* Full-width input fields */
.form-container input[type=text], .form-container input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  border: none;
  background: #f1f1f1;
}

/* When the inputs get focus, do something */
.form-container input[type=text]:focus, .form-container input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Set a style for the submit/login button */
.form-container .btn {
  background-color: #04AA6D;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  margin-bottom:10px;
  opacity: 0.8;
}

/* Add a red background color to the cancel button */
.form-container .cancel {
  background-color: red;
}

/* Add some hover effects to buttons */
.form-container .btn:hover, .open-button:hover {
  opacity: 1;
}
</style>
</head>

<body>
  <py-script src="server\\server.py"></py-script>
  <!-- ======= Header ======= -->
  <header id="header" class="header d-flex align-items-center">

    <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
      <a href="index.html" class="logo d-flex align-items-center">
        <!-- Uncomment the line below if you also wish to use an image logo -->
        <!-- <img src="assets/img/logo.png" alt=""> -->
        <h1>Test Automation<span>.</span></h1>
      </a>
      <nav id="navbar" class="navbar">
        <ul>
          <li><a href="#hero">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="Login/login.php">Login</a></li>
          <li class="nav-item">
                            <div class="dropdown">
                                <a class='nav-link dropdown-toggle' href='Login/edit.php?id=$res_id' id='dropdownMenuLink'
                                    data-bs-toggle='dropdown' aria-expanded='false'>
                                    <i class='bi bi-person'></i>
                                </a>


                                <ul class="dropdown-menu mt-2 mr-0" aria-labelledby="dropdownMenuLink">

                                    <li>
                                        <?php

                                        $id = $_SESSION['id'];
                                        $query = mysqli_query($conn, "SELECT * FROM users WHERE id = $id");

                                        while ($result = mysqli_fetch_assoc($query)) {
                                            $res_username = $result['name'];
                                            $res_email = $result['email'];
                                            $res_id = $result['id'];
                                        }


                                        echo "<a class='dropdown-item' href='Login/edit.php?id=$res_id'>Change Profile</a>";


                                        ?>

                                    </li>
                                    <li><a class="dropdown-item" href="#"><?php echo "Hello, ".$res_username;?></a></li>
                                    <li><a class="dropdown-item" href="Login/logout.php">Logout</a></li>
                                </ul>
                            </div>

                        </li>
        </ul>
      </nav><!-- .navbar -->

      <i class="mobile-nav-toggle mobile-nav-show bi bi-list"></i>
      <i class="mobile-nav-toggle mobile-nav-hide d-none bi bi-x"></i>

    </div>
  </header><!-- End Header -->
  <!-- End Header -->
  
  <!-- ======= Hero Section ======= -->
<div class="hero">
    <div class="container position-relative">
      <div class="row gy-5" data-aos="fade-in">
        <div class="col-lg-6 order-2 order-lg-1 d-flex flex-column justify-content-center text-center text-lg-start">
          <h2>Selenium Test <span>Automation</span></h2>
        </div>
        <div class="col-lg-6 order-1 order-lg-2">
          <img src="assets/img/hero-img.svg" class="img-fluid" alt="" data-aos="zoom-out" data-aos-delay="100">
        </div>
      </div>
    </div>
<h3 style="margin-top:100px; margin-bottom:40px; color:white; text-align:center;">Choose the Application to be Tested</h3>
<div id="myform">
<form action="./form_backend/Prepare_TestEnv.php" method="POST" enctype="multipart/form-data">
  <h4>Select the Website</h4>
    <?php
            	include('Database/db.php');
              $query1="SELECT *
                       FROM websites";
              $result=mysqli_query($conn,$query1);

              while($row=mysqli_fetch_assoc($result))
              {
                echo '<input type="checkbox" name="checkboxes[]" value="' . $row["web_name"] . '" style="transform: scale(2); margin-right:20px;">' . $row["web_name"] . ' - '.$row["web_url"].'<br>';

              }
          
            //   $insertOrder="INSERT INTO orders (cid,itemid,shipaddress,total)
            //                 SELECT cid, itemid, caddress,price
            //                 FROM customer, item
            //                 WHERE cid='$custid' AND itemid='$x'";
            //   $result=mysqli_query($conn,$insertOrder);
            // // Read checkbox titles from the file and create checkboxes
            // $checkboxes = file("form_backend/checkboxes.txt", FILE_IGNORE_NEW_LINES);
            // foreach ($checkboxes as $checkbox) {
            //     echo '<input type="checkbox" name="checkboxes[]" value="' . htmlspecialchars($checkbox) . '">' . htmlspecialchars($checkbox) . '<br>';
            // }
        ?>
        <br><br><br>
  <div class="form-group">
    <label for="pwd">Upload Test Scripts</label>
    <input class="form-control" type="file" name="fileUpload[]" multiple />  </div>

  <button type="submit" class="btn btn-default" name="submit">Submit</button>
</form>
</div><!-- center menu-->

  <!-- ADD new Website BUTTON  -->
<button class="open-button" onclick="openForm()">ADD NEW WEBSITE</button>  
<div class="form-popup" id="myForm">
  <form action="./form_backend/add_checkbox.php" class="form-container" method="POST">
    <h1>ADD NEW WEBSITE</h1>

    <label for="newweb"><b>Add New Website</b></label>
    <input type="text" placeholder="Enter Website" name="newweb" required>
    <label for="newweb"><b>Enter the website URL</b></label>
    <input type="text" placeholder="Enter the URL" name="weburl" required>
    <label for="newweb"><b>Username</b></label>
    <input type="text" placeholder="Enter the Username" name="username" required>
    <label for="newweb"><b>Email</b></label>
    <input type="text" placeholder="Enter the Email" name="newemail" required>

    <button type="submit" class="btn">Login</button>
    <button type="button" class="btn cancel" onclick="closeForm()">Close</button>
  </form>
</div>

<br><br>
</div>
<!-- Hero END-->
  <main id="main">

    <!-- ======= About Us Section ======= -->
    <section id="about" class="about">
      <div class="container" data-aos="fade-up">

        <div class="section-header">
          <h2>About Us</h2>
          <h5><h4>Created by:</h4><br>Shreesha S Shetty<br>Shreyas <br>Vyshak Achar</h5>
        </div>
      </div>
    </section><!-- End About Us Section -->


  <!-- ======= Footer ======= -->
  <footer id="footer" class="footer">

    <div class="container">
      <div class="row gy-4">
        <div class="col-lg-5 col-md-12 footer-info">
          <a href="index.html" class="logo d-flex align-items-center">
            <span>Test Automation</span>
          </a>
          <p>This is a dashboard to manage Test Suits and view Test Logs.</p>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h4>Useful Links</h4>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About us</a></li>
            <li><a href="#">Test Logs</a></li>
            <li><a href="#">Test Cases</a></li>
          </ul>
        </div>
      </div>
    </div>

  </footer><!-- End Footer -->
  <!-- End Footer -->

  <a href="#" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/vendor/purecounter/purecounter_vanilla.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>

  <!-- Template Main JS File -->
  <script src="assets/js/main.js"></script>
  <script>
function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
</script>
</body>

</html>