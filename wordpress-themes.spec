Summary:	Additional themes for the WordPress personal publishing system
Summary(pl):	Dodatkowe motywy dla osobistego systemu publikacji WordPress
Name:		wordpress-themes
Version:	1.5
Release:	2
License:	GPL
Group:		Applications/Publishing
URL:		http://codex.wordpress.org/Using_Themes
#Source0:	http://www.thoughtmechanics.com/templatefiles/v2.2/download.php?get=bionicjive.zip
Source0:	bionicjive.zip
# Source0-md5:	8702b83c2909ed0741ffc4dec7bb0b23
# Source12:	http://www.thoughtmechanics.com/templatefiles/v2.2/download.php?get=benevolence.zip
Source12:	benevolence.zip
# Source12-md5:	c35dd174ff183aad0ee11cef4b38689f
Source13:	http://www.eretzvaju.org/download/black.tgz
# Source13-md5:	628e7dc2a505a1fb66536b3dec8c7ba5
Source14:	http://www.bighead.cn/wp-content/themes/ChinaRed_1.0_Alpha.zip
# Source14-md5:	a31cc7c191b6e5dbe470b7b3e9e13edc
Source15:	http://chris.coggburn.us/wp-content/cleanbreeze/releases/cleanbreeze111.zip
# Source15-md5:	e033d64efc56c2cf74f333c3361a30f4
#Source16:	http://www.thoughtmechanics.com/templatefiles/v2.2/download.php?get=Conestogastreet.zip
Source16:	Conestogastreet.zip
# Source16-md5:	044ade9ef3b0990999e21750e4300fcc
Source17:	http://www.eretzvaju.org/download/devenir_en_gris.tgz
# Source17-md5:	85f39ca8b50c1839d9c1a6b44d21b2ff
Source18:	http://supremecolor.xoopiter.com/LtStuff/dxx.rar
# Source18-md5:	f70f5296922b5d057635de1acafcd305
Source20:	http://www.lamateporunyogur.com/misc/hiperminimalist-v1.zip
# Source20-md5:	3609764bcac123e13aea05b49eeaf6df
Source21:	http://devel.bluegator.org/themes/1.5/Neuron/Neuron.zip
# Source21-md5:	e4ec2b79f20bd296b46a834dca5a99d8
Source22:	http://www.eretzvaju.org/download/old_train.tgz
# Source22-md5:	4709fa3f8176d30d75eaaaa9e57bcf54
Source23:	http://www.hpnadig.net/wordpress-themes/parishuddha.tar.gz
# Source23-md5:	3ba796ead903bd28e45c50970311539b
Source24:	http://www.lamateporunyogur.com/misc/pool-v106.zip
# Source24-md5:	e8c23b49d195c6291acfa730d74db226
Source25:	http://www.eretzvaju.org/download/spiral.tgz
# Source25-md5:	0a66ad6187795e0d4763454e9b031e32
Source26:	http://www.bbiverson.com/spirit/wp-content/spirit.zip
# Source26-md5:	7e0c9f7a6fdf32ccda102c3d9572a48c
# Source27:	http://www.steamedpenguin.com/get/steam-1.5.tar.bz2
Source27:	steam-1.5.tar.bz2
# Source27-md5:	c19dc9d2703053baf7da9b93bc6b7e16
# Source28:	http://www.thoughtmechanics.com/templatefiles/v2.2/download.php?get=thoughtmechanics.zip
Source28:	thoughtmechanics.zip
# Source28-md5:	ab7bd7c6eb775600bee34b1f4c7631d1
Source29:	http://www.eretzvaju.org/download/trident.tgz
# Source29-md5:	f384f5f6276c7702a9ccb3fe3c5c7f13
BuildRequires:	FIX-FILES(numerous duplicates)
BuildRequires:	unrar
Requires:	wordpress = %{version}
Obsoletes:	wordpress-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	wordpressdir	/home/services/httpd/html/wordpress
%define	themessubdir	wp-content/themes
%define	themesdir	%{wordpressdir}/%{themessubdir}

%description
WordPress is a state-of-the-art semantic personal publishing platform
with a focus on aesthetics, web standards, and usability.

