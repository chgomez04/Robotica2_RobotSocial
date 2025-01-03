#include <Servo.h>
#include <Adafruit_NeoPixel.h>
//#include <rp2040_pio.h>

#define PIN 3
#define Numpix 64

Adafruit_NeoPixel pixel = Adafruit_NeoPixel(Numpix, PIN, NEO_RGB + NEO_KHZ800);


String cadena;
//Inicio de posición de los motores (Estado inicial del Robot HOME)
int pos0 = 90;
int pos1 = 45;
int pos2 = 135;

Servo myservo0;
Servo myservo1;
Servo myservo2;

boolean var=false;
int veces=0;

void setup() {
Serial.begin(9600);
delay(30);

//Se inicializa los pines que van a controlar los servomotores
 myservo0.attach(11);  //Servo 0 - Base
 myservo1.attach(10); //Servo 1 - izquierda
 myservo2.attach(9); //Servo 2 - derecho
 
 myservo0.write(pos0);
 myservo1.write(pos1);
 myservo2.write(pos2);
 delay(5);

 pixel.begin();
}
void loop() {
  
  //Lectura para el Serial
  if(Serial.available()){
    cadena="";
    cadena= Serial.readString();
    fnActuadores(cadena); //Si hay algo en el serial se ejecuta la funcion fnActuadores
    
    }
}

void fnActuadores(String cad){   // Cada valor que venga desde python tendrá una etiqueta 
  String label;
  String value;
  int pos;
  cad.trim(); //Elimina los espacios en blanco(todos los caracteres sin contenido "espacio, tabulación, etc.") en ambos extremos del string
  cad.toLowerCase();  //Este método devuelve el valor de la cadena convertida a minúsculas. No afecta al valor de la cadena en sí misma.
  pos = cad.indexOf(':'); //retorna el índice en el que se puede encontrar un ':', ó retorna -1 si ':' no esta presente.
  label= cad.substring(0,pos); //extrae caracteres desde 0 (indiceA) hasta pos(indiceB) sin incluirlo
  value= cad.substring(pos+1); //Como se omite el indiceB, substring extrae caracteres hasta el final de la cadena.
  //Serial.println(label);


  if (label.equals("mot")){
    mov_all_motors(value);
  }

}

void mov_all_motors(String value){  
    int val0;
    int val1;
    int val2;
    int val3;
    int pos;
    
    pos = value.indexOf(','); //retorna el índice en el que se puede encontrar una ',', ó retorna -1 si ',' no esta presente.
    String m0 = value.substring(0,pos); //extrae caracteres desde 0 (indiceA) hasta pos(indiceB) sin incluirlo
    val0 = m0.toInt(); //Convierte value(un string) en un número entero
    //val = map(val, -90, 90, 0, 180); //Se mapea el valor del servo motor pasando de -90 a 90 s valores positivos entre 0 y 180
    myservo0.write(val0);   //Se escribe el valor o ángulo de pos0 en el servomotor
    
    
    value = value.substring(pos+1);
    pos = value.indexOf(','); 
    String m1 = value.substring(0,pos);
    val1 = m1.toInt();
    //val = map(val, 0, 180, 0, 180);
    myservo1.write(val1);
    

    value = value.substring(pos+1);
    pos = value.indexOf(',');
    String m2 = value.substring(0,pos);
    val2 = m2.toInt();
    //val = map(val, -90, 90, 0, 180);
    myservo2.write(val2);

    value = value.substring(pos+1);
    pos = value.indexOf(',');
    String m3 = value.substring(0,pos);
    val3 = m3.toInt();
    //val = map(val, -90, 90, 0, 180);
    if (val3 == 1)
    {
      pixel.clear();
      rostroNormal();
      
    }
    if (val3 == 2)
    {
      pixel.clear();
      rostrofeliz(); 
    }
    if (val3 == 3)
    {
      pixel.clear();
      rostroAsombrado();
    }
   
    Serial.println("fin");
     
}

