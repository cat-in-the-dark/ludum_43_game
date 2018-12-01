#include <jvcr_ecm_01_python/py_import_sprites.h>
#include <jvcr_ecm_01/import_sprites.h>
#include <jvcr_ecm_01_python/jvcr.h>

PyObject *jvcr_import_sprites(PyObject *self, PyObject *args) {
  char *str;
  float offset;
  PyArg_ParseTuple(args, "sf", &str, &offset);

  import_sprites(machine, str, (ptr_t) offset);
  Py_RETURN_NONE;
}
