%define product         CMFDynamicViewFTI
%define ver             2.1
%define rel             1

%define zope_minver     2.7

%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python


Summary:        Product for dynamic views in CMF 1.5
Name:           zope-%{product}
Version:        %{ver}
Release:        %mkrel %{rel}
License:        GPL
Group:          System/Servers
Source:         http://plone.org/products/cmfdynamicviewfti/releases/%{ver}/CMFDynamicViewFTI-%{ver}.tar.bz2
URL:            http://plone.org/products/cmfdynamicviewfti
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       zope >= %{zope_minver}
Requires:       zope-CMF >= 1.5


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
%defattr(-, root, root, 0755)
%{software_home}/Products/*




