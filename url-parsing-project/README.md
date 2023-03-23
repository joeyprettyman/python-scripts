
# URL Parsing Project
I have used `urllib.parse` for a while now, and I'm not aware of a solid solution that allows the `urlparse()` method to consistently get certain parts of the URL correct. I am compiling a list of things that this project will hopefully solve, but the filename and extension are both primary areas of interest for me personally.

If there is a project out there that does this with high precision, please let me know, because it would save me a lot of trouble having to write my own.

I think the `hostname`, in particular, is a difficult area to manage because of `tlds`, `country-codes`, `punycode`, etc. As it turns out, there's a lot more at play in that little URL bar at the top of my browser than I thought.

Another problem that I've noticed is, when you start to look around at resources online, you begin to realize that there isn't a whole lot of consensus on this stuff. I mean, there *technically is* a broad sense of understanding, but not precision, which surprised me. As geeks, we are generally exceptional at outlining things that no one cares about (until they do), however, it seems like that might not be the case.

+ Was it `scheme` or `protocol`?
	+ If they are the same, then why do they have separate names?
	+ Is the **full** scheme/protocol `https:` or is it `https:` or is it `https://`?
+ Was is `host` or `hostname`?
+ Was it `domain` or `domain name` or `fully-qualified domain name`, etc.?

There are loose enough rules, for us to get what we need, but the use-cases haven't really presented themselves consistently across languages. Tim Burners-Lee defined the URI in a format that has since changed.
He is actually quoted as having admitted to regretting the `//` in the `https://` scheme.

From my understanding, if an `authority` is provided, then the `//` is required after the `https` portion of the scheme. The authority being your domain.

There's a lot of minutia to all of this, but I'd like to pin down a universal standard. Fortunately GitHub has some code examples from developers at Google who wrote the Chrome drivers along with some other good examples to gather inspiration and direction from.

When in doubt, study the greats! More to come.