# Autoinput
This library is for easier input in Python. It is 100% that you don't want to do this:

```Python
while 1:
  try:
    x = int(input())
    break
  except:
    print("Please input a number")
```

because it is 6 lines when you can have 1 line:

```Python
x = autoinput("", autoinput_type.INTEGER)
```

and everything is inside the function. No work by hands.

## how to use
Here is the definition

```Python
def autoinput(outstring: str, typeel, pipe_in: Callable[[str], str]=input, pipe_out: Callable[[str], None]=print, pipe_out_end_name: str="end", pipe_out_flush_name: str="flush", parser=None) -> Any:
```

First argument  - `outstring`, string to show.

Second argument - `typeel`, use autoinput_type enum to form this (example: `autoinput_type.INTEGER | autoinput_type.ARRAY`)

kwargs:

  `pipe_in`  - for custom input function (for example if you use GUI)
  
  `pipe_out` - for custom output function
  
  `parser`   - for custom parser (don't use with `autoinput_type` except of `autoinput_type.ARRAY`)
  
  `pipe_out_end_name`   - if your custom output function doesn't have parameter like `print`'s `end` use `None`, if has but called not `end` use the parameter to specify the name.
  
  `pipe_out_flush_name` - the same as `pipe_out_end_name` but for flush.
