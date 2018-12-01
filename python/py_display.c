#include <jvcr_ecm_01/display.h>
#include <jvcr_ecm_01/render.h>
#include <jvcr_ecm_01/input.h>
#include <Python.h>
#include <jvcr_ecm_01_python/jvcr.h>
#include <jvcr_ecm_01_python/py_display.h>

PyObject *jvcr_cls(PyObject *self, PyObject *args) {
  byte color;
  PyArg_ParseTuple(args, "B", &color);
  cls(machine, color);
  Py_RETURN_NONE;
}

PyObject *jvcr_print(PyObject *self, PyObject *args) {
  char *str;
  float x;
  float y;
  byte color;
  PyArg_ParseTuple(args, "sffB", &str, &x, &y, &color);
  print(machine, str, (u32) x, (u32) y, color);
  Py_RETURN_NONE;
}

PyObject *jvcr_print_symbol(PyObject *self, PyObject *args) {
  char str;
  float x;
  float y;
  byte color;
  PyArg_ParseTuple(args, "CffB", &str, &x, &y, &color);
  print_symbol(machine, str, (u32) x, (u32) y, color);
  Py_RETURN_NONE;
}
PyObject *jvcr_pget(PyObject *self, PyObject *args) {
  float x;
  float y;
  PyArg_ParseTuple(args, "ff", &x, &y);
  byte pixel = pget(machine, (u32) x, (u32) y);
  return PyLong_FromLong(pixel);
}
PyObject *jvcr_pset(PyObject *self, PyObject *args) {
  float x;
  float y;
  byte color;
  PyArg_ParseTuple(args, "ffB", &x, &y, &color);
  pset(machine, (u32) x, (u32) y, (byte) color);
  Py_RETURN_NONE;
}
PyObject *jvcr_rectfill(PyObject *self, PyObject *args) {
  float x;
  float y;
  float w;
  float h;
  byte color;
  PyArg_ParseTuple(args, "ffffB", &x, &y, &w, &h, &color);
  rectfill(machine, (i32) x, (i32) y, (u32) w, (u32) h, color);
  Py_RETURN_NONE;
}
PyObject *jvcr_line(PyObject *self, PyObject *args) {
  float x0;
  float y0;
  float x1;
  float y1;
  byte color;
  PyArg_ParseTuple(args, "ffffB", &x0, &y0, &x1, &y1, &color);
  line(machine, (i32) x0, (i32) y0, (i32) x1, (i32) y1, color);
  Py_RETURN_NONE;
}
PyObject *jvcr_spr(PyObject *self, PyObject *args) {
  float screen_x;
  float screen_y;
  float sheet_x;
  float sheet_y;
  float width;
  float height;
  byte flip;
  byte rotate;
  byte scale;

  PyArg_ParseTuple(args, "ffffffBBB",
                   &screen_x,
                   &screen_y,
                   &sheet_x,
                   &sheet_y,
                   &width,
                   &height,
                   &flip,
                   &rotate,
                   &scale
  );
  spr(machine,
      (i32) screen_x,
      (i32) screen_y,
      (i32) sheet_x,
      (i32) sheet_y,
      (u32) width,
      (u32) height,
      flip,
      rotate,
      scale
  );
  Py_RETURN_NONE;
}
PyObject *jvcr_set_pallet(PyObject *self, PyObject *args) {
  byte color;
  byte red;
  byte green;
  byte blue;
  PyArg_ParseTuple(args, "BBBB", &color, &red, &green, &blue);
  set_pallet(machine, color, red, green, blue);
  Py_RETURN_NONE;
}
