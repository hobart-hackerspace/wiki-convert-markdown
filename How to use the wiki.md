## The basics
- The usual Markdown formatting options apply. [See the cheatsheet here](Markdown cheatsheet).
- Links 
	- Links are constructed in classic markdown form -- `[`label text`](`destination URL`)`
	- Links to other pages in the wiki can be inserted by putting the name of the page (without the `.md` extension) in brackets, eg: `[How to use the wiki](How to use the wiki)` would link back to this page. [How to use the wiki](How to use the wiki)

## Plugins

The plugins are used to extend the functionality of the wiki. Most of them are accessible through the use of `tags`.
For now there are only a few supported.  

- `[[draw]]` Allows you to add an **interactive drawio drawing** to the wiki.  
- `[[ page: some-page ]]` Allows to show an other page in the current one.
- **Banners**  
	- Can be: `[[info]]`, `[[warning]]`, `[[danger]]`, `[[success]]`  
	- for example,  the text `[[success]] You are ready to go!` gives:

[[success]] You are ready to go!

### More plugins

All plugins are documented at the [wikmd doocumentation site](https://linbreux.github.io/wikmd/plugins.html)

## Latex

It's possible to use $\LaTeX$ syntax inside your markdown because the markdown is first converted to latex and after that to html. This means you have a lot more flexibility.

- For in-line $\LaTeX$ snippets, enclose them in `$` characters, eg: `$\LaTeX$`
- For an example of a larger block of $\LaTeX$, see the mathematical formulae below.


### Change image size
```
![](https://i.ibb.co/Dzp0SfC/download.jpg){width="50%"}
```
![](https://i.ibb.co/Dzp0SfC/download.jpg){width="50%"}

### Image references
```
![\label{test}](https://i.ibb.co/Dzp0SfC/download.jpg){width="50%"}

Inside picture \ref{landscape picture} you can see a nice mountain.

```
![picture \label{landscape picture}](https://i.ibb.co/Dzp0SfC/download.jpg){width="50%"}

Clickable reference in picture \ref{landscape picture}.

### Math
```
\begin{align}
y(x) &= \int_0^\infty x^{2n} e^{-a x^2}\,dx\\
&= \frac{2n-1}{2a} \int_0^\infty x^{2(n-1)} e^{-a x^2}\,dx\\
&= \frac{(2n-1)!!}{2^{n+1}} \sqrt{\frac{\pi}{a^{2n+1}}}\\
&= \frac{(2n)!}{n! 2^{2n+1}} \sqrt{\frac{\pi}{a^{2n+1}}}
\end{align}
```
\begin{align}
y(x) &= \int_0^\infty x^{2n} e^{-a x^2}\,dx\\
&= \frac{2n-1}{2a} \int_0^\infty x^{2(n-1)} e^{-a x^2}\,dx\\
&= \frac{(2n-1)!!}{2^{n+1}} \sqrt{\frac{\pi}{a^{2n+1}}}\\
&= \frac{(2n)!}{n! 2^{2n+1}} \sqrt{\frac{\pi}{a^{2n+1}}}
\end{align}

```
You can also use $inline$ math to show $a=2$ and $b=8$
```
You can also use $inline$ math to show $a=2$ and $b=8$

And many other latex functions.

## Converting the files

Open the wiki folder of your instance.  

|- static  
|- templates  
|- **wiki** $\leftarrow$ This folder  
|- wiki.py  

In this folder all the markdownfiles are listed. Editing the files will be visible in the web-version.  

|- homepage.md  
|- How to use the wiki.md  
|- Markdown cheatsheet.md  

The advantage is that u can use the commandline to process some data. For example using pandoc:
```
$ pandoc -f markdown -t latex homepage.md How\ to\ use\ the\ wiki.md -o file.pdf --pdf-engine=xelatex
```
This creates a nice pdf version of your article.  Its possible you have to create a yml header on top of your document to set the margins etc better
```
---
title: titlepage
author: your name
date: 05-11-2020
geometry: margin=2.5cm
header-includes: |
		\usepackage{caption}
		\usepackage{subcaption}
lof: true
---
```
For more information you have to read the pandoc documentation.

[Using the version control system](/Using the version control system)
