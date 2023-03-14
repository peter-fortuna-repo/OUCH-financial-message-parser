# OUCH_Parser
A simple parser for OUCH messages

Introduction
OUCH 5.0 is a text-based protocol for interaction between parties in financial trading. Banks, brokers, clearing firms, exchanges, and other general market participants use OUCH protocol for all phases of electronic trading.

This package provides a simple parser to interpret and store OUCH messages after they have been used for electronic trading purposes. It does not create OUCH messages or read accept them in real time. It supports the decoding and formatting of OUCH messages.

Licence
The module is licensed under the MIT license.

Parsing Messages
To parse an OUCH message, first create an instance of the Parser class.

parser = Parser.Parser()

parser.parse(data) will parse the encoded OUCH messages that you pass in. You should enter data of type bytes, str, List[bytes], List[str], or List[int]. This method can be called multiple times and all results will be stored within the parser object
parser.getMessages() will return a Python dictionary containing all the data stored inside your parser object
parser.reset() will clear the data stored inside your parser

Contributing
Comments, suggestions, bug reports, bug fixes – all contributions to this project are welcomed. Please use this project’s GitHub page for access to the latest source code, and please open an issue for comments, suggestions, and bugs.