This package provides additional themes for WordPress found in the
Net, which are released under GNU GPL license.

%description -l pl
WordPress jest technologicznie dopracowan±, semantyczn±, osobist±
platform± do publikacji k³ad±c± nacisk na standardy WWW oraz
u¿yteczno¶æ.

Ten pakiet dostarcza dodatkowe motywy dla WordPress znalezione w
Sieci, które s± udostêpniane na warunkach okre¶lonych w licencji GNU
GPL.

%package -n wordpress-theme-Bionicjive
Summary:	Bionicjive theme for WordPress
Summary(pl):	Motyw Bionicjive dla WordPress
Group:		Applications/Publishing
URL:		http://www.thoughtmechanics.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Bionicjive
The Bionicjive theme for WordPress publishing system.

%description -n wordpress-theme-Bionicjive -l pl
Motyw Bionicjive dla systemu publikacji WordPress.

%package -n wordpress-theme-Benevolence
Summary:	Benevolence theme for WordPress
Summary(pl):	Motyw Benevolence dla WordPress
Group:		Applications/Publishing
URL:		http://www.thoughtmechanics.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Benevolence
The Benevolence theme for WordPress publishing system.

%description -n wordpress-theme-Benevolence -l pl
Motyw Benevolence dla systemu publikacji WordPress.

%package -n wordpress-theme-Black
Summary:	Black theme for WordPress
Summary(pl):	Motyw Black dla WordPress
Group:		Applications/Publishing
URL:		http://www.eretzvaju.org/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Black
The Black theme for WordPress publishing system.

%description -n wordpress-theme-Black -l pl
Motyw Black dla systemu publikacji WordPress.

%package -n wordpress-theme-ChinaRed_1
Summary:	ChinaRed_1 theme for WordPress
Summary(pl):	Motyw ChinaRed_1 dla WordPress
Group:		Applications/Publishing
URL:		http://www.bighead.cn/wp-content/themes/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-ChinaRed_1
The ChinaRed_1 theme for WordPress publishing system.

%description -n wordpress-theme-ChinaRed_1 -l pl
Motyw ChinaRed_1 dla systemu publikacji WordPress.

%package -n wordpress-theme-Cleanbreeze
Summary:	Cleanbreeze theme for WordPress
Summary(pl):	Motyw Cleanbreeze dla WordPress
Group:		Applications/Publishing
URL:		http://chris.coggburn.us/wp-content/cleanbreeze/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Cleanbreeze
The Cleanbreeze111 theme for WordPress publishing system.

%description -n wordpress-theme-Cleanbreeze -l pl
Motyw Cleanbreeze111 dla systemu publikacji WordPress.

%package -n wordpress-theme-Conestogastreet
Summary:	Conestogastreet theme for WordPress
Summary(pl):	Motyw Conestogastreet dla WordPress
Group:		Applications/Publishing
URL:		http://www.thoughtmechanics.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Conestogastreet
The Conestogastreet theme for WordPress publishing system.

%description -n wordpress-theme-Conestogastreet -l pl
Motyw Conestogastreet dla systemu publikacji WordPress.

%package -n wordpress-theme-Devenir_en_gris
Summary:	Devenir_en_gris theme for WordPress
Summary(pl):	Motyw Devenir_en_gris dla WordPress
Group:		Applications/Publishing
URL:		http://www.eretzvaju.org/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Devenir_en_gris
The Devenir_en_gris theme for WordPress publishing system.

%description -n wordpress-theme-Devenir_en_gris -l pl
Motyw Devenir_en_gris dla systemu publikacji WordPress.

%package -n wordpress-theme-Dxx
Summary:	Dxx theme for WordPress
Summary(pl):	Motyw Dxx dla WordPress
Group:		Applications/Publishing
URL:		http://supremecolor.xoopiter.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Dxx
The Dxx theme for WordPress publishing system.

%description -n wordpress-theme-Dxx -l pl
Motyw Dxx dla systemu publikacji WordPress.

