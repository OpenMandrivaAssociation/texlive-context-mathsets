# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-mathsets
# catalog-date 2011-05-13 02:08:48 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-context-mathsets
Version:	20110513
Release:	1
Summary:	Set notation in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-mathsets
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-mathsets.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-mathsets.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-context.bin

%description
Typeset good-looking set notation (e.g., {x|x \in Y}), as well
as similar things such as Dirac bra-ket notation, conditional
probabilities, etc. The package is a partial port of Donald
Arseneau's LaTeX package braket.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-mathsets.xml
%{_texmfdistdir}/tex/context/third/mathsets/t-mathsets.tex
%doc %{_texmfdistdir}/doc/context/third/mathsets/mathsets-doc.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
