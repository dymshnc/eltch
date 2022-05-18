# Eltch
**Eltch** is a module that will help you in working with electricity.

Now, an "electric current wheel" based on Ohm's law has been implemented. With it, you can calculate: *Volts, Watts, Ohms, Amps*. Having only two values from this list.

```python
import eltch

e = eltch.EWheel()

# e.volts_amps(volts_val, volts_val)
all_values = e.volts_amps(100, 200)

print(all_values)
```
```python
{'U': 100.0, 'R': 0.5, 'I': 200.0, 'P': 20000.0}
```

The "EWheel" class has a number of functions: `watts_volts()`, `watts_ohms()`, `watts_amps()`, `volts_watts()`, `volts_ohms()`, `volts_amps()`, `ohms_watts()`, `ohms_volts()`, `ohms_amps()`, `amps_watts()`, `amps_volts()`, `amps_ohms()`.

With an example, you can see how it works. A function is selected for the value you have. Based on the name of the function, you pass these values to it.
The function returns a dictionary with all the values from "electric current wheel" that you can use for your own purposes.

```python
resist_sum = all_values['R'] + 0.6
# ...
```
## Installing Eltch and Supported Versions
**Eltch** is available on PyPI:
```
$ python -m pip install eltch
```

Eltch officially supports Python 3.6+.
