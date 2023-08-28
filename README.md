<a id="top"></a>
# CodeCheck 2.0 Python Research

**Table of Contents:**
* [Summary](#Summary)
* [Abstract](#Abstract)
* [Introduction](#Introduction)
* [Background](#Background)
* [Project Description](#Project_Description)
* [Research Project Achievements](#Research_Project_Achievements)
* [Pseudocode](#Pseudocode)
* [The Code](#The_Code)
* [Conclusion](#Conclusion)
* [Test Cases](#Test_Cases)
* [References](#References)
* [Works Cited](#Works_Cited)

***


<a id="Summary"></a>
**Project Summary:**

CodeCheck 2.0 is an advanced textual pattern recognition algorithm designed for string analysis. It operates by examining two input strings, identifying distinctive patterns present within the shared tokens of these inputs. The algorithm then produces reports detailing the extent of similarity, along with comprehensive metadata describing the nature of the similarities detected.

This software iteration has its origins in its predecessor, CodeCheck 1.0, which was initially implemented using the Java programming language. Furthermore, the deprecated 2.0 versions were also Java-based and formed the basis for this iteration. However, CodeCheck 2.0 has undergone a thorough reengineering process, now being meticulously constructed using the Python programming language.

The migration to Python was driven by the desire to leverage more efficient allocation of computational resources and the utilization of contemporary libraries. The redesigned CodeCheck 2.0 harnesses the capabilities of Python to achieve enhanced performance and resource management. The application is accessible in two main forms: a standalone Python application that includes a graphical user interface (GUI), and a version tailored for developers and researchers, packaged for ease of use in their respective workflows.

<a id="Abstract"></a>
**Abstract:**

Textual similarity has many applications within the world of computer science, with general and
specific applications with academic integrity, general software feature augmentation, and data
analysis within specific fields. This project aims to make an open-source, lightweight textual
similarity algorithm for multiple applications.

<a id="Introduction"></a>
**Introduction:**

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

<a id="Background"></a>
**Background:**

Assessing and establishing both relative and absolute similarities between two sets of
strings is of vital importance for a wide range of applications in the field of computer science.
CodeCheck 1.0 was initially developed to tackle these challenges; however, specific optimization
and accuracy issues were uncovered after its development, as it primarily analyzed token
frequency rather than usage patterns. As a result, CodeCheck 2.0 was conceived to address the
shortcomings of the original (legacy) algorithm, providing a solution that can be effortlessly
integrated into an array of computer science applications.

<a id="Project_Description"></a>
**Project Description:**

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

<a id="Research_Project_Achievements"></a>
**Research Project Achievements:**

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

<a id="Pseudocode"></a>
**Pseudocode:**

~~~~
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
~~~~

Please note that this pseudocode omits the implementations of the majority of variables, helpers
functions, objects, methods, and internal structures/processes outside of broad strokes in order to
keep the conceptual flow and length reasonable yet still relevant to the overall primary algorithm
function of CodeCheck2 method.
This pseudocode assumes that inputA and inputB are provided when calling the CodeCheck2
function. To use the pseudocode for any arbitrary inputs, replace the inputs in step 3 with the
desired input strings.

<a id="The_Code"></a>
**The Code:**

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

<a id="Test_Cases"></a>
**Test Cases:**

OpenAI's GPT-3.5 (Deprecated) and 4.0 API Models were utilized to generate test cases and
corresponding HTML similarity comparisons for evaluation purposes. Due to the inherent
characteristics of these advanced large language models with natural language processing
capabilities, there may be minor or significant discrepancies in the machine-generated HTML
comparisons. It is important to note that these machine-generated comparisons should be
regarded as an additional reference for the outputs of CodeCheck 2.0 (OpenAI’s Terms of
Service and user disclaimers even recommend that end user exercise discretion with model
outputs as its outputs may be completely inaccurate or false and also somewhat unpredictable),
not definitive results. OpenAI's products were employed in this instance to produce test cases
and reference HTML comparisons, owing to a non-availability of available model data
concerning plagiarized code, text samples, and biometric data. Both models have been cited in
the works cited section. The prompts for generating the test cases and references have been
included below.


The following are six test cases demonstrating the functionality of CodeCheck 2.0, including
similarity analysis for plain text, biometric data (DNA), and code. Each test case is structured as
follows: machine-generated test cases and their respective HTML comparisons are displayed on
the left, accompanied by an image illustrating the HTML rendering. The output data generated
by the CodeCheck 2.0 application based on the provided inputs are presented on the right.

<br>

| These are the prompts used to generate test cases (GPT-3.5 Legacy):                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get a short random sentence and print it out, then plagiarize that sentence (avoid changing thesentence structure, just change a few words) and print the results. Also, give the link to the page where the sentence was found. |
| Generate two stands of DNA of 36 characters with a space between every four characters and a shared gene of four characters between then                                                                                         |
| make a few lines of Python code and print it out, then plagiarize that code (avoid changing the structure, just change a few words) and print the results.                                                                       |
<br>

| This prompt was used to create the html references:                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This prompt was also modified to have the “sentences” portion of the prompt changed to code or DNA sequences for the other tests.                                             |
| Take in these two sentences and for all of the text matched between them surround that text with a highlight tag in HTML and then both sentences out:  sentence1:  sentence2: |

![image](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/assets/100094056/6cbdb213-0b6f-45e4-9e99-dc96dacddb77)

![image](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/assets/100094056/e9af2acf-3ac2-4ac5-aa58-1fb92a616aae)

![image](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/assets/100094056/8da671a9-ae79-4b98-b0ab-330b59fdaa3e)

![image](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/assets/100094056/9e92d9a9-33b6-45b7-9aba-c4d01a271a41)

![image](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/assets/100094056/7c5104a3-72cf-4d51-b9a9-774bcbd00131)

![image](https://github.com/Austin-Daigle/CodeCheck-2.0-Python-Research/assets/100094056/4a6e92f2-c0ea-42b5-8144-4f0ce5b6701f)

<a id="Conclusion"></a>
**Conclusion:**

This research project has successfully developed an open-source, lightweight textual
similarity algorithm that is versatile and applicable to multiple fields with various use cases
without requiring external services, AI, machine learning, or proprietary software. The algorithm
has successfully addressed the intended applications, such as anti-plagiarism (textual similarity
analysis), repetitive file name detection, biometric data analysis, and textual similarity. The
project has been optimized to cater to technical and non-technical researchers and users, making
it easily integrated into existing Python projects.

<a id="References"></a>
**References:**

The core code for CodeCheck 2.0 and Legacy does not rely on external sources to design
and construct the core algorithm. However, the CodeCheck 2.0 application utilizes the following
external dependencies for the graphical user interface: PyQt5, QtCore, QtGui, QtWidgets,
tkinter, messagebox from tkinter, and webbrowser. Each of these external Python packages is
referenced on the works cited page.

<a id="Works_Cited"></a>
**Works Cited:**

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
