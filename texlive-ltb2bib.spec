%global tl_name ltb2bib
%global tl_revision 43746

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Converts amsrefs .ltb bibliographical databases to BibTeX format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/utils/ltb2bib
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltb2bib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltb2bib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltb2bib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a LaTeX command that converts an amsrefs
bibliographical database (.ltb) to a BibTeX bibliographical database
(.bib). ltb2bib is the reverse of the "amsxport" option in amsrefs.
Typical uses are: produce bib entries for some publishers which don't
accept amsrefs (Taylor & Francis, for example); import an ltb database
in a database management program, e.g. for sorting; access one's ltb
database within emacs's RefTeX mode.

