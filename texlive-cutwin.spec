# revision 20000
# category Package
# catalog-ctan /macros/latex/contrib/cutwin
# catalog-date 2010-10-04 12:17:09 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-cutwin
Version:	0.1
Release:	1
Summary:	Cut a window in a paragraph, typeset material in it
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cutwin
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides facilities to cut windows out of
paragraphs, and to typeset text or other material in the
window. The window may be rectangular, or may have other sorts
of shape.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cutwin/cutwin.sty
%doc %{_texmfdistdir}/doc/latex/cutwin/README
%doc %{_texmfdistdir}/doc/latex/cutwin/cutwin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cutwin/cutwin.dtx
%doc %{_texmfdistdir}/source/latex/cutwin/cutwin.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
