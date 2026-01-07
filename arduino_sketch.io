const int pedalPin = 2;
int ultimoEstado = HIGH;

void setup() {
  pinMode(pedalPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int estadoActual = digitalRead(pedalPin);
  if (estadoActual != ultimoEstado) {
    if (estadoActual == LOW) {
      Serial.println("PULSADO");
    }
    delay(50);
  }
  ultimoEstado = estadoActual;
}
