# flattenJSON

Takes a file containing JSON and flattens it. For example,
given an input file like:

```json
{
  "a": 1,
  "b": true,
  "c": {
    "d": 3,
    "e": "test"
  }
}
```

the output is:
```json
{
  "a": 1, 
  "b": true, 
  "c.d": 3, 
  "c.e": "test"
}
```

It also has support for multiple levels of 
hierarchical dictionary-like structures. There is no
support for list structures, and the program will
exit if it encounters it.

## usage

cat files/input.json | python main.py

## test
python tests.py