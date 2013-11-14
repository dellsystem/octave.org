![octave.org](http://i.imgur.com/vhPfLAZ.png)

Source code for the redesigned GNU Octave website. Built with Jekyll and
released under the MIT license.

# Dependencies

The site is generated using [Jekyll](http://jekyllrb.com/), a static site
generator written in Ruby. To use it, you'll need to have Ruby and Rubygems
installed. You can then install jekyll with the command

```
gem install jekyll
```

Optionally, you can install [Fabric](http://docs.fabfile.org/en/1.8/), which is
a command-line tool written in Python that helps streamline some common
commands. You will have to install Fabric if you wish to make use of the `fab`
commands mentioned below, but it's not required to build the site. (It just
means less typing for you.)

# Usage instructions

## Building

To build the static site, run `jekyll` in the root of the repository. That will
generate the static files for the site under the `_site/` directory. You can
then transfer those files to the production server as-is.

## Developing

You can run a local development server at <http://localhost:4000> by running

```
fab up
```

or `jekyll serve --watch` if you don't have Fabric installed. Any changes you
make will cause the server to automatically reload.

## Editing content

Most of the content of the pages is stored in the Markdown files (`*.md`) in
the root of this repository. For example, the file about.md holds the content
for the generated about.html.
