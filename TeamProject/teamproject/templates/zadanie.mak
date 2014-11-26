
<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('teamproject:static/pyramid-16x16.png')}">

    <title>Moje zadanie</title>

    <!-- Bootstrap core CSS -->
    <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('teamproject:static/theme.css')}" rel="stylesheet">

  </head>

  <body>
    <h1>
    % for zad in zadanie:
      <p>${zad['contents'].decode('utf-8')}</p>
      <ul>
        % for element in zad['elements']:
        <li>${element.decode('utf-8')}</li>
      % endfor
      </ul>
      <p>${zad['summary'].decode('utf-8')}</p>
    % endfor
    </h1>
    <br/>
    <form action="/zadanie" method="post" accept-charset="utf-8" enctype="multipart/form-data">

      <input id="pdf" name="pdf" type="file" value="" />

      <input name='submit' type="submit" value="submit" />
    </form>

  </body>
</html>
