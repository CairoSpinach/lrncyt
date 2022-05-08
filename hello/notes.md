## Questions

- how to integrate `bat` file in setup script
- usage with numpy array
- cython language specifics: 
  * `def` vs `cdef` vs `cpdef`
  * how is ptr used?


## Takeaways
- almost all tutorials starts by saying you need a `.pyx` for writing cython code, `setup.py` to streamline
  building, and something like `main.py` to import the cython function and use it
- From the workflow, it looks like **numba** is much better integrated and. It even allows for parallel. 
  Just importing (reloading) takes a bit of time to compile code 