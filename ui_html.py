def web_page(state,writing):
    rover_state = state
    if writing != 0:
        log_state = 'Recording'
    else:
        log_state = 'Not recording'
    html = """<html>
      <head>
        <title>ROVER</title>
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
			border-bottom: 60px solid #7DF9FF;
        }
        .triangle-down {
            width: 0;
            height: 0;
            border-left: 25px solid transparent;
            border-right: 25px solid transparent;
            border-top: 60px solid #7DF9FF;
        }
        .triangle-left {
            width: 0;
            height: 0;
            border-top: 25px solid transparent;
            border-right: 60px solid #7DF9FF;
            border-bottom: 25px solid transparent;
        }
        .triangle-right {
            width: 0;
            height: 0;
            border-top: 25px solid transparent;
            border-left: 60px solid #7DF9FF;
            border-bottom: 25px solid transparent;
        }
        .square {
          height: 60px;
          width: 60px;
          background-color: #FF3131;
        }
		
		/* Define the styles for the arm elements */
		#shoulder_joint {
			width: 30px;
			height: 30px;
			border-radius: 70%;
			background-color: blue;
			position: absolute;
			top: calc(40% - 5px);
			left: calc(70% - 185px);
		}
		
		#elbow_joint {
			width: 30px;
			height: 30px;
			border-radius: 70%;
			background-color: blue;
			position: absolute;
			top: calc(40% - 5px);
			left: calc(70% - 185px + 75px);
		}
		
		#wrist_joint {
			width: 30px;
			height: 30px;
			border-radius: 70%;
			background-color: blue;
			position: absolute;
			top: calc(40% - 5px);
			left: calc(70% - 185px + 150px);
		}
	
		#upper_arm {
			width: 75px;
			height: 20px;
			background-color: red;
			position: absolute;
			top: 40%;
			left: calc(70% - 170px);
			transform-origin: 0% 50%;
		}
		
		#forearm {
			width: 75px;
			height: 20px;
			background-color: red;
			position: absolute;
			top: 40%;
			left: calc(70% - 170px + 75px);
			transform-origin: 0% 50%;
			}
			
		#claw {
			width: 0px;
			height: 0px;
			border-right: 30px solid transparent;
			border-top: 20px solid green;
			border-left: 65px solid green;
			border-bottom: 20px solid green;
			border-top-left-radius: 20px;
			border-top-right-radius: 30px;
			border-bottom-left-radius: 20px;
			border-bottom-right-radius: 30px;
			background-color: transparent;
			position: absolute;
			top: calc(40% - 10px);
			left: calc(70% - 170px + 150px);
			transform-origin: 0% 50%;
		}
			
		#ground {
			width: 100%;
			height: 5px;
			background-color: brown;
			position: absolute;
			top: calc(40% + 66px);
			left: 0%;
		}
			
		#rover {
			width: 210px;
			height: 80px;
			border-radius: 60px;
			outline-color:black;
			outline-width: 10px;
			outline-style: dashed;
			background-color: transparent;
			position: absolute;
			top: calc(40% - 25px);
			left: calc(70% - 350px);
		}
        </style>
      </head>
<body style="background-color:#D8DBF1;">
    <div id="page1">
        <h3>Rover v1.0 - UI v1.7</h3>
		<h3>Tracks Control</h3>
        <table>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('forward');" ontouchstart="toggleCheckbox('forward');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-up"></div></button></td></tr>
          <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('left');" ontouchstart="toggleCheckbox('left');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-left"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('stop');" ontouchstart="toggleCheckbox('stop');"><div class="square"></div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('right');" ontouchstart="toggleCheckbox('right');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-right"></div></button></td></tr>
          <tr><td colspan="3" align="center"><button class="button" onmousedown="toggleCheckbox('backward');" ontouchstart="toggleCheckbox('backward');" onmouseup="toggleCheckbox('stop');" ontouchend="toggleCheckbox('stop');"><div class="triangle-down"></div></button></td></tr>                   
		  <tr><td align="center"><button class="button" onmousedown="toggleCheckbox('enable');" ontouchstart="toggleCheckbox('enable');";">ENABLE</div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('stop_rec');" ontouchstart="toggleCheckbox('stop_rec');";">STOP REC</div></button></td><td align="center"><button class="button" onmousedown="toggleCheckbox('disable');" ontouchstart="toggleCheckbox('disable');";">DISABLE</div></button></td></tr>
		  <tr><td colspan="3" align="center"><button class="button" onclick="showPage('page2');toggleCheckbox('arm_controls');" ontouchstart="showPage('page2');toggleCheckbox('arm_controls');"> ARM CONTROL </button></td></tr>
        </table>
    </div>

    <div id="page2" style="display: none">
        <h3>Rover v1.0 - UI v1.7</h3>
		<h3>Arm Control</h3>
		
		<table style="position: absolute; top:60%; margin-left: 7%">
			<tr><td align="center">
			<div>
				<label for="input1">Shoulder angle:</label>
				<input type="number" id="input1" name="input1" min="0" max="180" value="0" oninput="updateslider('slider1', 'input1')" id="slider1">
				<input type="range" id="slider1" name="slider1" min="0" max="180" value="0" oninput="updateInput('input1', 'slider1')" onmouseup="sendInput('input1')" ontouchend="sendInput('input1')">
			</div>
			</td></tr>
			<tr><td align="center">
			<div>
				<label for="input2">Elbow angle:</label>
				<input type="number" id="input2" name="input2" min="0" max="180" value="90" oninput="updateslider('slider2', 'input2')" id="slider2">
				<input type="range" id="slider2" name="slider2" min="0" max="180" value="90" oninput="updateInput('input2', 'slider2')" onmouseup="sendInput('input2')" ontouchend="sendInput('input2')">
			</div>
			</td></tr>
			<tr><td align="center">
			<div>
				<label for="input3">Wrist angle:</label>
				<input type="number" id="input3" name="input3" min="0" max="180" value="90" oninput="updateslider('slider3', 'input3')" id="slider3">
				<input type="range" id="slider3" name="slider3" min="0" max="180" value="90" oninput="updateInput('input3', 'slider3')" onmouseup="sendInput('input3')" ontouchend="sendInput('input3')">
			</div>
			</td></tr>
			<tr><td align="center">
			<div>
				<label for="input4">Claw:</label>
				<input type="number" id="input4" name="input4" min="0" max="165" value="80" oninput="updateslider('slider4', 'input4')" id="slider4">
				<input type="range" id="slider4" name="slider4" min="0" max="165" value="80" oninput="updateInput('input4', 'slider4')" onmouseup="sendInput('input4')" ontouchend="sendInput('input4')">
			</div>
			</td></tr>
			<tr><td align="center">
				<button class="button" onclick="showPage('page1');toggleCheckbox('tracks_control');" ontouchstart="showPage('page1');toggleCheckbox('tracks_control');"> TRACKS CONTROL</button>
			</td></tr>
		</table>
	<div id="upper_arm"></div>
	<div id="forearm"></div>
	<div id="claw"></div>
	<div id="shoulder_joint"></div>
	<div id="elbow_joint"></div>
	<div id="wrist_joint"></div>
	<div id="ground"></div>
	<div id="rover"></div>
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
		
		// arm control functions
		
		const shoulder_joint = document.getElementById('shoulder_joint');
		const upper_arm = document.getElementById('upper_arm');
		const slider1 = document.getElementById('slider1');
		const slider2 = document.getElementById('slider2');
		const elbow_joint = document.getElementById('elbow_joint');
		const wrist_joint = document.getElementById('wrist_joint');
		const forearm = document.getElementById('forearm');
		const claw = document.getElementById('claw');
	
		function rotateupper_arm(angle) {
			upper_arm.style.transform = `rotate(${-angle}deg)`;
			updateElbowJointPosition(angle);
			updateForearmPosition(angle);
			forearm.style.transform = `rotate(${90-slider2.value-angle}deg)`;
			updateWristJointPosition();
			updateClawPosition();
			rotateclaw(angle);
		}
		
		function rotateforearm(angle) {
			forearm.style.transform = `rotate(${90-slider1.value-angle}deg)`;
			updateWristJointPosition();
			updateClawPosition();
			rotateclaw();
		}
		
		function rotateclaw(angle) {
			claw.style.transform = `rotate(${180 - slider2.value - slider1.value-slider3.value}deg)`;
		}
		
		function closeopenclaw(angle) {
			if (angle < 82) {
				claw.style.backgroundColor = 'transparent';
			} else {
				claw.style.backgroundColor = 'green';
			}
		}
		
		function updateClawPosition() {
			const claw = document.getElementById('claw');
			const forearm = document.getElementById('forearm');
			const styles = window.getComputedStyle(forearm);
			var a = 180 - slider1.value;
			var o = - slider2.value-180;
			var d = styles.getPropertyValue('width');
			var d = parseInt(d,10);
			var w = a + o/2 - 45;
			var l = 2 * d * Math.sin(((90 + o) / 2) * Math.PI / 180);
			var m = 2 * d * Math.sin(((90 + o) / 2) * Math.PI / 180) * Math.cos(w * Math.PI / 180);
			var h = 2 * d * Math.sin(((90 + o) / 2) * Math.PI / 180) * Math.sin(w * Math.PI / 180);
			
			// Set the position of the wrist joint relative to the center of the forearm
			claw.style.left = `calc(70% - ${m}px - 165px)`;
			claw.style.top = `calc(40% - ${h}px - 10px)`;
		}
		
		function updateForearmPosition(angle) {
			const forearm = document.getElementById('forearm');
			
			const forearmX = upper_arm.offsetWidth * Math.cos(angle * Math.PI / 180);
			const forearmY = upper_arm.offsetWidth * Math.sin(angle * Math.PI / 180) * -1;
			
			forearm.style.left = `calc(70% + ${forearmX}px - 170px)`;
			forearm.style.top = `calc(40% + ${forearmY}px)`;
		}
		
		function updateElbowJointPosition(angle) {
			const upper_arm = document.getElementById('upper_arm');
			const elbowJoint = document.getElementById('elbow_joint');
			
			// Calculate the position of the circle relative to the center of the line
			const circleX = upper_arm.offsetWidth * Math.cos(angle * Math.PI / 180);
			const circleY = upper_arm.offsetWidth * Math.sin(angle * Math.PI / 180) * -1;
			
			// Set the position of the circle relative to the center of the line
			elbowJoint.style.left = `calc(70% + ${circleX}px - 185px)`;
			elbowJoint.style.top = `calc(40% + ${circleY}px - 5px)`;
		}
		
		function updateWristJointPosition() {
			const wristJoint = document.getElementById('wrist_joint');
			const forearm = document.getElementById('forearm');
			const styles = window.getComputedStyle(forearm);
			var a = 180 - slider1.value;
			var o = - slider2.value-180;
			var d = styles.getPropertyValue('width');
			var d = parseInt(d,10);
			var w = a + o/2 - 45;
			var l = 2 * d * Math.sin(((90 + o) / 2) * Math.PI / 180);
			var m = 2 * d * Math.sin(((90 + o) / 2) * Math.PI / 180) * Math.cos(w * Math.PI / 180);
			var h = 2 * d * Math.sin(((90 + o) / 2) * Math.PI / 180) * Math.sin(w * Math.PI / 180);
			
			// Set the position of the wrist joint relative to the center of the forearm
			wristJoint.style.left = `calc(70% - ${m}px - 185px)`;
			wristJoint.style.top = `calc(40% - ${h}px - 5px)`;
		}
	
	
		slider1.addEventListener('input', () => {
			rotateupper_arm(slider1.value);
		});
		
		slider2.addEventListener('input', () => {
			rotateforearm(slider2.value);
		});
		
		slider3.addEventListener('input', () => {
			rotateclaw();
		});
		
		slider4.addEventListener('input', () => {
			closeopenclaw(slider4.value);
		});
    </script>
</body>
</html>"""
    return html