%package -n wordpress-theme-Hiperminimalist_v1
Summary:	Hiperminimalist theme for WordPress
Summary(pl):	Motyw Hiperminimalist dla WordPress
Group:		Applications/Publishing
URL:		http://www.lamateporunyogur.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Hiperminimalist_v1
The Hiperminimalist theme for WordPress publishing system.

%description -n wordpress-theme-Hiperminimalist_v1 -l pl
Motyw Hiperminimalist dla systemu publikacji WordPress.

%package -n wordpress-theme-Neuron
Summary:	Neuron theme for WordPress
Summary(pl):	Motyw Neuron dla WordPress
Group:		Applications/Publishing
URL:		http://devel.bluegator.org/themes/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Neuron
The Neuron theme for WordPress publishing system.

%description -n wordpress-theme-Neuron -l pl
Motyw Neuron dla systemu publikacji WordPress.

%package -n wordpress-theme-Old_train
Summary:	Old_train theme for WordPress
Summary(pl):	Motyw Old_train dla WordPress
Group:		Applications/Publishing
URL:		http://www.eretzvaju.org/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Old_train
The Old_train theme for WordPress publishing system.

%description -n wordpress-theme-Old_train -l pl
Motyw Old_train dla systemu publikacji WordPress.

%package -n wordpress-theme-Parishuddha
Summary:	Parishuddha theme for WordPress
Summary(pl):	Motyw Parishuddha dla WordPress
Group:		Applications/Publishing
URL:		http://www.hpnadig.net/wordpress-themes/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Parishuddha
The Parishuddha theme for WordPress publishing system.

%description -n wordpress-theme-Parishuddha -l pl
Motyw Parishuddha dla systemu publikacji WordPress.

%package -n wordpress-theme-Pool_v106
Summary:	Pool theme for WordPress
Summary(pl):	Motyw Pool dla WordPress
Group:		Applications/Publishing
URL:		http://www.lamateporunyogur.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Pool_v106
The Pool theme for WordPress publishing system.

%description -n wordpress-theme-Pool_v106 -l pl
Motyw Pool dla systemu publikacji WordPress.

%package -n wordpress-theme-Spiral
Summary:	Spiral theme for WordPress
Summary(pl):	Motyw Spiral dla WordPress
Group:		Applications/Publishing
URL:		http://www.eretzvaju.org/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Spiral
The Spiral theme for WordPress publishing system.

%description -n wordpress-theme-Spiral -l pl
Motyw Spiral dla systemu publikacji WordPress.

%package -n wordpress-theme-Spirit
Summary:	Spirit theme for WordPress
Summary(pl):	Motyw Spirit dla WordPress
Group:		Applications/Publishing
URL:		http://www.bbiverson.com/spirit/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Spirit
The Spirit theme for WordPress publishing system.

%description -n wordpress-theme-Spirit -l pl
Motyw Spirit dla systemu publikacji WordPress.

%package -n wordpress-theme-Steam
Summary:	Steam theme for WordPress
Summary(pl):	Motyw Steam dla WordPress
Group:		Applications/Publishing
URL:		http://www.steamedpenguin.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Steam
The Steam theme for WordPress publishing system.

%description -n wordpress-theme-Steam -l pl
Motyw Steam dla systemu publikacji WordPress.

%package -n wordpress-theme-Thoughtmechanics
Summary:	Thoughtmechanics theme for WordPress
Summary(pl):	Motyw Thoughtmechanics dla WordPress
Group:		Applications/Publishing
URL:		http://www.thoughtmechanics.com/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Thoughtmechanics
The Thoughtmechanics theme for WordPress publishing system.

%description -n wordpress-theme-Thoughtmechanics -l pl
Motyw Thoughtmechanics dla systemu publikacji WordPress.

%package -n wordpress-theme-Trident
Summary:	Trident theme for WordPress
Summary(pl):	Motyw Trident dla WordPress
Group:		Applications/Publishing
URL:		http://www.eretzvaju.org/
Requires:	wordpress
Provides:	wordpress-theme
Obsoletes:	wordpress-themes

%description -n wordpress-theme-Trident
The Trident theme for WordPress publishing system.

%description -n wordpress-theme-Trident -l pl
Motyw Trident dla systemu publikacji WordPress.

