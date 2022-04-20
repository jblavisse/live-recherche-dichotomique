<?php
$t = [3, 7, 11, 15, 22, 37];
$val = 37;

$trv = false;

$deb = 0;
$fin = count($t)-1;

$pos=-1;

while(!$trv && $deb <= $fin) {
    $mil = floor(($deb+$fin)/2);

    if($t[$mil] == $val) {
        $trv = true;
        $pos = $mil;
    }

    else if($t[$mil] < $val) {
        $deb = $mil+1;
    }

    else if($t[$mil] >$val) {
        $fin = $mil-1;
    }

}


echo $pos;