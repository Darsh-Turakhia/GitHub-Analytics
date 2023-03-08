<!DOCTYPE html>
<html>
<head>
  <title>Issues Table</title>
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
  position: relative;
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
  <a href="../Github Analytics/Year Table.php">Year Wise</a>
</nav>

<br><br><br><br><br><br><br>

</body>
</html>

<?php
$con = mysqli_connect("localhost","root","","dmw");
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$lang = "0";

if(!isset($_POST['lang']))
  {
    $lang= "%";
  }
else
  {
    $lang= $_POST['lang'];
    if ($_POST['lang'] == '%') {
      $query = "SELECT * FROM issues";
    }
    else{
      $query = "SELECT * FROM issues where `Sr. No.` = '".$lang."'";
    }
  }


$result = mysqli_query($con,$query);
echo "<center><table border='1'>
<tr>
<th>Language</th>
<th>YR-2011</th>
<th>YR-2012</th>
<th>YR-2013</th>
<th>YR-2014</th>
<th>YR-2015</th>
<th>YR-2016</th>
<th>YR-2017</th>
<th>YR-2018</th>
<th>YR-2019</th>
<th>YR-2020</th>
<th>YR-2021</th>
<th>Grand Total</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['Language'] . "</td>";
echo "<td>" . $row['YR-2011'] . "</td>";
echo "<td>" . $row['YR-2012'] . "</td>";
echo "<td>" . $row['YR-2013'] . "</td>";
echo "<td>" . $row['YR-2014'] . "</td>";
echo "<td>" . $row['YR-2015'] . "</td>";
echo "<td>" . $row['YR-2016'] . "</td>";
echo "<td>" . $row['YR-2017'] . "</td>";
echo "<td>" . $row['YR-2018'] . "</td>";
echo "<td>" . $row['YR-2019'] . "</td>";
echo "<td>" . $row['YR-2020'] . "</td>";
echo "<td>" . $row['YR-2021'] . "</td>";
echo "<td>" . $row['Grand Total'] . "</td>";
echo "</tr>";
}
echo "</table></center>";

mysqli_close($con);
?>