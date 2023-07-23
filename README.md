# dividir_para_copiar

![parodia com julio cesar falando dividir para copiar](imagens/julio_cesar_dividir_para_conquistar_.png)

Esse programa pode dividir textos em partes menores e copiá-las para a área de transferência, uma por uma.

## Instalação

```bash
pip -r requirements.txt
```

## Utilizaçao

```bash
ipython -i . # iniciar o programa
```

```python
In [1]: len(texto_dividido) # pra saber a quantidade dividida
Out[1]: 3 # nesse exemplo deu 3 
In [2]: copy(0) # copia a primeira parte
In [3]: copy(2) # copia a terceira parte
```

> Recomendo utilizar em prompts, que pedem uma quantidade expecífica de caractéres
