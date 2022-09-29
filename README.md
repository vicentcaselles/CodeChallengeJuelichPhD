# CodeChallengeJuelichPhD
My submission in response to the code challenge posed by Dr Kranz in the context of my application for the PhD position in "High Dimensional Multi Omics Data Integration".

## Exercise 1

This exercise was very enriching for me, since I was unfamiliar with the concept of DAG. I wanna remark that all code was done from scratch from me, which was quite challenging. First of, I looked up online how DAGs are usually inputed into computers, and I settled with using dictionaries. After choosing this path, I had to approach the creation of a function that goes from a dictionary depicting a DAG, to an adjacency matrix (concept I was unfamiliar with too).

I created a function that, as I said, takes a dictionary as an input and returns the depth to the root node. You can see an example DAG in the repo (dag_example.jpeg). Such a DAG would be encoded as: 

```
{'root': ['a', 'b', 'c'], 'a': ['f', 'g', 'h'], 'b': ['h'], 'c': ['l', 'm'], 'f': ['i', 'j', 'k']}.
```
As you can see, the DAG is encoded as a dictionary where every key is connected to its values.

The function must be run from the command line using the python3 command (or the python version you use) and ex1.py, and it asks you for a DAG which should be inputed **without quotations**. Right after, you will be prompted for a node to find the depth of, which should **also be introduced without quotations**.
```
python3 ex1.py
```
The depth calculator function is designed to make its way from the node towards the root, appending every branching possible and returning the minimum value corresponding to the shortest path.

## Exercise 2

The second exercise works on the assumption that you have blast installed on your computer, and you can call the blast commands (i.e. makeblastdb and blastp) from your shell. However, if that's not the case you should call first install blast and its exectuables from [here](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download). Afterwards, if you don't have the blastp/makeblastdb commands available, you can call them using the following sintax:
```
/path/to/ncbi-blast-2.13.0+/bin/makeblastdb
```
(I have blast version 2.13.0 btw).

I want to be honest, I wasn't familiar with running blast through my command line, so I had to spend a lot of time learning how to do that. Therefore, the **python function isn't mine**, my sincerest apologies for that. They are from [this github repository](https://github.com/hongqin/Simple-reciprocal-best-blast-hit-pairs).

The two Nostoc genomes I chose were [Nostoc punctiforme](https://www.ncbi.nlm.nih.gov/genome/1050?genome_assembly_id=300502), which is a complete genome, and [Nostoc piscinale](https://www.ncbi.nlm.nih.gov/genome/40224?genome_assembly_id=248578), which is only a "chromosome" assembly level genome.

The recommendation for runing exercise 2's shell script is to download the repo locally and run it from your shell establishing the repo with the ex2.sh as your current directory.
