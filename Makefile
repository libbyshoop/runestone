# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
COURSEID = devcourse
APPNAME = runestone
LOGLEVEL = 10
#COURSEURL = http://127.0.0.1:8000
COURSEURL = http://141.140.167.226:8000

LOGINREQ = true
#
#
TEMPLATEDEFS  = -A course_id=$(COURSEID) -A appname=$(APPNAME) -A loglevel=$(LOGLEVEL) -A course_url=$(COURSEURL) -A login_required=$(LOGINREQ)
SPHINXOPTS    = -a -E 
#SPHINXOPTS    = 
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = static/$(COURSEID)

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(TEMPLATEDEFS) source
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html thinkcspy pythonds dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext 

help:
	@echo "Please use \'make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"


all:	thinkcspy pythonds html

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)"

thinkcspy: COURSEID=thinkcspy
thinkcspy: LOGINREQ=false
thinkcspy:
	cp source/OldIndexAndConfFiles/index-thinkcs source/index.rst
	cp source/OldIndexAndConfFiles/thinkcs-conf.py source/conf.py
	$(SPHINXBUILD) -d static/thinkcspy/doctrees $(SPHINXOPTS) -A project='How to Think Like a Computer Scientist Interactive Edition' $(TEMPLATEDEFS) source static/$(COURSEID)
	cp source/OldIndexAndConfFiles/index-master source/index.rst
	cp source/OldIndexAndConfFiles/master-conf.py source/conf.py

pythonds: COURSEID=pythonds
pythonds: LOGINREQ=false
pythonds:
	cp source/OldIndexAndConfFiles/index-pythonds source/index.rst
	cp source/OldIndexAndConfFiles/pythonds-conf.py source/conf.py
	$(SPHINXBUILD) -d static/pythonds/doctrees $(SPHINXOPTS) -D project='Problem Solving with Algorithms and Data Structures' $(TEMPLATEDEFS) source static/$(COURSEID)
	cp source/OldIndexAndConfFiles/index-master source/index.rst
	cp source/OldIndexAndConfFiles/master-conf.py source/conf.py

luther151:	COURSEID=luther151
luther151:	COURSEURL=http://interactivepython.org
luther151:
	cp source/OldIndexAndConfFiles/index-pythonds source/index.rst
	cp source/OldIndexAndConfFiles/pythonds-conf.py source/conf.py
	$(SPHINXBUILD) -d static/pythonds/doctrees $(SPHINXOPTS) -D project='Problem Solving with Algorithms and Data Structures' $(TEMPLATEDEFS) source static/$(COURSEID)
	cp source/OldIndexAndConfFiles/index-master source/index.rst
	cp source/OldIndexAndConfFiles/master-conf.py source/conf.py

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/ProblemSolvingwithAlgorithmsandDataStructures.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/ProblemSolvingwithAlgorithmsandDataStructures.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/ProblemSolvingwithAlgorithmsandDataStructures"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/ProblemSolvingwithAlgorithmsandDataStructures"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."
