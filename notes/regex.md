# Regular Expressions (Regex)

## 1. Introduction

Regular Expressions (Regex) are patterns used to search, match, extract, validate, and manipulate text. They provide a concise and powerful way to identify specific sequences of characters within a string.

In Natural Language Processing (NLP), regex is commonly used during text preprocessing to remove unwanted content such as URLs, HTML tags, punctuation, numbers, and extra whitespace before the text is analyzed by machine learning models.

Regex is supported in many programming languages, including Python through the built-in `re` module.

---

## 2. Why is Regex Needed?

Real-world text often contains inconsistent formatting and unnecessary information.

For example:

```
Contact me at zenn@gmail.com
Visit https://example.com
Price: $250
```

Instead of writing multiple loops and conditions to process such text, regex allows us to define a pattern once and efficiently match all similar text.

Regex helps by:

1. Finding specific text patterns.
2. Extracting useful information.
3. Validating user input.
4. Cleaning noisy text.
5. Replacing unwanted characters.

---

## 3. How Does Regex Work?

A regular expression consists of normal characters and special symbols called **metacharacters**.

For example:

```
Pattern

\d+

↓

Matches

1
25
2026
999
```

Python compares the pattern with the input string and returns matches based on the specified rule.

---

# 4. Python Regex Module

```python
import re
```

Some commonly used functions are:

| Function        | Purpose                                      |
| --------------- | -------------------------------------------- |
| `re.search()`   | Finds the first match.                       |
| `re.match()`    | Matches only at the beginning of the string. |
| `re.findall()`  | Returns all matches as a list.               |
| `re.finditer()` | Returns an iterator of match objects.        |
| `re.sub()`      | Replaces matched text.                       |
| `re.split()`    | Splits text using a pattern.                 |

---

# 5. Common Regex Metacharacters

## 5.1 `.`

Matches any single character except a newline.

```python
import re

text = "cat bat rat"

print(re.findall(r".at", text))
```

Output

```
['cat', 'bat', 'rat']
```

---

## 5.2 `^`

Matches the beginning of a string.

```python
re.findall(r"^Hello", "Hello World")
```

Output

```
['Hello']
```

---

## 5.3 `$`

Matches the end of a string.

```python
re.findall(r"World$", "Hello World")
```

Output

```
['World']
```

---

## 5.4 `*`

Matches zero or more occurrences.

```python
re.findall(r"ab*", "ab abb abbb a")
```

Output

```
['ab', 'abb', 'abbb', 'a']
```

---

## 5.5 `+`

Matches one or more occurrences.

```python
re.findall(r"ab+", "ab abb a")
```

Output

```
['ab', 'abb']
```

---

## 5.6 `?`

Matches zero or one occurrence.

```python
re.findall(r"colou?r", "color colour")
```

Output

```
['color', 'colour']
```

---

## 5.7 `[]`

Matches any one character inside the brackets.

```python
re.findall(r"[aeiou]", "Artificial Intelligence")
```

Output

```
['A', 'i', 'i', 'a', 'I', 'e', 'i', 'e', 'e']
```

---

## 5.8 `[^ ]`

Matches characters **not** inside the brackets.

```python
re.findall(r"[^aeiou ]", "hello")
```

Output

```
['h', 'l', 'l']
```

---

## 5.9 `\d`

Matches digits.

```python
re.findall(r"\d+", "Age: 21")
```

Output

```
['21']
```

---

## 5.10 `\D`

Matches non-digit characters.

```python
re.findall(r"\D+", "Age21")
```

Output

```
['Age']
```

---

## 5.11 `\w`

Matches letters, digits and underscore.

```python
re.findall(r"\w+", "hello_world123")
```

Output

```
['hello_world123']
```

---

## 5.12 `\W`

Matches non-word characters.

```python
re.findall(r"\W+", "Hello@123!")
```

Output

```
['@', '!']
```

---

## 5.13 `\s`

Matches whitespace.

```python
re.findall(r"\s", "Hello World")
```

---

## 5.14 `\S`

Matches non-whitespace.

```python
re.findall(r"\S+", "Hello World")
```

Output

```
['Hello', 'World']
```

---

## 5.15 `\b`

Matches a word boundary.

```python
re.findall(r"\bcat\b", "cat category")
```

Output

```
['cat']
```

---

# 6. Common Regex Applications in NLP

### Remove URLs

```python
re.sub(r'https?://\S+|www\.\S+', '', text)
```

---

### Remove HTML Tags

```python
re.sub(r'<.*?>', '', text)
```

---

### Remove Numbers

```python
re.sub(r'\d+', '', text)
```

---

### Remove Punctuation

```python
re.sub(r'[^\w\s]', '', text)
```

---

### Remove Extra Spaces

```python
re.sub(r'\s+', ' ', text).strip()
```

---

# 7. Advantages

1. Fast text searching.
2. Powerful pattern matching.
3. Simplifies text cleaning.
4. Useful in NLP preprocessing.
5. Supported in many programming languages.

---

# 8. Limitations

1. Complex expressions become difficult to read.
2. Cannot understand semantic meaning.
3. Long regex patterns are harder to maintain.
4. Poorly designed patterns may affect performance.

---

# 9. Real-World Applications

* Text preprocessing
* Email validation
* Password validation
* Phone number extraction
* Web scraping
* Data cleaning
* Log file analysis
* Search engines

---

# 10. Common Mistakes

❌ Forgetting to use raw strings (`r""`).

❌ Confusing `*` and `+`.

❌ Forgetting that `.` matches almost any character.

❌ Using greedy matching when non-greedy matching is needed.

❌ Forgetting word boundaries (`\b`).

---

# 11. Interview Questions

1. What is a regular expression?

2. Why is regex used in NLP?

3. What is the difference between `search()` and `match()`?

4. What is the difference between `findall()` and `finditer()`?

5. Explain `\d`, `\w`, `\s`, and `\b`.

6. Why are raw strings (`r""`) recommended in regex?

7. What is the difference between `*`, `+`, and `?`?

---

# 12. Key Takeaways

* Regex is a pattern-matching language.
* It is widely used for text preprocessing.
* Python provides regex support through the `re` module.
* Regex is excellent for cleaning and extracting text.
* Regex works on character patterns, not semantic meaning.
* It is a fundamental skill for NLP, web scraping, and data cleaning.
