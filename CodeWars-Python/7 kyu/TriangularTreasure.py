"""Triangular Treasure
https://www.codewars.com/kata/triangular-treasure

Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.

```
1st (1)   2nd (3)    3rd (6)
*          **        ***
           *         **
                     *
```

You need to return the nth triangular number. You should return 0 for out of range values:

```haskell
all [
  triangular 0     == 0,
  triangular 2     == 3,
  triangular 3     == 6,
  triangular (-10) == 0
] -- True
```
```javascript
  triangular(0)==0,
  triangular(2)==3,
  triangular(3)==6,
  triangular(-10)==0
```
```ruby
  triangular(0)==0,
  triangular(2)==3,
  triangular(3)==6,
  triangular(-10)==0
```
```python
  triangular(0)==0,
  triangular(2)==3,
  triangular(3)==6,
  triangular(-10)==0
```
```dart
  triangular(0)==0,
  triangular(2)==3,
  triangular(3)==6,
  triangular(-10)==0
```
```swift
  triangular(0)==0
  triangular(2)==3
  triangular(3)==6
  triangular(-10)==0
```
"""


def triangular(n):
    return n*(n+1)/2 if n > 0 else 0
