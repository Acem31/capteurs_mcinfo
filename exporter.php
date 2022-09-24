<?php
query($query);
$items = array();


while( $row = $result->fetch_assoc() ) {
$items[] = $row;
}

if(isset($_POST["export"])) {
//Define the filename with current date
$fileName = "itemdata-".date('d-m-Y').".xls";


header('Content-Type: application/vnd.ms-excel');
header('Content-Disposition: attachment; filename='.$fileName);

$heading = false;

if(!empty($items)) {
foreach($items as $item) {
if(!$heading) {
echo implode("\t", array_keys($item)) . "\n";
$heading = true;
}
echo implode("\t", array_values($item)) . "\n";
}
}
exit();
}

?>