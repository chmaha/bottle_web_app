<html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="styles.css" />
        <title>WHOIS Results</title>
    </head>
    <style>
        h3 {font-family: 'Montserrat', sans-serif;}
    </style>
    <body>
        <h3>Result:</h3>
        <pre>{{pretty_whois}}</pre>
        <input type="button" value="Return to previous page" onclick="history.back()"/> 
    </body>
</html>