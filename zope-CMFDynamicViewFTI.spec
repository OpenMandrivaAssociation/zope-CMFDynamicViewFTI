%define Product CMFDynamicViewFTI
%define product cmfdynamicviewfti
%define name    zope-%{Product}
%define version 3.0.1
%define release %mkrel 4

%define zope_minver     2.10
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Product for dynamic views in CMF 1.5
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:    zope >= %{zope_minver}
Requires:    zope-CMF >= 2.1
BuildArch:   noarch
BuildRoot:   %{_tmppath}/%{name}-%{version}

%description
CMFDynamicViewFTI is a product for dynamic views in CMF 1.5. The product
contains an additional base class for types and a new factory type information
(FTI).

The FTI contains two new properties for the default view method and
supplementary view methods. The queryMethodID functionality used for
alias lookups is enhanced to support a new keyword (dynamic view).

The BrowserDefaultMixin class adds some methods to classes. It is not required
to make use of the basic features but it is recommend to subclass your types
from the class to gain more functionality.




%prep
%setup -c -q

rm -rf `find -type d -name .svn`

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
