UTF-8 Validation
This repository contains a Python method validUTF8() that determines whether a given dataset represents a valid UTF-8 encoding.

Method Description
The validUTF8() method takes a list of integers as input, where each integer represents one byte of data. It then checks whether the given data set represents a valid UTF-8 encoding according to the following rules:

A character in UTF-8 can be 1 to 4 bytes long.
The data set can contain multiple characters.
The method returns True if the data is a valid UTF-8 encoding, otherwise it returns False.
