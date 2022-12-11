def web_page(state,writing):
    rover_state = state
    if writing == 1:
        log_state = 'Recording'
    else:
        log_state = 'Not recording'
    html = """<html>
    <head>
        <title>ESP32 Rover</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; text-align: center; margin:0px auto; padding-top: 30px;}
            table { margin-left: auto; margin-right: auto; }
            td { padding: 0 px; }
            .button {
                -webkit-border-radius: 20;
                -moz-border-radius: 20;
                border-radius: 20px;
                background-color: #3B4153;
                border: none;
                color: white;
                padding: 15px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 18px;
                font-weight : bold;
                margin: 6px 0px;
                cursor: pointer;
                -webkit-touch-callout: none;
                -webkit-user-select: none;
                -khtml-user-select: none;
                -moz-user-select: none;
                -ms-user-select: none;
                user-select: none;
                -webkit-tap-highlight-color: rgba(0,0,0,0);
            }
            button:active {
                background:#59cbcf;
            }
            .button_invisible {
                background: transparent;
                border: none;
            }
            .button_invisible:active {
                background: transparent;
            }
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
        <h4>Rover v1.0  -  UI v1.6</h4>
        <p><strong>STATE: """ + rover_state + """     LOG: """ + log_state + """</strong></p>
        <table>
            <tr><td colspan="3" align="center"><button class="button" onmousedown="changeButtonColor();toggleCheckbox('forward');" ontouchstart="changeButtonColor();toggleCheckbox('forward');" onmouseup="toggleCheckbox('buttonstop');" ontouchend="toggleCheckbox('buttonstop');"><div class="triangle-up"></div></button></td></tr>
            <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('left');" ontouchstart="toggleCheckbox('left');" onmouseup="toggleCheckbox('buttonstop');" ontouchend="toggleCheckbox('buttonstop');"><div class="triangle-left"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('stop');" ontouchstart="toggleCheckbox('stop');"><div class="square"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('right');" ontouchstart="toggleCheckbox('right');" onmouseup="toggleCheckbox('buttonstop');" ontouchend="toggleCheckbox('buttonstop');"><div class="triangle-right"></div></button></td></tr>
            <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('backward');" ontouchstart="toggleCheckbox('backward');" onmouseup="toggleCheckbox('buttonstop');" ontouchend="toggleCheckbox('buttonstop');"><div class="triangle-down"></div></button></td></tr>                   
            <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('enable');window.location.reload();" ontouchstart="toggleCheckbox('enable');window.location.reload();";">ENABLE</div></button></td><td align="center"><button class="button_invisible" </button></td><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('disable');window.location.reload();" ontouchstart="toggleCheckbox('disable')window.location.reload();;";">DISABLE</div></button></td></tr>
            <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('start_rec');window.location.reload();" ontouchstart="toggleCheckbox('start_rec');window.location.reload();";">START LOG</div></button></td><td align="center"><button class="button_invisible" </button></td><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('stop_rec');window.location.reload();" ontouchstart="toggleCheckbox('stop_rec');window.location.reload();";">STOP LOG</div></button></td></tr>
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