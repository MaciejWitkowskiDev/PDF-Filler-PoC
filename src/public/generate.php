<?php

include_once('Logger.php');

function generatePdf($form, $fields){
    $path = "/opt/pdf-generator/generate_pdf.py";
    $form = escapeshellcmd($form);
    $command_string = "python3 $path ".$form." ";
    foreach ($fields as $key => $value) {
        $key = escapeshellcmd($key);
        $value = escapeshellcmd($value);
        $command_string .= $key.":".$value." ";
    }
    $command_string = escapeshellcmd($command_string);
    ob_start();
    passthru($command_string);
    $output = ob_get_clean();
    $response = json_decode($output, true);
    if($response["status"] == 1){
        throw new Exception($response["message"]);
    } else {
        $fileContent = base64_decode($response["response_body"]);
        header('Content-Type: application/pdf');
        header('Content-Length: '.strlen( $fileContent ));
        header('Content-disposition: attachment; filename="' . str_replace("-L", "", $form) . '.pdf"');
        header('Cache-Control: public, must-revalidate, max-age=0');
        header('Pragma: public');
        Logger::info("Generated a ".$form." with no errors.",$fields);
        echo $fileContent;
    }
}

function main(){
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

    try {
        if(isset($cel) && isset($krs)){
            generatePdf($file, array(
                'rok' => $year,
                'krs' => $krs,
                'cel' => rawurlencode($cel),
                'agreement' => 'Tak'
            ));
        } else if(isset($cel)) {
            generatePdf($file, array(
                'rok' => $year,
                'cel' => rawurlencode($cel),
                'agreement' => 'Tak'
            ));
        } else {
            generatePdf($file, array(
                'rok' => $year,
            ));
        }
    }
    #TBD: unify exceptions
    catch (exception $e) {
        http_response_code(404);
        Logger::error("COULDNT GENERATE FILE: generate.php error. Received exception: ",$e);
        error_log("COULDNT GENERATE FILE: generate.php error. Received exception:".$e);
        die('Coś poszło nie tak! Prosimy spróbować ponownie później.');
    }

    flush(); // This is essential for large downloads
}

main();
?>
