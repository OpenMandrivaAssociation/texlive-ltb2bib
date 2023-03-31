Name:		texlive-ltb2bib
Version:	43746
Release:	2
Summary:	Converts amsrefs' .ltb bibliographical databases to BibTeX format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltb2bib
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltb2bib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltb2bib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltb2bib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a LaTeX command that converts an
amsrefs bibliographical database (.ltb) to a BibTeX
bibliographical database (.bib). ltb2bib is the reverse of the
"amsxport" option in amsrefs. Typical uses are: produce bib
entries for some publishers which don't accept amsrefs (Taylor
& Francis, for example); import an ltb database in a database
management program, e.g. for sorting; access one's ltb database
within emacs's RefTeX mode.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ltb2bib
%{_texmfdistdir}/tex/latex/ltb2bib
%doc %{_texmfdistdir}/doc/latex/ltb2bib

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
