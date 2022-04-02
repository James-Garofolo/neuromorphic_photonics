#include "Arduino.h"

int sample = 0, sample_not = 1, drain = 2, latch = 3; // digital pins

int sampled = 0, latched = 1, current = 2


int sample_current(){
  digitalWrite(sample_not, LOW);
  digitalWrite(sample, HIGH);
  digitalWrite(sample, LOW);
  digitalWrite(sample_not, HIGH);

  return analogRead(sampled);
}

void latch(int match_to){
  int latched_val;
  digital 
  do{
    latched_val = analogRead(latched);
  } while (latched_val != match_to);
}

void drain(){
  int sample_v;
  do{
    sample_v = analogRead(sampled);
  } while (sample_v > 0);
}

void setup() {
  pinMode(sample, OUTPUT);
  pinMode(sample_not, OUTPUT);
  pinMode(drain, OUTPUT);
  pinMode(latch, OUTPUT);
  
}

void loop() {
    digitalWrite(led, HIGH);
    digitalWrite(led, LOW);
}
