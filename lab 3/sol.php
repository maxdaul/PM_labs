<?php
ini_set('memory_limit', '-1');

function ApsSeq($str1, $str2)
{
    $ans = "";
    $min_len = 10 ** 5;
    for ($i = 0; $i < strlen($str1); $i++) {
        for ($j = 1; $j < $min_len && $j < strlen($str1) - $i; $j++) {
            if (!str_contains($str2, substr($str1, $i, $j))) {
                $min_len = $j;
                $ans = substr($str1, $i, $j);
                break;
            }
        }
    }
    return $ans;
}

function CommonSeq($str1, $str2)
{
    $ans = "";
    $min_len = 10**5;
    for ($i = 0; $i < strlen($str1); $i++) {
        for ($j = 1; $j < $min_len && $j < strlen($str1) - $i; $j++) {
            if (str_contains($str2, substr($str1, $i, $j))) {
                $min_len = $j;
                $ans = substr($str1, $i, $j);
                break;
            }
        }
    }
    return $ans;
}

function Common($str1, $str2)
{
    $dp = array_fill(0, strlen($str1)+1, array_fill(0, strlen($str2)+1, 0));
    for ($i = 1; $i < strlen($str1)+1; $i++) {
        for ($j = 1; $j < strlen($str2)+1; $j++) {
            $dp[$i][$j] = max($dp[$i-1][$j], $dp[$i][$j-1]);
            if ($str1[$i-1] == $str2[$j-1]) {
                $dp[$i][$j] = max($dp[$i-1][$j-1]+1, $dp[$i][$j]);
            }
        }
    }
    return $dp[strlen($str1)][strlen($str2)];
}

$str1 = file_get_contents("1.txt");
$str1 = str_replace(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n", "\r", " "], "", $str1);

$str2 = file_get_contents("2.txt");
$str2 = str_replace(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n", "\r", " "], "", $str2);

$str3 = file_get_contents("3.txt");
$str3 = str_replace(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n", "\r", " "], "", $str3);


$ans = ApsSeq($str1, $str2);
echo "Минимальная специфичная последовательность для (1), отсутствующая в (2): " . $ans . "\n";
$ans = ApsSeq($str2, $str1);
echo "Минимальная специфичная последовательность для (2), отсутствующая в (1): " . $ans . "\n";
$ans = CommonSeq($str1, $str2);
echo "Минимальная общая последовательность для (1) и (2): " . $ans . "\n";
$ans = ApsSeq($str1, $str3 . " " . $str2);
echo "Минимальная специфичная последовательность для (1), отсутствующая в (3) и (2): " . $ans . "\n";
$ans = ApsSeq($str3, $str1 . " " . $str2);
echo "Минимальная специфичная последовательность для (3), отсутствующая в (1) и (2): " . $ans . "\n";
$ans = Common($str1, $str2);
echo "Максимальная общая подпоследовательность для (1) и (3): " . $ans . "\n";
?>
