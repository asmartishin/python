Simplifying. But remember that `yield` is a `generator`  
1) Insert a line `result = []` at the start of the function.  
2) Replace each `yield expr` with `result.append(expr)`.  
3) Insert a line `return result` at the bottom of the function.  
4) Yay - no more `yield` statements! Read and figure out code.  
5) Compare function to original definition.
