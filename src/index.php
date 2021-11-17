<?php 
function generatePdf($form, $fields){
    $command_string = "python generate_pdf.py ".$form." ";
    foreach ($fields as $key => $value) {
        $command_string .= $key.":".$value." ";
    }
    $command_string = escapeshellcmd($command_string);
    ob_start();
    passthru($command_string);
    $output = ob_get_clean();
    $response = json_decode($output, true);
    if($response["status"] == 1){
        http_response_code(404);
        error_log("Python PDF generator error. Returned message: ".$response["message"]);
        die();
    } else {
        $fileContent = base64_decode($response["response_body"]);
        header('Content-Type: application/pdf');
        header('Content-Length: '.strlen( $fileContent ));
        header('Content-disposition: attachment; filename="' . $form . '.pdf"');
        #CONFIGURE THIS LATER
        header('Cache-Control: public, must-revalidate, max-age=0');
        header('Pragma: public');
        echo $fileContent;
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $file = $_POST["file"]; 
    if(isset($_POST["year"])) {
        $year = $_POST["year"];
    }
    if(isset($_POST["krs"])) {
        $krs = $_POST["krs"];
    }
    if(isset($_POST["cel"])) {
        $cel = $_POST["cel"];
    }
    
} else  {
    $file = $_GET["file"]; 
    if(isset($_GET["year"])) {
        $year = $_GET["year"];
    }
    if(isset($_GET["krs"])) {
        $krs = $_GET["krs"];
    }
    if(isset($_GET["cel"])) {
        $cel = $_GET["cel"];
    }
}

if(isset($cel) && isset($krs)){
    generatePdf($file, array(
        'rok' => $year,
        'krs' => $krs,
        'cel' => rawurlencode($cel),
        'agreement' => 'Tak'
    ));
} else {
    generatePdf($file, array(
        'rok' => $year,
    ));
}

flush(); // This is essential for large downloads 
?> 
