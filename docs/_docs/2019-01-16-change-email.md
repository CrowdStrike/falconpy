---
layout: doc
title: Doc with multiple tags/ category
date: 2019-09-08 8:14:30 +0600
post_image: assets/images/service-icon3.png
tags: [Profile, Account Settings, Invoice]
toc: true
custom_links:
- text: Installation
  url: /
- text: Getting Started
  url: /pages/support
- text: Product Manual
  url: /#drop
  submenu:
  - text: Invoice
    url: /blog-post-left-sidebar
  - text: Payment
    url: /blog-post-right-sidebar
  - text: Another Link
    url: /tag/education
- text: Support
  url: https://support.themeix.com	
- text: Contact
  url: /pages/contact
---
Jekyll is a simple, blog-aware, static site generator. It takes a template directory containing raw text files in various formats, runs it through a converter (like Markdown) and our Liquid renderer, and spits out a complete, ready-to-publish static website suitable for serving with your favorite web server.

If you already have a full Ruby development environment with all headers and RubyGems installed, you can create a new Jekyll site by doing the following:

## How to install

~~~ bash
# Install Jekyll and Bundler gems through RubyGems
~ $ gem install jekyll bundler

# Create a new Jekyll site at ./myblog
~ $ jekyll new myblog

# Change into your new directory
~ $ cd myblog

# Build the site on the preview server
~/myblog $ bundle exec jekyll serve

# Now browse to http://localhost:4000
~~~

## Next steps

Building a Jekyll site with the default theme is just the first step. The real magic happens when you start creating blog posts, using the front matter to control templates and layouts, and taking advantage of all the awesome configuration options Jekyll makes available.

## Basic usage

The Jekyll gem makes a `jekyll` executable available to you in your Terminal window. You can use this command in a number of ways:

~~~ bash
$ jekyll build
# => The current folder will be generated into ./_site

$ jekyll build --destination <destination>
# => The current folder will be generated into <destination>

$ jekyll build --source <source> --destination <destination>
# => The <source> folder will be generated into <destination>

$ jekyll build --watch
# => The current folder will be generated into ./_site,
#    watched for changes, and regenerated automatically.
~~~

## Directory structure

Jekyll is, at its core, a text transformation engine. The concept behind the system is this: you give it text written in your favorite markup language, be that Markdown, Textile, or just plain HTML, and it churns that through a layout or a series of layout files. Throughout that process you can tweak how you want the site URLs to look, what data gets displayed in the layout, and more. This is all done through editing text files; the static web site is the final product.

A basic Jekyll site usually looks something like this:

~~~ bash
.
├── _config.yml
├── _data
|   └── members.yml
├── _drafts
|   ├── begin-with-the-crazy-ideas.md
|   └── on-simplicity-in-technology.md
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   └── post.html
├── _posts
|   ├── 2007-10-29-page--nethack.md
|   └── 2009-04-26-barcamp-boston-4-roundup.md
├── _sass
|   ├── _base.scss
|   └── _layout.scss
├── _site
├── .jekyll-metadata
└── index.html # comment example
~~~

## Front matter

The front matter is where Jekyll starts to get really cool. Any file that contains a YAML front matter block will be processed by Jekyll as a special file. The front matter must be the first thing in the file and must take the form of valid YAML set between triple-dashed lines. Here is a basic example:

~~~ html
---
layout: post
title: Blogging Like a Hacker
---
~~~

Between these triple-dashed lines, you can set predefined variables (see below for a reference) or even create custom ones of your own. These variables will then be available to you to access using Liquid tags both further down in the file and also in any layouts or includes that the page or post in question relies on.

![Example image](https://images.unsplash.com/photo-1481487196290-c152efe083f5?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1920&h=1080&fit=crop&s=80308172730757a7db0434987fa985f3)

## Where additional pages live

Where you put HTML or Markdown files for pages depends on how you want the pages to work. There are two main ways of creating pages:

* Place named HTML or Markdown files for each page in your site’s root folder.
* Place pages inside folders and subfolders named whatever you want.

Both methods work fine (and can be used in conjunction with each other), with the only real difference being the resulting URLs. By default, pages retain the same folder structure in `_site` as they do in the source directory.