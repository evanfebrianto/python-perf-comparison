#include <Python.h>

static PyObject* sum_of_squares_c(PyObject* self, PyObject* args) {
    int n, i;
    long total = 0;

    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    for (i = 0; i < n; i++) {
        total += i * i;
    }

    return PyLong_FromLong(total);
}

static PyMethodDef SumOfSquaresMethods[] = {
    {"sum_of_squares_c", sum_of_squares_c, METH_VARARGS, "Calculate sum of squares"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sumofsquaresmodule = {
    PyModuleDef_HEAD_INIT,
    "sumofsquares",
    NULL,
    -1,
    SumOfSquaresMethods
};

PyMODINIT_FUNC PyInit_sumofsquares(void) {
    return PyModule_Create(&sumofsquaresmodule);
}
