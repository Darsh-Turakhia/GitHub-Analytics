<!DOCTYPE html>
<html>
<head>
	<title>Year Wise</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="shortcut icon" href="Icon.jpg" type="image/x-icon" />
	<style>
    @import url('https://fonts.googleapis.com/css?family=Oswald:500');
.bg{
  background-color: #90e0ef;
}
.thx{
  position: fixed;
  left:50%;
  transform:translateX(-50%);
  bottom: 15px;
}
nav{
  width: 100%;
  position: fixed;
  top:50px;
  text-align:center;
  
}
nav a{
  font-family: 'Oswald', sans-serif;
  font-weight:500;
  text-transform:uppercase;
  text-decoration:none;
  color:#16151b;
  margin:0 15px;
  font-size:16px;
  letter-spacing:1px;
  position:relative;
  display:inline-block;
}
nav a:before{
  content:'';
  position: absolute;
  width: 100%;
  height: 3px;
  background:#16151b;
  top:47%;
  animation:out 0.2s cubic-bezier(1, 0, 0.58, 0.97) 1 both;
}
nav a:hover:before{
  animation:in 0.2s cubic-bezier(1, 0, 0.58, 0.97) 1 both;

}
@keyframes in{
  0%{
    width: 0;
    left:0;
    right:auto;
  }
  100%{
    left:0;
    right:auto;
    width: 100%;
  }
}
@keyframes out{
  0%{
    width:100%;
    left: auto;
    right: 0;
  }
  100%{
    width: 0;
    left: auto;
    right: 0;
  }
}
@keyframes show{
  0%{
    opacity:0;
    transform:translateY(-10px);
  }
  100%{
    opacity:1;
    transform:translateY(0);
  }
}

@for $i from 1 through 5 {
  nav a:nth-child(#{$i}){
    animation:show .2s #{$i*0.1+1}s ease 1 both;
  }
}
.center {
  display: flex;
  justify-content: center;
  align-items: center;
  height:500px;
 }
 p.impact{
  font-family: Impact, Charcoal, sans-serif;
  font-size: 5em;
  color: rgb(0  ,0,0);
 }


.buttonClass {
  font-size:15px;
  font-family:Arial;
  width:140px;
  height:50px;
  border-width:1px;
  color:black;
  border-color:#84bbf3;
  font-weight:bold;
  border-top-left-radius:6px;
  border-top-right-radius:6px;
  border-bottom-left-radius:6px;
  border-bottom-right-radius:6px;
  box-shadow:inset 0px 1px 0px 0px #bbdaf7;
  text-shadow:inset 0px 1px 0px #528ecc;
  background:linear-gradient(#79bbff, #378de5);
}

.buttonClass:hover {
  background: linear-gradient(#378de5, #79bbff);
}

td {
  text-align: center;
}

</style>
</head>
<body class="bg">
<nav>
  <a href="../Github Analytics/home.html">Home</a>
  <a href="../Github Analytics/PRs Table.html">PRs</a>
  <a href="../Github Analytics/Issues Table.html">Issues</a>
  <a href="../Github Analytics/Repos Table.html">Repos</a>
</nav>
<br><br><br><br><br><br>
<center>
  <?php
    $con = mysqli_connect("localhost","root","","dmw");
    if (mysqli_connect_errno())
    {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
    }

    $query = "SELECT * FROM `year total`";


    $result = mysqli_query($con,$query);
    echo "<center><table border='1'>
    <tr>
    <th>Year</th>
    <th>Unique Languages in which Issues were raised</th>
    <th>Max Issues</th>
    <th>Language in which max Issues were raised</th>
    <th>Total Issues</th>
    <th>Unique Languages in which PRs were created</th>
    <th>Max PRs</th>
    <th>Language in which max PRs were created</th>
    <th>Total PRs</th>
    </tr>";

    while($row = mysqli_fetch_array($result))
    {
    echo "<tr>";
    echo "<td>" . $row['Year'] . "</td>";
    echo "<td>" . $row['Issue Lang'] . "</td>";
    echo "<td>" . $row['Max Issues'] . "</td>";
    echo "<td>" . $row['Max Issue Lang'] . "</td>";
    echo "<td>" . $row['Issues'] . "</td>";
    echo "<td>" . $row['PR Lang'] . "</td>";
    echo "<td>" . $row['Max PRs'] . "</td>";
    echo "<td>" . $row['Max PR Lang'] . "</td>";
    echo "<td>" . $row['PR'] . "</td>";
    echo "</tr>";
    }
    echo "</table></center>";

    mysqli_close($con);
  ?>
  <br><br><br><br><br><br><br><br>
  <a href="../Github Analytics/Issues per Year.png" target="_blank"><strong>Graphical View of Issues per Year</strong></a><br>
  <a href="../Github Analytics/Pull Requests per Year.png" target="_blank"><strong>Graphical View of Pull Requests per Year</strong></a><br>
  <a href="../Github Analytics/Languages in which issue were raised per Year.png" target="_blank"><strong>Graphical View of Languages in which issue were raised per Year per Year</strong></a><br>
  <a href="../Github Analytics/Languages in PRs were created per Year.png" target="_blank"><strong>Graphical View of Languages in PRs were created per Year per Year</strong></a><br>
  </center>
</body>
</html>