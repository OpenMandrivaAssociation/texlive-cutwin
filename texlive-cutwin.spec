Name:		texlive-cutwin
Version:	60901
Release:	2
Summary:	Cut a window in a paragraph, typeset material in it
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cutwin
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/cutwin
%doc %{_texmfdistdir}/doc/latex/cutwin
#- source
%doc %{_texmfdistdir}/source/latex/cutwin

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
