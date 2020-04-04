<?php

$ch = curl_init();
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_URL, 'http://www.rock-am-ring.com/lineup/');
$html = curl_exec($ch);
curl_close($ch);
preg_match_all("/bands\/(.*)' /m", $html, $band);
preg_match_all("/artist\/(.*)\)/m", $html, $cover);

foreach ($band[1] as $name) {
$name = preg_replace('/\'/', '', $name);
$name = preg_replace('/\//', '', $name);
$name = preg_replace('/-/', ' ', $name);
$name = mb_strtoupper($name, 'UTF-8');
$bands[] = $name;
}
foreach ($cover[1] as $image) {
$covers[] = $image;
}

foreach( $covers as $index => $image) {
echo 'name= '.$bands[$index].' logo= "https://assets.mlk-festivals.com/artist/'.$image.'"';
echo '<br>';
}
?>