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

**Pseudocode**

```
1. Define the findSharedPatterns() function.
2. Define the CodeCheck2() function.
3. Call CodeCheck2() with inputs inputA and inputB:
1. Tokenize inputA and inputB into lists of words and punctuation.
2. Create a list of unprocessed patterns by calling findSharedPatterns() with
tokenized inputA and inputB.
3. Process the list of unprocessed patterns using helper functions processList(),
removeAPairUnderlaps(), removeBPairUnderlaps(), and
removeEmptyPatterns().
4. Initialize the filteredAStream and filteredBStream lists.
5. Iterate through the processed patterns and append the corresponding token pairs
to the filteredAStream and filteredBStream.
6. Get similarity formatted HTML for both inputs using the
getSimilarityHTML() function.
7. Calculate similarity percentage scores for both inputs using the
calculatePercentage() function.
8. Compile the results into a single list and return it
```

Please note that this pseudocode omits the implementations of the majority of variables, helpers
functions, objects, methods, and internal structures/processes outside of broad strokes in order to
keep the conceptual flow and length reasonable yet still relevant to the overall primary algorithm
function of CodeCheck2 method.
This pseudocode assumes that inputA and inputB are provided when calling the CodeCheck2
function. To use the pseudocode for any arbitrary inputs, replace the inputs in step 3 with the
desired input strings.

**The Code**
The source code for the CodeCheck library is not included directly, as it is already
integrated within the application source code as part of its core analytical processes. A ported,
optimized version of CodeCheck 1.0 is incorporated into the library and the application under
"CodeCheck Legacy." The complete source code for the standalone CodeCheck 2.0 application,
including the graphical user interface, is provided below. Also, the raw source code with 
no application/GUI is included below for refference.

The application is called CodeCheck 2.0, as this represents its primary function, along with the
legacy build. However, the application is considered version 1.0, as this number denotes the
current version of the code managing the graphical user interface rather than the actual version of
the CodeCheck algorithm(s).

[CodeCheck 2.0 Application Source Code (Version 1.0)](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/blob/main/CodeCheck%202.0%20Application%20(Version%201.0).py)
[CodeCheck 2.0 Library Source Code (Version 1.0)](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/blob/main/CodeCheckLibrary.py)

**Conclusion**
This research project has successfully developed an open-source, lightweight textual
similarity algorithm that is versatile and applicable to multiple fields with various use cases
without requiring external services, AI, machine learning, or proprietary software. The algorithm
has successfully addressed the intended applications, such as anti-plagiarism (textual similarity
analysis), repetitive file name detection, biometric data analysis, and textual similarity. The
project has been optimized to cater to technical and non-technical researchers and users, making
it easily integrated into existing Python projects.

**Referrences**
The core code for CodeCheck 2.0 and Legacy does not rely on external sources to design
and construct the core algorithm. However, the CodeCheck 2.0 application utilizes the following
external dependencies for the graphical user interface: PyQt5, QtCore, QtGui, QtWidgets,
tkinter, messagebox from tkinter, and webbrowser. Each of these external Python packages is
referenced on the works cited page.

**Works Cited**
Developers, Staff. “Machine Generated Test Cases.” ChatGPT3.5, OpenAI, 2022,
https://chat.openai.com/.
Developers, Staff. “Machine Generated HTML Test Case references.” ChatGPT4, OpenAI,
2023, https://chat.openai.com/.
Group, Qt. “PYQT5.” PyPI, Qt Group, 1995, https://pypi.org/project/PyQt5/.
Group, Qt. “PySide2.QtCore.” PySide2.QtCore - Qt for Python, Qt Group, 21 Apr. 2016,
https://doc.qt.io/qtforpython-5/PySide2/QtCore/index.html.
Group, Qt. “PySide6.QtWidgets#.” PySide6.QtWidgets - Qt for Python, Qt Group, 1995,
https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html.
Group, Qt. “Qt Gui.” Qt Documentation, Qt Group, 2018, https://doc.qt.io/qt-5/qtgui-index.html.
Lumholt, Steen, and Guido van Rossum. “Tkinter - Python Interface to TCL/TK.” Edited by
Fredrik Lundh, Python Documentation, Python Software Foundation, 1999,
https://docs.python.org/3/library/tkinter.html.
Staff, Developer. “Webbrowser - Convenient Web-Browser Controller.” Python Documentation,
Python Software Foundation, 2000, https://docs.python.org/3/library/webbrowser.html. 
