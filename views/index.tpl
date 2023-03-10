<html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
        <link type="text/css" rel="stylesheet" href="styles.css" />
        <title>WHOIS Web Application</title>
    </head>
    <style>
        h3 {font-family: 'Montserrat', sans-serif;}
    </style>
    <body>
         <h3>Please enter an IP address or domain name:</h3>
         <form method="post" action="/result">
             <input type="text" name="address">
             <button type="submit">Submit</button>
         </form>
    </body>
</html>