#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <jvcr_ecm_01/machine.h>
#include <jvcr_ecm_01_python/jvcr.h>

static PyObject *updateFunc;
static PyObject *initFunc;

static void update(Jvcr *machine, double delta) {
  PyObject* args = PyTuple_New(1);
  PyObject* value = PyFloat_FromDouble(delta);
  PyTuple_SetItem(args, 0, value);
  PyObject_CallObject(updateFunc, args);
  if (PyErr_Occurred()) PyErr_Print();
}

static void init(Jvcr *machine) {
  if (!initFunc) {
    printf("WARNING. There is no init function\n");
    return;
  }
  PyObject_CallObject(initFunc, NULL);
  if (PyErr_Occurred()) PyErr_Print();
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    fprintf(stderr, "Usage: python dir_path\n");
    return 1;
  }

  char *name = "main";

  PyImport_AppendInittab("jvcr", &PyInit_jvcr);

  Py_Initialize();
  char *code = malloc(sizeof(char) * (33 + strlen(argv[1])));
  sprintf(code, "import sys\nsys.path.insert(0, \"%s\")", argv[1]);
  PyRun_SimpleString(code);

  PyObject *pName = PyUnicode_DecodeFSDefault(name);
  PyObject *pModule = PyImport_Import(pName);
  Py_DECREF(pName);

  if (pModule == NULL) {
    PyErr_Print();
    fprintf(stderr, "Failed to load \"%s\"\n", name);
    return 1;
  }

  updateFunc = PyObject_GetAttrString(pModule, "update");
  if (!updateFunc || !PyCallable_Check(updateFunc)) {
    if (PyErr_Occurred()) PyErr_Print();
    fprintf(stderr, "Cannot find function 'update'\n");
    return 1;
  }

  initFunc = PyObject_GetAttrString(pModule, "init");
  if (!initFunc || !PyCallable_Check(initFunc)) {
    if (PyErr_Occurred()) PyErr_Print();
    fprintf(stderr, "Cannot find function 'init'\n");
    initFunc = NULL;
//    return 1;
  }

  RunMachine(&update, &init);

  Py_XDECREF(updateFunc);
  Py_DECREF(pModule);

  Py_Finalize();
  return 0;
}