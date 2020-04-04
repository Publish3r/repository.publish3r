<?php

$ch = curl_init();
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_URL, 'http://www.rock-am-ring.com/spielplan/');
$html = curl_exec($ch);
curl_close($ch);
preg_match_all("/data-name='(.*), Freitag, Volcano Stage/m", $html, $band);
foreach ($band[1] as $name) {
$name = preg_replace('/\'/', '', $name);
$name = preg_replace('/\//', '', $name);
$name = preg_replace('/-/', ' ', $name);
echo 'stage= Volcano Stage zeit= "" name= "'.$name.'" image= ""';
echo '<br>';
}
preg_match_all("/data-name='(.*), Freitag, Beck/m", $html, $band);
foreach ($band[1] as $name) {
$name = preg_replace('/\'/', '', $name);
$name = preg_replace('/\//', '', $name);
$name = preg_replace('/-/', ' ', $name);
echo 'stage= Beck\'s Crater Stage zeit= "" name= "'.$name.'" image= ""';
echo '<br>';
}
preg_match_all("/data-name='(.*), Freitag, Alternastage/m", $html, $band);
foreach ($band[1] as $name) {
$name = preg_replace('/\'/', '', $name);
$name = preg_replace('/\//', '', $name);
$name = preg_replace('/-/', ' ', $name);
echo 'stage= Alternastage zeit= "" name= "'.$name.'" image= ""';
echo '<br>';
}
?>