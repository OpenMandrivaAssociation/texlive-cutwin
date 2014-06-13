# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/cutwin
# catalog-date 2012-05-30 14:33:40 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-cutwin
Version:	0.1
Release:	8
Summary:	Cut a window in a paragraph, typeset material in it
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cutwin
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides facilities to cut windows out of
paragraphs, and to typeset text or other material in the
window. The window may be rectangular, or may have other sorts
of shape.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cutwin/cutwin.sty
%doc %{_texmfdistdir}/doc/latex/cutwin/README
%doc %{_texmfdistdir}/doc/latex/cutwin/cutwin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cutwin/cutwin.dtx
%doc %{_texmfdistdir}/source/latex/cutwin/cutwin.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
