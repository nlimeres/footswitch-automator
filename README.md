# footswitch-automator
Turning a piano sustain pedal into a macOS global shortcut.
This is a small util project to give my old piano sustain pedal a seccond life. 




## 🛠️ Hardware
- Arduino UNO (can be replaced by others)
- Piano pedal (or any type of pedal with Jack 1/4")
- USB Cable (serial connection)

- Protoboard (optional)


From the start, my goal was to keep the modification completely non-destructive. I wanted to avoid 'breaking' the pedal just in case I need it for its original purpose later.

Instead of cutting the cable, I wrapped jumper wires around the two sections of the TRS/TS jack: the Tip (signal) and the Sleeve (ground).

The Tip acts as the signal input (which we monitor via code), while the Sleeve provides the GND connection. The pedal effectively functions as a momentary switch.

he Arduino uses the internal `INPUT_PULLUP` resistor on Pin 2. The pedal acts as a momentary switch that pulls the signal to Ground when pressed.


![pedal-project-screenshoot](https://github.com/user-attachments/assets/aa82ebf7-bd5a-42f1-84ff-63b9cad48db5)

^^ This is the **working** mess i've done 😞

## Key Script Features:
* **Library:** Uses `pyautogui` for keyboard emulation and `pyserial` for communication.
* **Robustness:** Includes a `while True` loop with error handling to keep the script alive even if the USB is disconnected.

## ⚙️ Installation
1. You have to install this in your Arduino throw Arduino IDE. -> [arduino_sketch.io](https://github.com/nlimeres/footswitch-automator/arduino_sketch.ino)

arduino_sketch.ino
```
const int pedalPin = 2;
int lastStatus = HIGH;

void setup() {
  pinMode(pedalPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int actualStatus = digitalRead(pedalPin);
  if (actuaStatus != lastStatus) {
    if (actualStatus == LOW) {
      Serial.println("PRESSED");
    }
    delay(50);
  }
  lastStatus = actualStatus;
}
```

2. Instal your IDE (in my case, Thonny)
2. Connect your Arduino
3. Upload your code -> [main.py](https://github.com/nlimeres/footswitch-automator/main.py)
4. Modify `port` variable
5. Add the softkey you want to use. There are some of them already created down below

VARIANTS:
| File name    | Name        | Description  |
|--------------|-------------|--------------|
| [screenshoot.py](https://github.com/nlimeres/footswitch-automator/variants/screenshoot.py)      |   Screenshoot   | Take a screenshoot by just pressing the pedal       |
| [appswitcher.py](https://github.com/nlimeres/footswitch-automator/variants/appswitcher.py)       | App Switcher      | Switches to the most recent app just by running Cmd/Alt + Tab      |

Scheme:
```
[Pedal Mechanical Switch] 
      | (Physical signal)
      v
[Arduino Uno (Pin 2)] --> Logic: State Change Detection
      | (Serial Communication: "PRESSED")
      v
[Python Script (macOS)] --> Logic: String Matching
      | (PyAutoGUI Call)
      v
[macOS System (in my case)] --> Action: Press Spacebar
```


