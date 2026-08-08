%global tl_name l3kernel-dev
%global tl_revision 79878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Development pre-release of l3kernel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex-dev/required/l3kernel
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel-dev.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel-dev.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel-dev.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(l3backend-dev)
Requires:	texlive(lua-uni-algos)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a pre-release version of the l3kernel package. It accompanies
the pre-testing kernel code (latex-base-dev), and is intended for
testing by knowledgeable users.

