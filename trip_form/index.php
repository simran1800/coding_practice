<?php

$nameErr = $ageErr = $emailErr = $genderErr = $phoneErr = $message = "";
$name= $age = $email = $gender = $phone =  "";

if(isset($_POST['name'])){

//**************setting connection variables************
$server="localhost";
$username="root";
$password="";


//****create connection*********
$con=mysqli_connect($server,$username,$password);

//***********check for connection**************
if (!$con){
	die("connection to this database failed due to ".mysqli_connect_error());
}

//echo "Success connecting to the db";


//*******collect the post variables*********
if (empty($_POST["name"])) {
    $nameErr = "Name is required";
    }else{
    	$name=$_POST['name'];
    }

if (empty($_POST["age"])) {
    $ageErr = "Age is required";
    }else{
    	$age=$_POST['age'];
    }

if (empty($_POST["gender"])) {
    $genderErr = "gender is required";
    }else{
    	$gender=$_POST['gender'];
    }


if (empty($_POST["email"])) {
    $emailErr = "email is required";
    }else{
    	$email=$_POST['email'];
    }


 if (empty($_POST["phone"])) {
    $phoneErr = "contact num is required";
    }else{
    	$phone=$_POST['phone'];
    }



$description=$_POST['description'];

if($name==true and $age==true and $email==true and $gender==true and $phone==true)
{
$sql="INSERT INTO `trip`.`form` (`name`, `age`, `gender`, `email`, `phone`, `other`, `dd`) VALUES ( '$name', '$age', '$gender', '$email', '$phone', '$description', current_timestamp());";


//echo $sql;

//***execute the query**************
if($con->query($sql)==true){
	//echo "success insert";
}
else{
	//echo "error: $sql <br> $con->error";

}
}
else{
	$message="Fill all the required categories!!";
}





//**********close the connection************
$con->close();

}
?>





<!DOCTYPE html>
<html lang="en">
<head>
	<title>Welcome to Travel Form</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<img class="backg" src="images/bg.jpg" alt="DYPCOE">
	<div class="container">
		<h1>Welcome to DYPCOE Manali trip form!</h1>
		<p>Enter the details and submit the form to confirm your seats</p>
		<p class="errMessage"><?php
		echo $message
		?></p>

		<form action="index.php" method="POST" >
			<input type="text" name="name" placeholder="Enter your name" id="name"><span class="error">* <?php echo $nameErr;?></span><br>

			<input type="text" name="age" placeholder="Enter your age" id="age"><span class="error">* <br><?php echo $ageErr;?></span><br>

			<input type="text" name="gender" id="gender" placeholder="Enter your gender"><span class="error">* <?php echo $genderErr;?></span><br>

			<input type="email" name="email" placeholder="Enter your mail-id" id="email"><span class="error">* <?php echo $emailErr;?></span><br>

			<input type="phone" name="phone" id="phone" placeholder="Enter your contact number"><span class="error">* <?php echo $phoneErr;?></span><br>

			<textarea name="description" id="description" cols="10" rows="30" placeholder="Enter any other information"></textarea>
			<br>

			<button onclick="myFunction()"class="btn">Submit</button>
			<!-- <button class="btn">Reset</button> -->
		</form>
	</div>
	<script type="text/javascript" src="index.js"></script>

	

</body>
</html>