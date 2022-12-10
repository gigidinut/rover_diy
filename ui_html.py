def web_page(state):
    rover_state = state
    print('State inside the web page: ' + rover_state)
    html = """<html>
      <head>
        <title>ESP32 Rover</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
          body { font-family: Arial; text-align: center; margin:0px auto; padding-top: 30px;}
          table { margin-left: auto; margin-right: auto; }
          td { padding: 0 px; }
          .button {
            -webkit-border-radius: 28;
            -moz-border-radius: 28;
            border-radius: 28px;
            background-color: #3B4153;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            margin: 6px 3px;
            cursor: pointer;
            -webkit-touch-callout: none;
            -webkit-user-select: none;
            -khtml-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            -webkit-tap-highlight-color: rgba(0,0,0,0);
        }
        .button:active {
        background-color: #8695c2;
        .triangle-up {
        width: 0;
        height: 0;
        border-left: 25px solid transparent;
        border-right: 25px solid transparent;
        border-bottom: 50px solid #7DF9FF;
        }
        .triangle-down {
            width: 0;
            height: 0;
            border-left: 25px solid transparent;
            border-right: 25px solid transparent;
            border-top: 50px solid #7DF9FF;
        }
        .triangle-left {
            width: 0;
            height: 0;
            border-top: 25px solid transparent;
            border-right: 50px solid #7DF9FF;
            border-bottom: 25px solid transparent;
        }
        .triangle-right {
            width: 0;
            height: 0;
            border-top: 25px solid transparent;
            border-left: 50px solid #7DF9FF;
            border-bottom: 25px solid transparent;
        }
        .square {
          height: 50px;
          width: 50px;
          background-color: #FF3131;
        }
        </style>
      </head>
      <body style="background-color:#D8DBF1;">
        <h2>Rover v1.0</h2>
        <h3>UI v1.5</h3>
        <p>Rover: <strong>""" + rover_state + """</strong></p>
        <table>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('forward');" ontouchstart="toggleCheckbox('forward');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-up"></div></button></td></tr>
          <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('left');" ontouchstart="toggleCheckbox('left');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-left"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('stop');" ontouchstart="toggleCheckbox('stop');"><div class="square"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('right');" ontouchstart="toggleCheckbox('right');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-right"></div></button></td></tr>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('backward');" ontouchstart="toggleCheckbox('backward');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-down"></div></button></td></tr>                   
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('enable');window.location.reload();" ontouchstart="toggleCheckbox('enable');window.location.reload();";">ENABLE</div></button></td></tr>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('disable');window.location.reload();" ontouchstart="toggleCheckbox('disable')window.location.reload();;";">DISABLE</div></button></td></tr>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('stop_rec');" ontouchstart="toggleCheckbox('stop_rec');";">STOP REC</div></button></td></tr>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('start_rec');" ontouchstart="toggleCheckbox('start_rec');";">START REC</div></button></td></tr>
        </table>
        <script>
       function toggleCheckbox(x) {
         var xhr = new XMLHttpRequest();
         xhr.open("GET", "/?" + x, true);
         xhr.send();
       }
      </script>
       </body>
    </html>"""
    return html
