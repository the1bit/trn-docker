# Alap Docker példa


1. Indítsunk el egy Python konténert, és futtassunk benne egy Python parancsot.

```bash
docker run python:3.11 python -c "print('Hello, Docker!')"
```


2. Lépjünk be a konténerbe, és futtassunk egy Python parancsot.

```bash
docker run -it python:3.11 bash
```

```bash
python --version
```

```bash
python
```

```python
print('A Docker konténerben vagyok!')
```

```python
exit()
```

```bash
exit
```
