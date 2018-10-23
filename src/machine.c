#include <jvcr_ecm_01/machine.h>
#include <stdlib.h>
#include <stdio.h>

Jvcr *NewJvcr() {
  Jvcr *machine = (Jvcr *) malloc(sizeof(Jvcr));
  machine->ram = NewJvcrRam();
  machine->display = NewJvcrDisplay();
  printf("Jvcr machine is created: allocated %d bytes\n", RAM_SIZE);
  OnInit(machine);
  return machine;
}

void DestroyJvcr(Jvcr *machine) {
  OnDestroy(machine);
  DestroyJvcrRam(machine->ram);
  DestroyJvcrDisplay(machine->display);
  free(machine);
  printf("Jvcr machine is destroyed\n");
}

JvcrRam *NewJvcrRam() {
  JvcrRam *ram = (JvcrRam *) malloc(sizeof(JvcrRam));
  ram->memory = (byte *) calloc(sizeof(byte), RAM_SIZE);
  return ram;
}
void DestroyJvcrRam(JvcrRam *ram) {
  free(ram->memory);
  free(ram);
}

JvcrDisplay *NewJvcrDisplay() {
  JvcrDisplay *display = (JvcrDisplay *) malloc(sizeof(JvcrDisplay));
  display->texture = (byte *) calloc(sizeof(byte), DISPLAY_WIDTH * DISPLAY_HEIGHT * DISPLAY_CHANNELS);
  return display;
}
void DestroyJvcrDisplay(JvcrDisplay *display) {
  free(display->texture);
  free(display);
}