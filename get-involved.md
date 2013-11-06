---
layout: default
title: Get involved
---

We always need more help improving Octave and there are many ways you can
contribute. You can help by fixing bugs, developing new features, answering
questions on the mailing list or IRC channel, helping to improve the web pages.

If you are wondering what to work on, we have a standard answer: what would you
like to work on? We try not to tell contributors what to work on as most people
do their best work when they are within their own field of interest. So, we
would love your help, but would also love for you to work on what you love.

If you need some inspiration, we do maintain a [list of possible
projects][projects] on the Wiki.

If you have an idea on what to contribute, then join the maintainers mailing
list or the IRC channel and discuss your ideas there (see the next section for
details). That way others can provide input early on, which makes your
contribution more likely to get accepted.

## Contacting developers

If you want to participate in Octave development, you should join the
[maintainers@octave.org][maintainers] mailing list. Please use this list only
if you are participating in Octave's development. If you are looking for help
in using Octave, please use the [help@octave.org][help] list instead, or check
out other [support options][support].

For sometimes faster communication, you can also chat in IRC in [#octave in
Freenode][irc]. Note, however, that the primary medium for development talk is
the mailing list.

## Using the development sources

The latest development sources of Octave are also available via [Mercurial][hg]
(hg) archive.

The primary archive address is <http://www.octave.org/hg/octave>, which currently
redirects to <http://hg.savannah.gnu.org/hgweb/octave>.

If you decide to use the development sources from the Mercurial archive, please
read the file [etc/HACKING][hacking] that is available with the source files.

Assuming you have Mercurial and git installed on your machine you may obtain
the latest development version of Octave sources with the following command:

    hg clone http://www.octave.org/hg/octave

This will clone _two_ repositories, one of which is subrepository of the main
Octave repository. Once you have these, you can resync with the archive by
doing

    hg -v pull ## -v means "verbose", to get more diagnostic output
    hg -v update

The -v option is not required but provides extra information about what was
pulled and updated. The Octave manual has more information about [contributing
to Octave's development][contributing].

[projects]: http://www.octave.org/wiki/Projects
[maintainers]: https://mailman.cae.wisc.edu/listinfo/octave-maintainers
[help]: https://mailman.cae.wisc.edu/listinfo/help-octave
[support]: /support/
[irc]: http://webchat.freenode.net/?channels=octave
[hg]: http://www.selenic.com/mercurial/wiki
[hacking]: http://www.octave.org/hg/octave/file/tip/etc/HACKING
[contributing]: http://www.gnu.org/software/octave/doc/interpreter/Contributing-Guidelines.html#Contributing-Guidelines
