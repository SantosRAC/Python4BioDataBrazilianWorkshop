
- [Inicio](../index.md)
- [Cronograma](cronograma.md)
- [Guia de Instalação](guia_de_instalacao.md)
- [Material Python](python.md)
- [Problema 1](problema1.md)
- [Problema 2](problema2.md)


# Problema 1: processamento de resultados de RNA-seq


## Objetivos

1. Importar tabela com dados de expressão normalizados (RNA-seq, RPKM)

2. Calcular estatísticas a partir dos dados de expressão em múltiplos experimentos

3. Adicionar informação de anotação

4. Visualização de dados de expressão



## Desenvolvimento de código

Códigos deverão usar as seguintes bibliotecas de **python 3.6 (Jupyter Notebook no Anaconda)**:

1. matplotlib
2. pandas
3. numpy

### A tabela com dados de expressão

O arquivo usado durante a prática está disponível como material suplementar do artigo:

[Mortazavi et al, 2008](http://www.nature.com/nmeth/journal/v5/n7/full/nmeth.1226.html)

* nmeth.1226-S3

O cabeçalho da tabela:

`gid	RNAkb	gene	firstRPKM	expandedRPKM	finalRPKM	fractionMulti`

Linhas seguintes:

`100008564	17.422	RP23-273B19.1	0.05	0.05	0.27	0.84`

As informações em colunas são separadas por `tab` (tabulação). O arquivo pode ser visualizado no Excel.

### Lendo a tabela e transformando em um objeto de Python (dataFrame de Pandas)

Uma 'série' de pandas é um objeto unidimensional como uma lista que apresenta uma lista associada com 'labels', chamado índice.

Operação com séries:

`S1 = Series([7.3, -2.5, 3.4, 1.5], index=['a','c','d','e'])`

`S2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a','c','e','f','g'])`

`S1 + S2 # Summing values in different series, but with the same index`

Um 'DataFrame' de pandas representa uma estrutura de dados tabular que contém uma coleção de colunas, cada um com um tipo diferente de valor (numérico, 'string', booleana, etc). DataFrame tem índice para linhas e colunas e pode ser pensado como um dicionário de séries (todas que compartilham o mesmo índice).

### Dados de anotação

Genoma do camundongo (Mus musculus, montagem 'GRCm38.p5'): https://www.ncbi.nlm.nih.gov/genome?LinkName=assembly_genome&from_uid=763931

Informações em formato tabular serão/ foram baixadas para os genes ('related information', lado direito da página do genoma).

Download realizado em 21 de julho de 2017.

## Informações adicionais

Tipos de normalização
- **CPM**: ( número de reads / número de framentos sequenciados ) * 1000000
- **TPM** (entre genes): 
- **RPKM** (entre genes): 
- **FPKM** (entre genes): 
- **TMM** (entre amostras):

Requerimentos:
- Comprimento dos genes
- Tamanho da biblioteca (número de fragmentos sequenciados e mapeados)
- Número de amostras
- Dispersão

## Referências

Ching, Travers, Sijia Huang, and Lana X. Garmire. "[Power analysis and sample size estimation for RNA-Seq differential expression.](http://rnajournal.cshlp.org/content/20/11/1684.short)" Rna 20.11 (2014): 1684-1696.

Mortazavi, Ali, et al. "[Mapping and quantifying mammalian transcriptomes by RNA-Seq.](https://www.nature.com/nmeth/journal/v5/n7/full/nmeth.1226.html)" Nature methods 5.7 (2008): 621-628.

[Python for Data Science](http://wesmckinney.com/)

## Páginas de interesse

Blog do Dr. Harold Pimentel: "[What the FPKM? A review of RNA-Seq expression units](https://haroldpimentel.wordpress.com/2014/05/08/what-the-fpkm-a-review-rna-seq-expression-units/)"

Blog do Dr. Harold Pimentel: "[In RNA-Seq, 2 != 2: Between-sample normalization](https://haroldpimentel.wordpress.com/2014/12/08/in-rna-seq-2-2-between-sample-normalization/)"
