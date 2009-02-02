%include	/usr/lib/rpm/macros.java
Summary:	Alternative Servlet implementation
Summary(pl.UTF-8):	Alternatywna implementacja Java Servlet API
Name:		java-classpathx_servlet
Version:	20000924
Release:	4
License:	LGPL
Group:		Libraries/Java
Source0:	http://www.euronet.nl/~pauls/java/servlet/download/classpathx_servlet-%{version}.tar.gz
# Source0-md5:	a81feddb91b1358f9aaed94e83eddb54
URL:		http://www.euronet.nl/~pauls/java/servlet/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Provides:	classpathx_servlet
Provides:	servlet = 2.0
Provides:	servlet = 2.1
Provides:	servlet = 2.2
Obsoletes:	classpathx_servlet < 20000924-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a LGPL'ed implementation of Sun's Java Servlet API version
2.0, version 2.1 and recently there is preliminary support for version
2.2.

%description -l pl.UTF-8
Ten pakiet zawiera wydaną na licencji LGPL implementację Java Servlet
API Suna w wersji 2.0, wersji 2.1 oraz częściowo wersji 2.2.

%package javadoc
Summary:	Online manual for classpathx servlet
Summary(pl.UTF-8):	Dokumentacja online do classpathx servlet
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for classpathx servlet.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do classpathx servlet.

%description javadoc -l fr.UTF-8
Javadoc pour classpathx servlet.

%prep
%setup -q -n classpathx_servlet-%{version}
find -name '*.jar' | xargs rm -v

%build
export JAVA_HOME="%{java_home}"
%{__make} -j1 \
	J_COMPILER="%javac"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a servlet-2.0.jar $RPM_BUILD_ROOT%{_javadir}
cp -a servlet-2.1.jar $RPM_BUILD_ROOT%{_javadir}
cp -a servlet-2.2.jar $RPM_BUILD_ROOT%{_javadir}
cp -a servlet_intl-2.0.jar $RPM_BUILD_ROOT%{_javadir}
cp -a servlet_intl-2.1.jar $RPM_BUILD_ROOT%{_javadir}
cp -a servlet_intl-2.2.jar $RPM_BUILD_ROOT%{_javadir}

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a apidoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/{Makefile,CVS}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README Resources TODO
%{_javadir}/servlet-2.0.jar
%{_javadir}/servlet-2.1.jar
%{_javadir}/servlet-2.2.jar
%{_javadir}/servlet_intl-2.0.jar
%{_javadir}/servlet_intl-2.1.jar
%{_javadir}/servlet_intl-2.2.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
