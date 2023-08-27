# CodeCheck-2.0 Python Research

**Abstract:**

Textual similarity has many applications within the world of computer science, with general and
specific applications with academic integrity, general software feature augmentation, and data
analysis within specific fields. This project aims to make an open-source, lightweight textual
similarity algorithm for multiple applications.

**Introduction**

In recent years, the need for a lightweight, efficient, and accurate textual similarity
detection algorithm has grown significantly due to the increased importance of identifying
plagiarism, comprehending code reuse, ensuring intellectual property protection, and analyzing
similarities between niche applications of data (biometric data, filenames, etc.). This research
project presents CodeCheck 2.0, an innovative similarity recognition algorithm that addresses
these challenges by leveraging token pattern matching techniques using advanced pattern
recognition algorithms to differentiate similarities.
The methodology of this project involves processing two input sources, tokenizing all words or
shared strings between them, and examining the patterns of their usage rather than merely their
frequency. These patterns are subsequently analyzed and filtered to eliminate overlaps and
underlaps of data, thereby removing irrelevant data. Consequently, the refined algorithm
produces a researcher-oriented, list-based data structure of the patterns for each input and a
similarity percentage.
The outcome of this project is a complimentary, open-source software library and a
standalone software application featuring an intuitive graphical user interface for an accurate,
scalable, and adaptable text pattern recognition algorithm. This has been achieved without
reliance on external software products, algorithms, machine learning, or artificial intelligence,
except for default Python 3 libraries and necessary external graphical packages for standalone
applications.

**Background**

Assessing and establishing both relative and absolute similarities between two sets of
strings is of vital importance for a wide range of applications in the field of computer science.
CodeCheck 1.0 was initially developed to tackle these challenges; however, specific optimization
and accuracy issues were uncovered after its development, as it primarily analyzed token
frequency rather than usage patterns. As a result, CodeCheck 2.0 was conceived to address the
shortcomings of the original (legacy) algorithm, providing a solution that can be effortlessly
integrated into an array of computer science applications.

**Project Description**

The core algorithm of CodeCheck 2.0 consists of three primary components: the
tokenizer, the token pattern sequencers, and the token pattern recognition parser with a similarity
percentage method. The tokenizer encompasses several processes identifying and cataloging
tokens shared between two string inputs (two or more characters in matching sequential order).
The token pattern sequencers arrange all identified tokens into a continuous token pattern
"stream" data structure, displaying the tokens in the order they appear in their respective inputs.
Subsequently, the token pattern recognition parser examines the pattern streams for input A and
input B, identifying shared patterns of two or more tokens in sequential order present in both
pattern streams. Irrelevancies, overlaps, and underlaps are processed and removed to ensure the
accuracy of the analysis.
The final component processes the filtered streams for both inputs, calculating the
relative similarity percentages for each input concerning the other. An HTML-formatted string is
generated, displaying the matching text with highlights alongside the plain non-matching text for
each input.
The primary distinction between the CodeCheck 2.0 library and the user application is
that the application contains additional code to manage the graphical user interface. At the same
time, the core algorithm remains the same.

**Research Project achievements**

During the research for this project, the following steps were completed to fulfill the
original purpose and project proposal:
1. Proposed the project research to the CIMS department at Clayton State University.
2. Installed and configured the baseline environment for development and testing.
3. Analyzed the shortcomings of the original Java-based CodeCheck 1.0 program.
4. Adapted the processes developed for the deprecated Java-based CodeCheck 2.0 research
(discontinued due to runtime limitations, incompatible development frameworks, and
poor computational optimization in Java).
5. Enhanced tokenization by replacing the computationally expensive character referencing
process with a more efficient string-slicing technique.
6. Optimized the pattern recognition process by focusing on sequencing tokens found in
usage patterns instead of raw usage ratios.
7. Refactored all code in Python 3, ensuring minimal dependencies, computation time, and
memory usage.
8. Designed a poster for the second annual CIMS symposium at Clayton State University.
9. Compiled the improved CodeCheck 2.0 and the original CodeCheck 1.0 Python code into
a streamlined library.
10. Developed a graphical user interface using the PyQT5 graphical Python libraries.
11. Conducted final fine-tuning of all code and documented the development progress in a
comprehensive write-up.
