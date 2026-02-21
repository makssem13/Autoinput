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
def autoinput(outstring: str,
              typeel,
              pipe_in: Callable[[str], str]=input,
              pipe_out: Callable[[str], None]=print,
              pipe_out_end_name: str="end",
              pipe_out_flush_name: str = "flush",
              use_input_argument_for_output: bool=True,
              parser=None) -> Any:
```

First argument  - `outstring`, string to show.

Second argument - `typeel`, use autoinput_type enum to form this (example: `autoinput_type.INTEGER | autoinput_type.ARRAY`)

kwargs:

  `pipe_in`  - for custom input function (for example if you use GUI)
  
  `pipe_out` - for custom output function
  
  `parser`   - for custom parser (don't use with `autoinput_type` except of `autoinput_type.ARRAY` and/or `autoinput_type.STRING`)
  
  `pipe_out_end_name`   - if your custom output function doesn't have parameter like `print`'s `end` use `None`, if has but called not `end` use the parameter to specify the name.
  
  `pipe_out_flush_name` - the same as `pipe_out_end_name` but for flush.

  `use_input_argument_for_output` - specifies if your pipe_in should get outsring as an output.
## autoinput_type - the way to specify type of data

### values

`autoinput_type` - IntFlag used to specify the type. Here are variants of it:

`autoinput_type.INTEGER` - return integer

`autoinput_type.FLOAT` - return floating point number

`autoinput_type.STRING` - return string, default type

`autoinput_type.BOOLYN` - asks yes or no, return bool

`autoinput_type.BOOLTF` - asks true or false, return bool

`autoinput_type.ARRAY` - asks for array where values are separated by space, return array of another type (if not specified returns str)

### how to use

To combine autoinput_type use `|`. Example:

```Python
autoinput_type.INTEGER | autoinput_type.ARRAY
```

**WARNING:** Do not combine types like that:

```Python
autoinput_type.INTEGER | autoinput_type.FLOAT
```

You will get an error if you try to run this.

If you need not a basic type use `parser` named argument.

## how to get Autoinput

To get Autoinput you can run this:

```Bash
pip install autoinput
```

**or:**

**Linux:**

```Bash
python3 -m pip install autoinput
```

**Windows:**

```cmd
py -m pip install autoinput
```
