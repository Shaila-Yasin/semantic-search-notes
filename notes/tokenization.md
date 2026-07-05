# Tokenization

## 1. Introduction

Tokenization is the process of breaking raw text into smaller units called **tokens**. These tokens are the basic units that Natural Language Processing (NLP) models use to process text.

A token can be:

* A word
* A character
* A subword
* A punctuation mark
* A special symbol

Since computers cannot directly understand raw text, tokenization is one of the first steps in every NLP pipeline.

Example:

Raw Text

```text
I love Artificial Intelligence.
```

After Word Tokenization

```text
["I", "love", "Artificial", "Intelligence", "."]
```

---

## 2. Why is Tokenization Needed?

Machine learning models cannot process raw text directly.

Before text can be converted into vectors or embeddings, it must first be divided into meaningful units.

Tokenization helps by:

1. Breaking text into manageable pieces.
2. Preparing text for numerical representation.
3. Making feature extraction possible.
4. Serving as the input to embedding layers.
5. Reducing the complexity of text processing.

Without tokenization, modern NLP models such as BERT, GPT, and LLaMA cannot process language.

---

## 3. How Tokenization Works

A typical NLP pipeline looks like this:

```text
Raw Text
      ↓
Text Preprocessing
      ↓
Tokenization
      ↓
Token IDs
      ↓
Embeddings
      ↓
Transformer
      ↓
Output
```

Example:

Sentence

```text
I love NLP.
```

↓

Word Tokens

```text
["I", "love", "NLP", "."]
```

↓

Vocabulary Lookup

```text
"I" → 12

"love" → 98

"NLP" → 523

"." → 7
```

↓

Token IDs

```text
[12, 98, 523, 7]
```

The embedding layer later converts these IDs into dense vectors.

---

## 4. Types of Tokenization

### 4.1 Sentence Tokenization

Splits a paragraph into individual sentences.

Example

Before

```text
I love AI. It is amazing. I study NLP.
```

After

```python
[
"I love AI.",
"It is amazing.",
"I study NLP."
]
```

Python Example

```python
from nltk.tokenize import sent_tokenize

text = "I love AI. It is amazing."

sent_tokenize(text)
```

Output

```python
['I love AI.', 'It is amazing.']
```

---

### 4.2 Word Tokenization

Splits a sentence into words.

Example

```text
I love AI.
```

↓

```python
["I", "love", "AI", "."]
```

Python Example

```python
from nltk.tokenize import word_tokenize

text = "I love AI."

word_tokenize(text)
```

Output

```python
['I', 'love', 'AI', '.']
```

---

### 4.3 Character Tokenization

Splits text into individual characters.

Example

```text
ChatGPT
```

↓

```python
['C','h','a','t','G','P','T']
```

Python Example

```python
text = "ChatGPT"

list(text)
```

---

### 4.4 Subword Tokenization

Instead of splitting by complete words, text is divided into smaller meaningful pieces called **subwords**.

Example

```text
unhappiness
```

↓

```text
["un", "happi", "ness"]
```

or

```text
["un", "##happy", "##ness"]
```

Subword tokenization solves the **Out-of-Vocabulary (OOV)** problem because unknown words can be built from known subwords.

Modern LLMs use subword tokenization.

---

## 5. Tokenization in Modern LLMs

Unlike traditional NLP systems, modern Large Language Models do **not** simply split text by spaces.

Instead, they use advanced tokenization algorithms.

The most common are:

* Byte Pair Encoding (BPE)
* WordPiece
* SentencePiece

These methods learn the most frequent word pieces from large datasets.

Example

```text
playing
```

may become

```text
play
##ing
```

instead of a single token.

This allows models to understand millions of different words while keeping the vocabulary size manageable.

---

## 6. Vocabulary

A **vocabulary** is the collection of all tokens known to a tokenizer.

Example

```text
Vocabulary

I

love

AI

play

##ing

the

computer
```

Each token has a unique integer ID.

Example

| Token | Token ID |
| ----- | -------- |
| I     | 12       |
| love  | 98       |
| AI    | 523      |
| play  | 811      |
| ##ing | 145      |

