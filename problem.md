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
- Easy mode: [Deep Dive into .git](https://youtu.be/H5ZQuuygH7E?si=0oClHAaboFLP-1VN)

## Description

**I understand it now!**
ret2win ain't that hard. But where is the win function?
*Perhaps this is a lession in **git***

## Learning Objective

- Deep dive into git's objects

## Solution Overview

The user is is supposed to execute a simple ret2win buffer overflow. The catch is that neither the source file is provided nor the executable. All the user has is the .git folder.

Using commands like git cat-file, or by following the hints in the video, the user can figure out how to extract the executable from the .git file.
They can use is to execute the normal ret2win

## Details
Connect to the program on our server: `nc {{server}} {{port}}`
Download the .git folder: {{url_for("dotgit.tar.gz")}}

## Attributes
- author: nishant
