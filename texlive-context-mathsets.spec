Name:		texlive-context-mathsets
Version:	47085
Release:	2
Summary:	Set notation in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-mathsets
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-mathsets.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-mathsets.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
Typeset good-looking set notation (e.g., {x|x \in Y}), as well
as similar things such as Dirac bra-ket notation, conditional
probabilities, etc. The package is a partial port of Donald
Arseneau's LaTeX package braket.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-mathsets.xml
%{_texmfdistdir}/tex/context/third/mathsets
%doc %{_texmfdistdir}/doc/context/third/mathsets

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
