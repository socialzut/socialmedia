
<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('teamproject:static/pyramid-16x16.png')}">

    <title>Zadania dla was</title>

    <!-- Bootstrap core CSS -->
    <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('teamproject:static/theme.css')}" rel="stylesheet">

  </head>

  <body>
    <h2>Zadania dla was:</h2>
    <hr>
    % for task in tasks:
      <h2>Zadanie ${loop.index+1}</h2>
      <p>${task['contents'].decode('utf-8')}</p>
      <ul>
      % for element in task['elements']:
        <li>${element.decode('utf-8')}</li>
      % endfor
      </ul>
      <p>${task['summary'].decode('utf-8')}
    % endfor
  </body>
</html>
