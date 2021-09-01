<?php
$command = escapeshellcmd('python3 generate_pdf.py pit-example nip:123456');
ob_start();
passthru($command);
$output = ob_get_clean();
$test = json_decode($output, true);
$fileContent = $test["response_body"];
//var_dump($fileContent);
//file_put_contents('/var/www/html/px/public/pdfgen/dupsko.pdf', $fileContent);
//GET CONTENT
$fileToDownload = $fileContent;

//START DOWNLOAD
//header('Content-Description: File Transfer');
header('Content-Type: application/pdf');
//header('Content-Disposition: attachment; filename='.'dupsko.pdf');
//header('Content-Transfer-Encoding: binary');
//header('Expires: 0');
//header('Cache-Control: must-revalidate');
//header('Pragma: public');
//header('Content-Length: '. strlen($fileToDownload));
echo base64_decode($fileToDownload);
exit;
?>