%prep
%setup -q -c -a12 -a13 -a14 -a15 -a16 -a17 -a21 -a22 -a23 -a25 -a26 -a27 -a28 -a29
unzip -qq %{SOURCE20} -d hiperminimalist-v1
unzip -qq %{SOURCE24} -d pool-v106
unrar -inul x %{SOURCE18}
chmod u+rw devenir_en_gris

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{wordpressdir} $RPM_BUILD_ROOT%{themesdir}
cp -R * $RPM_BUILD_ROOT%{themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(640,root,http,750)
%dir %{wordpressdir}
%dir %{themesdir}
%{themesdir}/*
%{themesdir}/*/*

%files -n wordpress-theme-Bionicjive
%defattr(640,root,http,750)
%dir %{themesdir}/bionicjive
%{themesdir}/bionicjive/*
%{themesdir}/bionicjive/*/*

%files -n wordpress-theme-Benevolence
%defattr(640,root,http,750)
%dir %{themesdir}/benevolence
%{themesdir}/benevolence/*
%{themesdir}/benevolence/*/*

%files -n wordpress-theme-Black
%defattr(640,root,http,750)
%dir %{themesdir}/black
%{themesdir}/black/*

%files -n wordpress-theme-ChinaRed_1
%defattr(640,root,http,750)
%dir %{themesdir}/China*Red*
%{themesdir}/China*Red*/*
%{themesdir}/China*Red*/*/*

%files -n wordpress-theme-Cleanbreeze
%defattr(640,root,http,750)
%dir %{themesdir}/cleanbreeze
%{themesdir}/cleanbreeze/*
%{themesdir}/cleanbreeze/*/*

%files -n wordpress-theme-Conestogastreet
%defattr(640,root,http,750)
%dir %{themesdir}/Conestogastreet
%{themesdir}/Conestogastreet/*
%{themesdir}/Conestogastreet/*/*

%files -n wordpress-theme-Devenir_en_gris
%defattr(640,root,http,750)
%dir %{themesdir}/devenir_en_gris
%{themesdir}/devenir_en_gris/*

%files -n wordpress-theme-Dxx
%defattr(640,root,http,750)
%dir %{themesdir}/dxx
%{themesdir}/dxx/*

%files -n wordpress-theme-Hiperminimalist_v1
%defattr(640,root,http,750)
%dir %{themesdir}/hiperminimalist-v1
%{themesdir}/hiperminimalist-v1/*

%files -n wordpress-theme-Neuron
%defattr(640,root,http,750)
%dir %{themesdir}/Neuron
%{themesdir}/Neuron/*
%{themesdir}/Neuron/*/*

%files -n wordpress-theme-Old_train
%defattr(640,root,http,750)
%dir %{themesdir}/old_train
%{themesdir}/old_train/*
%{themesdir}/old_train/*/*

%files -n wordpress-theme-Parishuddha
%defattr(640,root,http,750)
%dir %{themesdir}/parishuddha
%{themesdir}/parishuddha/*

%files -n wordpress-theme-Pool_v106
%defattr(640,root,http,750)
%dir %{themesdir}/pool-v106
%{themesdir}/pool-v106/*
%{themesdir}/pool-v106/*/*

%files -n wordpress-theme-Spiral
%defattr(640,root,http,750)
%dir %{themesdir}/spiral
%{themesdir}/spiral/*
%{themesdir}/spiral/*/*

%files -n wordpress-theme-Spirit
%defattr(640,root,http,750)
%dir %{themesdir}/spirit
%{themesdir}/spirit/*
%{themesdir}/spirit/*/*

%files -n wordpress-theme-Steam
%defattr(640,root,http,750)
%dir %{themesdir}/steam
%{themesdir}/steam/*

%files -n wordpress-theme-Thoughtmechanics
%defattr(640,root,http,750)
%dir %{themesdir}/thoughtmechanics
%{themesdir}/thoughtmechanics/*
%{themesdir}/thoughtmechanics/*/*

%files -n wordpress-theme-Trident
%defattr(640,root,http,750)
%dir %{themesdir}/trident
%{themesdir}/trident/*