These IDs are passed to the embedding layer.

---

## 7. Special Tokens

Transformer models use special tokens to represent specific meanings.

Common examples include:

| Token    | Purpose                                    |
| -------- | ------------------------------------------ |
| `[CLS]`  | Represents the entire sentence (BERT).     |
| `[SEP]`  | Separates two sentences.                   |
| `[PAD]`  | Pads shorter sequences to the same length. |
| `[MASK]` | Masks words during BERT training.          |
| `<BOS>`  | Beginning of a sequence.                   |
| `<EOS>`  | End of a sequence.                         |
| `<UNK>`  | Unknown token not found in the vocabulary. |

Different models may use different special tokens.

---

## 8. Tokenization in GPT Models

GPT models use **Byte Pair Encoding (BPE)**.

Important facts:

* Tokens are **not** the same as words.
* A single word may become multiple tokens.
* A token may represent:

  * a whole word
  * part of a word
  * punctuation
  * whitespace

Example

```text
unbelievable
```

↓

```text
un
believ
able
```

This is one reason GPT counts **tokens**, not words.

---

## 9. Python Implementation

### Word Tokenization

```python
from nltk.tokenize import word_tokenize

text = "I love Artificial Intelligence."

tokens = word_tokenize(text)

print(tokens)
```

---

### Sentence Tokenization

```python
from nltk.tokenize import sent_tokenize

text = "AI is amazing. NLP is interesting."

sent_tokenize(text)
```

---

### Hugging Face Tokenizer

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

tokens = tokenizer.tokenize("I love Artificial Intelligence")

print(tokens)
```

Example Output

```python
['i', 'love', 'artificial', 'intelligence']
```

---

## 10. Advantages

1. Converts raw text into processable units.
2. Forms the foundation of every NLP pipeline.
3. Enables embedding generation.
4. Supports efficient vocabulary management.
5. Helps modern LLMs handle unknown words.

---

## 11. Limitations

1. Different tokenizers produce different outputs.
2. Poor tokenization can reduce model performance.
3. Languages without spaces are more difficult to tokenize.
4. Tokenization alone does not capture semantic meaning.

---

## 12. Real-World Applications

* Chatbots
* Search Engines
* Machine Translation
* Question Answering
* Text Classification
* Sentiment Analysis
* Large Language Models
* Semantic Search
* Retrieval-Augmented Generation (RAG)

---

## 13. Common Mistakes

 1. Assuming one word always equals one token.

 2. Believing GPT tokenizes only by spaces.

 3. Ignoring special tokens.

 4. Thinking token IDs contain semantic meaning (they are just integer identifiers).

 5. Confusing tokenization with embeddings.

---

## 14. Interview Questions

1. What is tokenization?

2. Why is tokenization necessary before embeddings?

3. What is the difference between word, character, sentence, and subword tokenization?

4. What is the Out-of-Vocabulary (OOV) problem?

5. Why do LLMs use subword tokenization?

6. What is a vocabulary?

7. Are token IDs embeddings?

8. Why do GPT models count tokens instead of words?

9. What are special tokens?

10. What is the difference between BPE and WordPiece?

---

## 15. Key Takeaways

* Tokenization is the process of splitting text into tokens.
* It is one of the first steps in every NLP pipeline.
* Tokens are converted into integer IDs before entering the embedding layer.
* Modern LLMs use subword tokenization instead of simple word splitting.
* Token IDs are not embeddings; they are numerical identifiers.
* The embedding layer transforms token IDs into dense vectors.
* Different models use different tokenization algorithms.
* GPT counts tokens rather than words.
* Good tokenization improves the quality of downstream NLP tasks.

---

## 16. Summary

Tokenization is the bridge between raw text and numerical processing. It converts human-readable language into tokens that can be mapped to integer IDs and later transformed into embeddings. Modern transformer models rely on advanced subword tokenization techniques such as Byte Pair Encoding (BPE), WordPiece, and SentencePiece to efficiently represent language while handling previously unseen words. Understanding tokenization is essential because every transformer-based model begins by tokenizing the input before generating embeddings and applying attention mechanisms.
