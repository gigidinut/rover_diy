def web_page(state,writing):
    rover_state = state
    if writing != 0:
        log_state = 'Recording'
    else:
        log_state = 'Not recording'
    html = """<html>
      <head>
        <title>ESP32-CAM Robot</title>
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
    <div id="page1">
        <h3>Rover v1.0 - UI v1.6</h3>
		<h3>Tracks Control</h3>
        <table>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('forward');" ontouchstart="toggleCheckbox('forward');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-up"></div></button></td></tr>
          <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('left');" ontouchstart="toggleCheckbox('left');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-left"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('stop');" ontouchstart="toggleCheckbox('stop');"><div class="square"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('right');" ontouchstart="toggleCheckbox('right');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-right"></div></button></td></tr>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('backward');" ontouchstart="toggleCheckbox('backward');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-down"></div></button></td></tr>                   
		  <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('enable');" ontouchstart="toggleCheckbox('enable');";">ENABLE</div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('stop_rec');" ontouchstart="toggleCheckbox('stop_rec');";">STOP REC</div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('disable');" ontouchstart="toggleCheckbox('disable');";">DISABLE</div></button></td></tr>
		  <tr><td colspan="3" align="center"><button class="button" onclick="showPage('page2');toggleCheckbox('arm_controls');" ontouchstart="showPage('page2');toggleCheckbox('arm_controls');"> ARM CONTROL </div></button></td></tr>
        </table>
    </div>

    <div id="page2" style="display:none">
        <h3>Rover v1.0 - UI v1.6</h3>
		<h3>Arm Control</h3>
		<!--
		<div>
        <label for="input1">Base angle:  </label>
        <input type="number" id="input1" name="input1" min="0" max="180" value="0" onchange="updateSlider('slider1', 'input1')">
        <input type="range" id="slider1" name="slider1" min="0" max="180" value="0" oninput="updateInput('input1', 'slider1')">
        <button onclick="sendInput('input1')">Send</button>
    </div>
        -->
    <div>
        <label for="input2">Join 1 angle:</label>
        <input type="number" id="input2" name="input2" min="0" max="180" value="90" oninput="updateSlider('slider2', 'input2')">
        <input type="range" id="slider2" name="slider2" min="0" max="180" value="90" oninput="updateInput('input2', 'slider2')" onmouseup="sendInput('input2')" ontouchend="sendInput('input2')">
        <button onclick="sendInput('input2')">Send</button>
    </div>

    <div>
        <label for="input3">Joint 2 angle:</label>
        <input type="number" id="input3" name="input3" min="0" max="180" value="90" oninput="updateSlider('slider3', 'input3')">
        <input type="range" id="slider3" name="slider3" min="0" max="180" value="00" oninput="updateInput('input3', 'slider3')" onmouseup="sendInput('input3')" ontouchend="sendInput('input3')">
        <button onclick="sendInput('input3')">Send</button>
    </div>

    <div>
        <label for="input4">Joint 3 angle:</label>
        <input type="number" id="input4" name="input4" min="0" max="180" value="90" oninput="updateSlider('slider4', 'input4')">
        <input type="range" id="slider4" name="slider4" min="0" max="180" value="90" oninput="updateInput('input4', 'slider4')" onmouseup="sendInput('input4')" ontouchend="sendInput('input4')">
        <button onclick="sendInput('input4')">Send</button>
    </div>

    <div>
        <label for="input5">Claw:</label>
        <input type="number" id="input5" name="input5" min="0" max="165" value="90" oninput="updateSlider('slider5', 'input5')">
        <input type="range" id="slider5" name="slider5" min="0" max="165" value="90" oninput="updateInput('input5', 'slider5')" onmouseup="sendInput('input5')" ontouchend="sendInput('input5')">
        <button onclick="sendInput('input5')">Send</button>
    </div>
        <button class="button" onclick="showPage('page1');toggleCheckbox('tracks_control');" ontouchstart="showPage('page1');toggleCheckbox('tracks_control');"> TRACKS CONTROL </div></button>
    </div>

    <script>
        function showPage(pageId) {
            document.getElementById("page1").style.display = "none";
            document.getElementById("page2").style.display = "none";
            document.getElementById(pageId).style.display = "block";
        }
		
		 function toggleCheckbox(x) {
         var xhr = new XMLHttpRequest();
         xhr.open("GET", "/?" + x, true);
         xhr.send();
       }
	   
	   function updateInput(inputId, sliderId) {
            document.getElementById(inputId).value = document.getElementById(sliderId).value;
        }
		
		function updateSlider(sliderId, inputId) {
        document.getElementById(inputId).value = document.getElementById(sliderId).value;
		}

        function sendInput(inputId) {
            var value = document.getElementById(inputId).value;
			var inputId = document.getElementById(inputId).name;
			var xhr = new XMLHttpRequest();
			xhr.open("POST", "/send-value", true);
			xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
			xhr.send(inputId + '#' +value);
			// alert("Sent: " + inputId + " Value: " + value);
            // TODO: Send value to server using AJAX or form submit.
            console.log("Input " + inputId + " value: " + value);
        }
    </script>
</body>
</html>"""
    return html
