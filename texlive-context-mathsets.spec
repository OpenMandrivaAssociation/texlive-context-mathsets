%global tl_name context-mathsets
%global tl_revision 47085

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Set notation in ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-mathsets
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-mathsets.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-mathsets.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typeset good-looking set notation (e.g., {x|x \in Y}), as well as
similar things such as Dirac bra-ket notation, conditional
probabilities, etc. The package is at least inspired by braket.