void rostroNormal()
{
  //Cejas
 pixel.setPixelColor(56,pixel.Color(20,0,0));
 pixel.setPixelColor(40,pixel.Color(20,0,0));
 pixel.setPixelColor(55,pixel.Color(20,0,0));
 pixel.setPixelColor(7,pixel.Color(20,0,0));
 pixel.setPixelColor(8,pixel.Color(20,0,0));
 pixel.setPixelColor(23,pixel.Color(20,0,0));
 //Ojos
 pixel.setPixelColor(10,pixel.Color(20,0,0));
 pixel.setPixelColor(11,pixel.Color(20,0,0));
 pixel.setPixelColor(21,pixel.Color(20,0,0));
 pixel.setPixelColor(20,pixel.Color(20,0,0));
 pixel.setPixelColor(52,pixel.Color(20,0,0));
 pixel.setPixelColor(53,pixel.Color(20,0,0));
 pixel.setPixelColor(42,pixel.Color(20,0,0));
 pixel.setPixelColor(43,pixel.Color(20,0,0));
 //Boca
 pixel.setPixelColor(14,pixel.Color(20,0,0));
 pixel.setPixelColor(17,pixel.Color(20,0,0));
 pixel.setPixelColor(30,pixel.Color(20,0,0));
 pixel.setPixelColor(33,pixel.Color(20,0,0));
 pixel.setPixelColor(46,pixel.Color(20,0,0));
 pixel.setPixelColor(49,pixel.Color(20,0,0));
 pixel.show();
}


void rostroAsombrado()
{
  //Cejas
 pixel.setPixelColor(57,pixel.Color(20,0,0));
 pixel.setPixelColor(40,pixel.Color(20,0,0));
 pixel.setPixelColor(55,pixel.Color(20,0,0));
 pixel.setPixelColor(6,pixel.Color(20,0,0));
 pixel.setPixelColor(8,pixel.Color(20,0,0));
 pixel.setPixelColor(23,pixel.Color(20,0,0));
 //Ojos
 pixel.setPixelColor(10,pixel.Color(20,0,0));
 pixel.setPixelColor(11,pixel.Color(20,0,0));
 pixel.setPixelColor(21,pixel.Color(20,0,0));
 pixel.setPixelColor(20,pixel.Color(20,0,0));
 pixel.setPixelColor(52,pixel.Color(20,0,0));
 pixel.setPixelColor(53,pixel.Color(20,0,0));
 pixel.setPixelColor(42,pixel.Color(20,0,0));
 pixel.setPixelColor(43,pixel.Color(20,0,0));
 //Boca
 pixel.setPixelColor(29,pixel.Color(20,0,0));
 pixel.setPixelColor(31,pixel.Color(20,0,0));
 pixel.setPixelColor(32,pixel.Color(20,0,0));
 pixel.setPixelColor(34,pixel.Color(20,0,0));
 pixel.setPixelColor(17,pixel.Color(20,0,0));
 pixel.setPixelColor(46,pixel.Color(20,0,0));
 pixel.show();
}

void rostrofeliz()
{
  //Cejas
 pixel.setPixelColor(57,pixel.Color(20,0,0));
 pixel.setPixelColor(40,pixel.Color(20,0,0));
 pixel.setPixelColor(55,pixel.Color(20,0,0));
 pixel.setPixelColor(6,pixel.Color(20,0,0));
 pixel.setPixelColor(8,pixel.Color(20,0,0));
 pixel.setPixelColor(23,pixel.Color(20,0,0));
 //Ojos
 pixel.setPixelColor(10,pixel.Color(20,0,0));
 pixel.setPixelColor(11,pixel.Color(20,0,0));
 pixel.setPixelColor(21,pixel.Color(20,0,0));
 pixel.setPixelColor(20,pixel.Color(20,0,0));
 pixel.setPixelColor(52,pixel.Color(20,0,0));
 pixel.setPixelColor(53,pixel.Color(20,0,0));
 pixel.setPixelColor(42,pixel.Color(20,0,0));
 pixel.setPixelColor(43,pixel.Color(20,0,0));
 //Boca
 pixel.setPixelColor(2,pixel.Color(20,0,0));
 pixel.setPixelColor(14,pixel.Color(20,0,0));
 pixel.setPixelColor(16,pixel.Color(20,0,0));
 pixel.setPixelColor(31,pixel.Color(20,0,0));
 pixel.setPixelColor(32,pixel.Color(20,0,0));
 pixel.setPixelColor(47,pixel.Color(20,0,0));
 pixel.setPixelColor(49,pixel.Color(20,0,0));
 pixel.setPixelColor(61,pixel.Color(20,0,0));
 pixel.show();
}
