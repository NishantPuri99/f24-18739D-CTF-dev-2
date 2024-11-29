# Git-ting good at ret2win
- Namespace: picoctf/18739f24
- ID: git-ting-good-at-it
- Type: custom
- Category: Binary Exploitation
- Points: 1
- Templatable: no

## Hints

- What does .git actually do?
- Have you heard about *git cat-file*
- Easy mode: https://youtu.be/H5ZQuuygH7E?si=0oClHAaboFLP-1VN

## Description

**I understand it now!**
ret2win ain't that hard. But where is the win function?
*Perhaps this is a lession in **git***

Download the server file: {{url_for("dotgit.tar.gz")}}

## Learning Objective

- Deep dive into git's objects

## Solution Overview

The user submits a gob-encode-nested-string and inputs it in the text area which causes the code to panic.
This leads to the api_key and route for the flag being revealed.

## Details

Connect to the webserver {{link_as("port", "/", "Here")}}

## Attributes
- author: nishant
