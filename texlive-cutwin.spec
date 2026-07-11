%global tl_name cutwin
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Cut a window in a paragraph, typeset material in it
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cutwin
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cutwin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides facilities to cut windows out of paragraphs, and to
typeset text or other material in the window. The window may be
rectangular, or may have other sorts of shape.

